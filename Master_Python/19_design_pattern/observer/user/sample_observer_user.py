# --- Código Cliente ---
from course.andres.designpattern.observer.user.admin_notification_observer import AdminNotificationObserver
from course.andres.designpattern.observer.user.log_record_observer import LogRecordObserver
from course.andres.designpattern.observer.user.user_repository import UserRepository, User
from course.andres.designpattern.observer.user.welcome_email_observer import WelcomeEmailObserver

if __name__ == "__main__":
    # 1. Crear el repositorio (sujeto)
    user_repository = UserRepository()

    # 2. Crear los observadores
    welcome_email_sender = WelcomeEmailObserver()
    admin_notifier = AdminNotificationObserver()
    log_recorder = LogRecordObserver()

    # 3. Suscribir los observadores al repositorio
    user_repository.attach(welcome_email_sender)
    user_repository.attach(admin_notifier)
    user_repository.attach(log_recorder)

    # 4. Ejecutar la acción que dispara la notificación
    user_data: dict = {'name': "Juan Perez", 'email': "juan.perez@example.com"}
    user_repository.create_user(user_data)

    user: User = User('Maria Garcia', 'maria.garcia@example.com')
    # 5. Crear otro usuario para demostrar que el patrón sigue funcionando
    user_repository.create_user(user)