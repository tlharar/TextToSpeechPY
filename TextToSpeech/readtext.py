import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QColor

class TextPlayerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Ana pencereyi siyah renkte ayarla
        self.setStyleSheet("background-color: black; color: white;")

        # QTextEdit (yazı yazma kutusu) oluştur
        self.text_edit = QTextEdit()

        # QPushButton (oynat butonu) oluştur ve kırmızı renkte ayarla
        play_button = QPushButton('Oynat')
        play_button.setStyleSheet("background-color: red; color: white;")
        play_button.clicked.connect(self.play_button_clicked)

        # Layout oluştur
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(play_button)

        # Widget'ı ayarla
        self.setLayout(layout)

        # Pencere başlığını belirle
        self.setWindowTitle('Text Player App')

    def play_button_clicked(self):
        # Yazı yazma kutusundaki metni al
        text_to_play = self.text_edit.toPlainText()

        # Mesaj kutusu oluştur ve metni göster
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Oynatılan Metin')
        msg_box.setText(text_to_play)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextPlayerApp()
    window.show()
    sys.exit(app.exec_())
