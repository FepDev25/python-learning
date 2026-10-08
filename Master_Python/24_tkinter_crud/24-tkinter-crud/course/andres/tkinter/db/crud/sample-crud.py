from course.andres.tkinter.db.crud.config.db import SessionLocal
from course.andres.tkinter.db.crud.repositories.user_repository import UserRepository
from course.andres.tkinter.db.crud.ui.user_app import UsersApp
if __name__ == "__main__":
    
    with SessionLocal() as session:
        app = UsersApp(UserRepository(session))
        app.mainloop()
