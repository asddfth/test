import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from GetKospiList import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 키움로그인
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        # OpenApi+ Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        kospi_list = []

        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 500, 500)

        btn1 = QPushButton("종목조회",self)
        btn1.move(80,50)
        btn1.clicked.connect(self.btn1_clicked)

        label = QLabel('종목코드: ',self)
        label.move(20,20)

        self.code_insert = QLineEdit(self)
        self.code_insert.move(80,20)
        self.code_insert.setText("039490")

        self.text_stock_info = QTextEdit(self)
        self.text_stock_info.setGeometry(10,60,280,80)
        self.text_stock_info.move(20,100)


        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.move(20, 400)
        self.text_edit.setEnabled(False)

        '''self.kospi_list_window = QListWidget(self)
        self.kospi_list_window.setGeometry(30,200,280,80)
        kospi_list = GetKospiList(self)
        self.kospi_list_window.addItems(kospi_list)'''

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공!")
    def btn1_clicked(self):
        code = self.code_insert.text()
        self.text_stock_info.append("종목코드: " + code)
        #SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)","종목코드",code)
        #CommRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)","opt10001_req","opt10001", 0, "0101")
    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "",
                                           rqname, 0, "종목명")
            bps = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "",
                                             rqname, 0, "BPS")
            now_price = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "",
                                          rqname, 0, "현재가")

            self.text_stock_info.append("종목명: " + name.strip())
            self.text_stock_info.append("BPS: " + bps.strip())
            self.text_stock_info.append("현재가 " + now_price.strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()