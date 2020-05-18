import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

'''
TR(Transaction): 서버로부터 데이터를 주고 받는 행위
KOA Studio를 통해 Open API+의 TR 목록 확인 가능
'''
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Kiwoom Login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        # OpenAPI+ Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)    # OnReceiveTrData 이벤트 발생마다 receive_trdata 호출

        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)    # setGeometry(x,y,w,h): 출력 위치와 크기 동시에 조절

        '''
        클래스	        용도
        QLabel	        간단한 텍스트 출력('종목코드:' 출력)
        QLineEdit	    간단한 사용자 입력 처리
        QPushButton	    버튼 생성 ('조회' 버튼 생성)
        QTextEdit	    메시지 출력 (실행결과 메시지)
        '''

        label = QLabel('종목코드: ', self)
        label.move(20, 20)  # move(x,y): 출력 위치만 조절

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("039490")    # 사용자에게 값을 입력받기 전의 기본값 설정

        btn1 = QPushButton("조회", self)  # QPushButton(버튼에 출력될 텍스트, 버튼의 부모 위젯)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)     # clicked 이벤트 발생시 btn1_clicked 호출

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)    # 사용자가 QTextEdit 위젯을 통해 입력할 수 없고 오직 읽기 모드로만 사용

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

    def btn1_clicked(self):     # btn1 객체의 clicked 이벤트 처리
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)

        # SetInputValue("종목코드", "입력값1"): TR 입력값 설정
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)

        # CommRqData("RQName", "opt10001", "0", "화면번호"): TR을 서버로 송신
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        """
        :param screen_no: 화면번호
        :param rqname: 사용자구분 명 (CommRqData의 RQName과 매핑)
        :param trcode: TR 명 (CommRqData의 TrCode와 매핑)
        :param recordname: Record 명
        :param prev_next: 연속조회 유무
        :param data_len: 1.0.0.1 버전 이후 사용 x
        :param err_code: 1.0.0.1 버전 이후 사용 x
        :param msg1: 1.0.0.1 버전 이후 사용 x
        :param msg2: 1.0.0.1 버전 이후 사용 x
        :return: 반환값 없음
        """

        if rqname == "opt10001_req":    # 어떤 TR 요청에 의해 OnReceiveTrData 이벤트가 발생했는지 확인하기 위해 먼저 사용자 Request 명(rqname)을 확인
            # CommGetData(): 수신 데이터 가져옴
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")

            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량: " + volume.strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()