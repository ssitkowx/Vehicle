import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PySide6.QtGui import QKeyEvent

#class KeyboardEventApp(QMainWindow):
class Keyboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keyboard Event Example")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.key_label = QLabel("Last Key Pressed: None", self.central_widget)
        self.key_label.setGeometry(10, 10, 200, 30)

    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            key_num = event.key ()
            self.key_label.setText(f"Last Key Pressed: {key_num}")

    def keyReleaseEvent(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            key_num = event.key ()
            self.key_label.setText(f"Key Released: {key_num}")

#def main():
#    app = QApplication(sys.argv)
#    window = KeyboardEventApp()
#    window.show()
#    sys.exit(app.exec_())

#if __name__ == "__main__":
#    main()
