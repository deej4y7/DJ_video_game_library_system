
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.login_screen import Ui_loginregister_mainwindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginregister_mainwindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])  # Use QApplication directly since it's imported
    test_app = App()        # Instantiate the correct class, which is App
    test_app.show()
    app.exec_()


