import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        # self.변수명을 사용하는 이유는 클래스의 다른 메서드에서도 해당 변수를 사용해 객체에 접근하기 위해서
        # 특정 객체가 다른 메서드에서는 사용될 필요가 없다면 self를 붙이지 않아도 됨
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)     # QTextEdit 클래스의 크기 및 출력 위치를 조절
        self.text_edit.setEnabled(False)                # 읽기/쓰기 모드를 변경

        '''
        void OnEvenctConnect(LONG nErrCode);
        인자로 입력받는 nErrCode의 값이 0이면 로그인 성공, 음수면 로그인 실패
        '''
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        '''
        Open API+는 통신 연결 상태가 바뀔 때 OnEventConnect라는 이벤트가 발생.
        이벤트와 이벤트 처리 메서드만 연결하면 이벤트(OnEventConnect) 발생 시
        자동으로 이벤트 처리 메서드(self.event_connect)가 호출됨
        '''

    def event_connect(self, err_code):              # 이벤트 처리 메소드
        if err_code == 0:
            self.text_edit.append("로그인 성공")     # list.append 와는 다름

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()