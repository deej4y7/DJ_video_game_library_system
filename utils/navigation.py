from PyQt5.QtWidgets import QMainWindow, QWidget, QStackedWidget, QMessageBox
from controllers.user_controller import UserController

class navigation:
    @staticmethod
    def switch_page(stacked_widget: QStackedWidget, page_index: int):
        if stacked_widget and 0 <= page_index < stacked_widget.count():
            stacked_widget.setCurrentIndex(page_index)

    @staticmethod
    def switch_window(curent_window: QMainWindow, target_window: QMainWindow):
        if curent_window:
            curent_window.hide()
        if target_window:
            target_window.show()

    @staticmethod
    def handle_login(username, password, ui_instance):
        # Initialize the UserController
        user_controller = UserController()

        # Call the login method from UserController
        user = user_controller.login_user(username, password)

        if user:
            QMessageBox.information(ui_instance, "Login Successful", "You have successfully logged in!")
            # Add navigation logic here (e.g., navigate to main page)
        else:
            QMessageBox.warning(ui_instance, "Login Failed", "Invalid username or password. Please try again.")

    @staticmethod
    def register_user(first_name, last_name, username, email, password, ui_instance):
        # Initialize the UserController
        user_controller = UserController()

        # Call the register method from UserController
        user_controller.register_user(first_name, last_name, username, email, password)

        QMessageBox.information(ui_instance, "Registration Successful", "You have successfully registered!")
        # Add navigation logic here (e.g., navigate to login page after registration)
