from datetime import date

from PySide6.QtWidgets import (
    QVBoxLayout, QDialog, QFormLayout, QLineEdit, QComboBox,
    QDateEdit, QDoubleSpinBox, QDialogButtonBox, QMessageBox
)
from PySide6.QtCore import QDate, Qt

from course.andres.pyside.kardex.app.entity.operation import Operation
from course.andres.pyside.kardex.app.models.dto.operation_with_balance import OperationWithBalance


class FinancialFormDialog(QDialog):
    """
    Modal con QFormLayout. Devuelve un dict con los datos si se acepta.
    """
    def __init__(self, parent=None, operation: OperationWithBalance | None = None):
        super().__init__(parent)
        self.setWindowTitle("Registrar operación")
        self.setModal(True)
        self._operation = operation

        # Inputs
        self.company_input = QLineEdit()
        self.account_number_input = QLineEdit()
        self.issuer_input = QLineEdit()

        self.operation_input = QComboBox()
        self.operation_input.addItems(["COMPRA", "VENTA", "COSTO"])

        self.movement_date_input = QDateEdit()
        self.movement_date_input.setCalendarPopup(True)
        self.movement_date_input.setDate(QDate.currentDate())

        self.instrument_input = QLineEdit()

        self.quantity_input = QDoubleSpinBox()
        self.quantity_input.setDecimals(4)
        self.quantity_input.setMaximum(1_000_000_000)

        self.price_input = QDoubleSpinBox()
        self.price_input.setDecimals(6)
        self.price_input.setMaximum(1_000_000_000)

        # Si viene una operación, pre-rellenamos
        if self._operation is not None:
            self._fill_from_operation(self._operation)

        # Form layout (textos en español)
        form = QFormLayout()
        form.addRow("Compañía:", self.company_input)
        form.addRow("Número de cuenta:", self.account_number_input)
        form.addRow("Emisor:", self.issuer_input)
        form.addRow("Operación:", self.operation_input)
        form.addRow("Fecha de movimiento:", self.movement_date_input)
        form.addRow("Instrumento:", self.instrument_input)
        form.addRow("Cantidad:", self.quantity_input)
        form.addRow("Precio:", self.price_input)

        # Botones OK/Cancel
        buttons = QDialogButtonBox()
        save_btn = buttons.addButton(QDialogButtonBox.StandardButton.Save)
        save_btn.setText("Guardar")
        cancel_btn = buttons.addButton(QDialogButtonBox.StandardButton.Cancel)
        cancel_btn.setText("Cancelar")
        # buttons.accepted.connect(self.accept)
        buttons.accepted.connect(self._on_accept)
        buttons.rejected.connect(self.reject)

        # Layout principal del diálogo
        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def _on_accept(self):
        if not self.validate_form():
            return  # No cerrar el diálogo

        self.accept()  # Cerrar solo si está todo válido

    def _fill_from_operation(self, operation: OperationWithBalance):
        self.company_input.setText(operation.company or "")
        self.account_number_input.setText(operation.account_number or "")
        self.issuer_input.setText(operation.issuer or "")

        idx = self.operation_input.findText(operation.operation or "", Qt.MatchExactly)
        if idx >= 0:
            self.operation_input.setCurrentIndex(idx)

        if operation.movement_date:
            qd = QDate(operation.movement_date.year, operation.movement_date.month, operation.movement_date.day)
            self.movement_date_input.setDate(qd)

        self.instrument_input.setText(operation.instrument or "")
        self.quantity_input.setValue(float(operation.quantity or 0))
        self.price_input.setValue(float(operation.price or 0))

    def apply_to_operation(self, operation: OperationWithBalance):
        """
        Copia los valores del form a la instancia Operation recibida.
        No guarda en BD, eso lo hace el repo.
        """
        qdate: QDate = self.movement_date_input.date()
        movement_date_py = date(qdate.year(), qdate.month(), qdate.day())

        operation.company = self.company_input.text().strip()
        operation.account_number = self.account_number_input.text().strip()
        operation.issuer = self.issuer_input.text().strip()
        operation.operation = self.operation_input.currentText()
        operation.movement_date = movement_date_py
        operation.instrument = self.instrument_input.text().strip()
        operation.quantity = float(self.quantity_input.value())
        operation.price = float(self.price_input.value())

    def get_new_operation_data(self) -> dict:
        """
        Para modo 'crear' (cuando no se pasa Operation).
        """
        qdate: QDate = self.movement_date_input.date()
        movement_date_py = date(qdate.year(), qdate.month(), qdate.day())

        return {
            "company": self.company_input.text().strip(),
            "account_number": self.account_number_input.text().strip(),
            "issuer": self.issuer_input.text().strip(),
            "operation": self.operation_input.currentText(),
            "movement_date": movement_date_py,
            "instrument": self.instrument_input.text().strip(),
            "quantity": float(self.quantity_input.value()),
            "price": float(self.price_input.value()),
        }

    def validate_form(self) -> bool:
        errors = []

        # --- Validaciones de campos requeridos ---
        if not self.company_input.text().strip():
            errors.append("El campo 'Compañía' es obligatorio.")

        if not self.account_number_input.text().strip():
            errors.append("El campo 'Número de cuenta' es obligatorio.")

        if not self.issuer_input.text().strip():
            errors.append("El campo 'Emisor' es obligatorio.")

        if not self.instrument_input.text().strip():
            errors.append("El campo 'Instrumento' es obligatorio.")

        # --- Operación ---
        if not self.operation_input.currentText().strip():
            errors.append("Debe seleccionar una operación.")

        # --- Fecha ---
        if not self.movement_date_input.date().isValid():
            errors.append("La fecha de movimiento no es válida.")

        # --- Cantidad ---
        qty = self.quantity_input.value()
        if qty <= 0:
            errors.append("La cantidad debe ser numérica y mayor que 0.")

        # --- Precio ---
        price = self.price_input.value()
        if price <= 0:
            errors.append("El precio debe ser numérico y mayor que 0.")

        # --- Resultado final ---
        if errors:
            QMessageBox.warning(
                self,
                "Errores de validación",
                "\n".join(errors)
            )
            return False

        return True