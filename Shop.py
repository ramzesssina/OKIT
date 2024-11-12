from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit
from PyQt5.QtGui import QIcon
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Оформление заказа")
        self.resize(900, 500)
        self.move(550, 300)
        self.setWindowIcon(QIcon("images.png"))

        self.delivery_text = QtWidgets.QLabel(self)
        self.delivery_btn_text = QtWidgets.QLabel(self)

        self.ShopPay_text = QtWidgets.QLabel(self)

        self.prin = QtWidgets.QLabel(self)

        self.pickup_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Выберите способ получения заказа")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Доставка")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.Delivery)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(300, 150)
        self.btn2.setText("Самовывоз")
        self.btn2.setFixedWidth(200)
        self.btn2.clicked.connect(self.Pickup)

    def Pickup(self):
        self.pickup_text.setText("Выберите способ оплаты")
        self.pickup_text.move(100, 50)
        self.pickup_text.adjustSize()

        self.btn.hide()
        self.btn2.hide()
        self.main_text.hide()

        self.pickup_btn = QtWidgets.QPushButton(self)
        self.pickup_btn.setText("Онлайн!")
        self.pickup_btn.move(70, 150)
        self.pickup_btn.setFixedWidth(200)
        self.pickup_btn.clicked.connect(self.OnlinePay)
        self.pickup_btn.show()

        self.pickup_btn2 = QtWidgets.QPushButton(self)
        self.pickup_btn2.setText("Оплата в магазине")
        self.pickup_btn2.move(300, 150)
        self.pickup_btn2.setFixedWidth(200)
        self.pickup_btn2.clicked.connect(self.ShopPay)
        self.pickup_btn2.show()

    def ShopPay(self):
        self.ShopPay_text.setText("Товар ожидает оплаты\n\n\nоформление заказа завершается")
        self.ShopPay_text.move(100, 50)
        self.ShopPay_text.adjustSize()

        self.btn.hide()
        self.btn2.hide()
        self.main_text.hide()
        self.pickup_text.hide()
        self.pickup_btn2.hide()
        self.pickup_btn.hide()

    def OnlinePay(self):
        self.delivery_text.setText(
            "Оплата онлайн, нужно деняг дать разработчику\n\n\n\nВведите номер карточки и номер на ее обороте")
        self.delivery_text.move(100, 50)
        self.delivery_text.adjustSize()

        self.btn.hide()
        self.btn2.hide()
        self.main_text.hide()
        self.pickup_text.hide()
        self.pickup_btn2.hide()
        self.pickup_btn.hide()

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите номер карты")
        self.input_field.move(100, 150)
        self.input_field.setFixedWidth(140)
        self.input_field.setMaxLength(16)
        self.input_field.show()

        self.input_field2 = QLineEdit(self)
        self.input_field2.setPlaceholderText("Введите номер на обратной стороне карточки")
        self.input_field2.move(320, 150)
        self.input_field2.setFixedWidth(40)
        self.input_field2.setMaxLength(3)
        self.input_field2.show()

        self.delivery_btn = QtWidgets.QPushButton(self)
        self.delivery_btn.setText("Отправить")
        self.delivery_btn.move(130, 200)
        self.delivery_btn.setFixedWidth(200)
        self.delivery_btn.clicked.connect(self.Prinpay)
        self.delivery_btn.show()


    def Delivery(self):
        self.delivery_text.setText("Оплата онлайн, нужно деняг дать разработчику\n\n\n\nВведите номер карточки и номер на ее обороте")
        self.delivery_text.move(100,50)
        self.delivery_text.adjustSize()

        self.btn.hide()
        self.btn2.hide()
        self.main_text.hide()
        self.pickup_text.hide()

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите номер карты")
        self.input_field.move(100, 150)
        self.input_field.setFixedWidth(140)
        self.input_field.setMaxLength(16)
        self.input_field.show()


        self.input_field2 = QLineEdit(self)
        self.input_field2.setPlaceholderText("Введите номер на обратной стороне карточки")
        self.input_field2.move(320, 150)
        self.input_field2.setFixedWidth(40)
        self.input_field2.setMaxLength(3)
        self.input_field2.show()

        self.delivery_btn = QtWidgets.QPushButton(self)
        self.delivery_btn.setText("Отправить")
        self.delivery_btn.move(130, 200)
        self.delivery_btn.setFixedWidth(200)
        self.delivery_btn.clicked.connect(self.Prinpay)
        self.delivery_btn.show()


    def Prinpay(self):
        self.prin.setText("Оплата принята!\n\n\nОформление заказа завершается")
        self.prin.move(100, 50)
        self.prin.adjustSize()

        self.delivery_btn.hide()
        self.input_field.hide()
        self.input_field2.hide()
        self.delivery_text.hide()




def application():
    app = QApplication(sys.argv)
    window = Window()


    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()