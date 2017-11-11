import sys
import time
from os import path
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "IoThings.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.init_ui()
        self.handle_buttons()

    def init_ui(self):
        self.setFixedSize(450, 600)
        self.setWindowTitle('IoThings')
        self.setWindowIcon(QIcon("iot.png"))

    def handle_buttons(self):
        self.connect.clicked.connect(self.handle_connect)
        self.pub.clicked.connect(self.handle_publish)
        self.sub.clicked.connect(self.handle_subscrib)

    def handle_connect(self):
        hostname = str(self.host.text())
        port = int(self.port.text())
        mqtt_client = mqtt.Client(client_id="0", clean_session=True, userdata=None, transport="tcp")
        mqtt_client.connect(hostname, port=port, keepalive=60)

    def handle_publish(self):
        publish_topic = str(self.pubtop.text())
        publish_message = str(self.pubmsg.toPlainText())
        publish.single(publish_topic, publish_message)

    def handle_subscrib(self):
        subscribe_topic = str(self.subtop.text())
        subscribe_message = subscribe.simple(subscribe_topic)
        self.submsg.setPlainText(subscribe_message.payload)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()