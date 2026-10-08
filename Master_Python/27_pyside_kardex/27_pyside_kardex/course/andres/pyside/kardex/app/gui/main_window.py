from decimal import InvalidOperation

from PySide6.QtWidgets import QHBoxLayout, QFileDialog
import pandas as pd
import csv

from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QDialog, QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout
)
from PySide6.QtCore import Qt

from course.andres.pyside.kardex.app.config.db import SessionLocal
from course.andres.pyside.kardex.app.entity.operation import Operation
from course.andres.pyside.kardex.app.gui.financial_form_dialog import FinancialFormDialog
from course.andres.pyside.kardex.app.models.dto.operation_with_balance import OperationWithBalance
from course.andres.pyside.kardex.app.repositories.operation_repository_impl import OperationRepositoryImpl


def _safe_decimal(value: str | None) -> float:
    if not value:
        return float('0')
    value = value.replace(',', '.').strip()
    try:
        return float(value)
    except InvalidOperation:
        return float('0')


def dto_to_entity(dto: OperationWithBalance) -> Operation:
    return Operation(
        id=dto.id,
        company=dto.company,
        account_number=dto.account_number,
        issuer=dto.issuer,
        operation=dto.operation,
        movement_date=dto.movement_date,
        instrument=dto.instrument,
        quantity=dto.quantity,
        price=dto.price
    )


class MainWindow(QMainWindow):
    """
    Ventana principal con layout vertical:
    - Arriba: botón "Registrar operación" (abre modal)
    - Abajo: tabla (placeholder de grid) para mostrar datos
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operaciones Financieras")
        self.resize(1080, 720)
        self.operations_by_id: dict[int, OperationWithBalance] = {}
        # Repository (session factory injected)
        self.operation_repo = OperationRepositoryImpl(SessionLocal)

        # Root central
        central = QWidget()
        self.setCentralWidget(central)

        # Layout vertical raíz
        root_layout = QVBoxLayout(central)
        button_pane = QWidget()
        button_layout = QHBoxLayout(button_pane)

        # Botón superior
        self.register_button = QPushButton("Registrar operación")
        self.register_button.clicked.connect(self.open_register_dialog)
        button_layout.addWidget(self.register_button, alignment=Qt.AlignmentFlag.AlignLeft)

        self.export_csv_button = QPushButton("Exportar CSV")
        self.export_csv_button.clicked.connect(self.export_to_csv)
        button_layout.addWidget(self.export_csv_button)

        self.export_excel_button = QPushButton("Exportar Excel")
        self.export_excel_button.clicked.connect(self.export_to_excel)
        button_layout.addWidget(self.export_excel_button)

        self.export_pdf_button = QPushButton("Exportar PDF")
        self.export_pdf_button.clicked.connect(self.export_to_pdf)
        button_layout.addWidget(self.export_pdf_button)

        self.refresh_button = QPushButton('Refrescar')
        self.refresh_button.clicked.connect(self.refresh_table)
        button_layout.addWidget(self.refresh_button, alignment=Qt.AlignmentFlag.AlignRight)
        button_layout.addStretch()
        root_layout.addWidget(button_pane)

        # Tabla inferior (placeholder tipo grid)
        self.table = QTableWidget(0, 11)
        self.table.setHorizontalHeaderLabels([
            "ID",
            "Compañía",
            "Número de cuenta",
            "Emisor",
            "Operación",
            "Fecha de movimiento",
            "Instrumento",
            "Cantidad",
            "Balance",
            "Precio",
            "Acciones",
        ])
        self._action_col_index = 10  # índice de la columna "Acciones"
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setAlternatingRowColors(True)
        root_layout.addWidget(self.table)
        # Initial load from DB
        self.load_operations()

    # ---------- DB <-> UI helpers ----------

    def refresh_table(self):
        self.load_operations()

    def load_operations(self):
        """
        Load all operations from the database and fill the table.
        """
        try:
            operations = self.operation_repo.find_all_with_balance()
        except Exception as exc:
            QMessageBox.critical(
                self,
                "Error",
                f"Error al cargar operaciones desde la base de datos:\n{exc}",
            )
            return

        self.operations_by_id.clear()
        self.table.setRowCount(0)

        for op in operations:
            if op.id is None:
                continue
            self.operations_by_id[int(str(op.id))] = op
            self._append_operation_to_table(op)

    def _append_operation_to_table(self, operation: OperationWithBalance):
        """
        Append a single Operation row to the table.
        """
        row = self.table.rowCount()
        self.table.insertRow(row)

        values = [
            operation.id,
            operation.company,
            operation.account_number,
            operation.issuer,
            operation.operation,
            operation.movement_date.isoformat() if operation.movement_date else "",
            operation.instrument,
            str(operation.quantity),
            str(operation.balance),
            str(operation.price),
        ]

        for col, value in enumerate(values):
            item = QTableWidgetItem(str(value) if value is not None else "")
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, col, item)

        # Botones Editar + Eliminar
        # self._add_action_button(row, int(str(operation.id))) # type: ignore[arg-type]
        self._add_action_button(row, operation.id)

    def _add_action_button(self, row: int, operation_id: int):
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        btn_edit = QPushButton("Editar")
        btn_delete = QPushButton("Eliminar")

        btn_edit.setProperty("operation_id", operation_id)
        btn_delete.setProperty("operation_id", operation_id)

        btn_edit.clicked.connect(self.on_edit_clicked)
        btn_delete.clicked.connect(self.on_delete_clicked)

        layout.addWidget(btn_edit)
        layout.addWidget(btn_delete)
        layout.addStretch()

        self.table.setCellWidget(row, self._action_col_index, container)

    def _update_operation_row(self, row: int, operation: Operation):
        values = [
            operation.id,
            operation.company,
            operation.account_number,
            operation.issuer,
            operation.operation,
            operation.movement_date.isoformat() if operation.movement_date else "",
            operation.instrument,
            str(operation.quantity),
            str(operation.balance),
            str(operation.price),
        ]

        for col, value in enumerate(values):
            item = self.table.item(row, col)
            if item is None:
                item = QTableWidgetItem()
                self.table.setItem(row, col, item)
            item.setText(str(value) if value is not None else "")

    def _find_row_for_button(self, button: QPushButton) -> int:
        """
        Busca la fila que contiene el botón dado dentro de la columna Actions.
        """
        for row in range(self.table.rowCount()):
            container = self.table.cellWidget(row, self._action_col_index)
            if container is None:
                continue
            # ¿El botón es hijo de este contenedor?
            if button in container.findChildren(QPushButton):
                return row
        return -1

    # ---------- UI actions ----------
    def open_register_dialog(self):
        dialog = FinancialFormDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_new_operation_data()
            operation = Operation(**data)

            try:
                saved = self.operation_repo.save(operation)
            except Exception as exc:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Error al guardar la operación en la base de datos:\n{exc}",
                )
                return
            if saved.id is None:
                return

            self.operations_by_id[int(str(saved.id))] = saved
            self._append_operation_to_table(saved)
            current_row = self.table.rowCount() - 1
            self.update_running_balance(current_row, saved)

    def update_running_balance(self, current_row: int, operation: Operation):
        prev_row = current_row - 1 # penultima fila o fila anterior
        balance_col = 8 # columna del saldo o balance

        # Obtener valor de la fila anterior del balance
        prev_item = self.table.item(prev_row, balance_col)
        prev_balance = _safe_decimal(prev_item.text() if prev_item else "0")

        delta = 0.00
        if operation.operation in ("COMPRA", "COSTO"):
            delta = float(str(operation.quantity))
        elif operation.operation == "VENTA":
            delta = -float(str(operation.quantity))

        new_balance = prev_balance + delta

        current_item = self.table.item(current_row, balance_col)
        if current_item:
            current_item.setText(f"{new_balance:.4f}")

    def on_edit_clicked(self):
        button = self.sender()
        if not isinstance(button, QPushButton):
            return

        op_id = button.property("operation_id")
        if op_id is None:
            return

        op_id = int(op_id)
        operation = self.operations_by_id.get(op_id)
        if operation is None:
            QMessageBox.warning(self, "No encontrado", "La operación no existe en memoria.")
            return

        # Abrimos el diálogo en modo edición
        dialog = FinancialFormDialog(self, operation=operation)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        # Aplicamos cambios sobre la instancia y guardamos en BD
        dialog.apply_to_operation(operation)

        try:
            updated = self.operation_repo.save(dto_to_entity(operation))
        except Exception as exc:
            QMessageBox.critical(self, "Error", f"Error al actualizar operación:\n{exc}")
            return

        self.operations_by_id[op_id] = operation

        # Actualizamos solo la fila correspondiente
        row = self._find_row_for_button(button)
        if row >= 0:
            self._update_operation_row(row, updated)
            self.update_running_balance(row, updated)

    def on_delete_clicked(self):
        """
        Handle delete button click: remove from DB and from table.
        """
        button = self.sender()
        if not isinstance(button, QPushButton):
            return
        op_id = button.property("operation_id")
        if op_id is None:
            return

        reply = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Desea eliminar esta operación?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        # Borrar en BD
        try:
            deleted = self.operation_repo.delete(int(op_id))
        except Exception as exc:
            QMessageBox.critical(
                self,
                "Error",
                f"Error al eliminar la operación en la base de datos:\n{exc}",
            )
            return

        if not deleted:
            QMessageBox.warning(
                self,
                "No encontrado",
                "La operación ya no existe en la base de datos.",
            )
            # Igualmente podríamos refrescar la tabla:
            # self.load_operations()
            return

        # Buscar la fila que contiene este botón
        # Quitamos de la tabla sin recargar todo
        row = self._find_row_for_button(button)
        if row >= 0:
            self.table.removeRow(row)

        # Quitamos del diccionario
        self.operations_by_id.pop(op_id, None)

    def export_to_csv(self):
        """
        Export current table data (excluding Actions column) to a CSV file.
        """
        if self.table.rowCount() == 0:
            QMessageBox.information(self, "Exportar CSV", "No hay datos para exportar.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar como CSV",
            "operaciones.csv",
            "CSV Files (*.csv);;All Files (*)",
        )

        if not file_path:
            return

        # Asegurar extensión
        if not file_path.lower().endswith(".csv"):
            file_path += ".csv"

        try:
            with open(file_path, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=";")

                # Headers (excluimos columna Acciones)
                headers = []
                for col in range(self.table.columnCount()):
                    if col == self._action_col_index:
                        continue
                    header_item = self.table.horizontalHeaderItem(col)
                    headers.append(header_item.text() if header_item else f"Columna {col}")
                writer.writerow(headers)

                # Rows
                for row in range(self.table.rowCount()):
                    row_data = []
                    for col in range(self.table.columnCount()):
                        if col == self._action_col_index:
                            continue
                        item = self.table.item(row, col)
                        row_data.append(item.text() if item is not None else "")
                    writer.writerow(row_data)

            QMessageBox.information(self, "Exportar CSV", f"Datos exportados correctamente a:\n{file_path}")
        except Exception as exc:
            QMessageBox.critical(self, "Error", f"Error al exportar CSV:\n{exc}")

    def export_to_excel(self):
        """
        Export current table data (excluding Actions column) to an Excel (.xlsx) file.
        """
        if self.table.rowCount() == 0:
            QMessageBox.information(self, "Exportar Excel", "No hay datos para exportar.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar como Excel",
            "operaciones.xlsx",
            "Excel Files (*.xlsx);;All Files (*)",
        )

        if not file_path:
            return

        if not file_path.lower().endswith(".xlsx"):
            file_path += ".xlsx"

        try:
            # Headers
            headers = []
            col_indexes = []
            for col in range(self.table.columnCount()):
                if col == self._action_col_index:
                    continue
                col_indexes.append(col)
                header_item = self.table.horizontalHeaderItem(col)
                headers.append(header_item.text() if header_item else f"Columna {col}")

            # Data rows
            rows = []
            for row in range(self.table.rowCount()):
                row_data = []
                for col in col_indexes:
                    item = self.table.item(row, col)
                    row_data.append(item.text() if item is not None else "")
                rows.append(row_data)

            df = pd.DataFrame(rows, columns=headers)
            df.to_excel(file_path, index=False)

            QMessageBox.information(self, "Exportar Excel", f"Datos exportados correctamente a:\n{file_path}")
        except Exception as exc:
            QMessageBox.critical(self, "Error", f"Error al exportar Excel:\n{exc}")

    def export_to_pdf(self):
        """
        Export current table data (excluding Actions column) to a PDF file
        with a simple table layout.
        """
        if self.table.rowCount() == 0:
            QMessageBox.information(self, "Exportar PDF", "No hay datos para exportar.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar como PDF",
            "operaciones.pdf",
            "PDF Files (*.pdf);;All Files (*)",
        )

        if not file_path:
            return

        if not file_path.lower().endswith(".pdf"):
            file_path += ".pdf"

        try:
            # --- Recoger headers y datos desde la tabla ---
            headers = []
            col_indexes = []
            for col in range(self.table.columnCount()):
                if col == self._action_col_index:
                    continue
                col_indexes.append(col)
                header_item = self.table.horizontalHeaderItem(col)
                headers.append(header_item.text() if header_item else f"Columna {col}")

            data = [headers]

            for row in range(self.table.rowCount()):
                row_data = []
                for col in col_indexes:
                    item = self.table.item(row, col)
                    row_data.append(item.text() if item is not None else "")
                data.append(row_data)

            # --- Construir PDF con reportlab ---
            doc = SimpleDocTemplate(
                file_path,
                pagesize=landscape(A4),
                leftMargin=20,
                rightMargin=20,
                topMargin=30,
                bottomMargin=30,
            )

            elements = []
            styles = getSampleStyleSheet()

            title = Paragraph("Operaciones financieras", styles["Heading1"])
            elements.append(title)
            elements.append(Spacer(1, 12))

            table = Table(data, repeatRows=1)

            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTSIZE", (0, 0), (-1, 0), 10),
                        ("FONTSIZE", (0, 1), (-1, -1), 9),
                        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightyellow]),
                    ]
                )
            )

            elements.append(table)

            doc.build(elements)

            QMessageBox.information(self, "Exportar PDF", f"Datos exportados correctamente a:\n{file_path}")

        except Exception as exc:
            QMessageBox.critical(self, "Error", f"Error al exportar PDF:\n{exc}")