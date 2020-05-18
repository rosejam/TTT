import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Kiwoom Login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        # OpenAPI+ Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)

        self.setWindowTitle("계좌 정보")
        self.setGeometry(300, 300, 300, 150)

        btn1 = QPushButton("계좌 얻기", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)

    def btn1_clicked(self):
        '''
        GetLoginInfo(Tag): 로그인한 사용자 정보 반환
            Tag: 사용자 정보 구분 TAG값(
                "ACCOUNT_CNT": 전체 계좌 개수 반환
                "ACCNO": 전체 계좌 반환(;로 구분)
                "USER_ID": 사용자 ID 반환
                "USER_NAME": 사용자명 반환
                "KEY_BSECGB": 키보드보안 해지여부(0:정상 1:해지)
                "FIREW_SECGB": 방화벽 설정 여부(0:미설정 1:설정 2:해지)
            )
        '''
        account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])   ### 반드시 리스트[]의 형태로 전달
        self.text_edit.append("계좌번호: " + account_num.rstrip(';'))

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()