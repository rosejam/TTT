import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from Kiwoom import *

form_class = uic.loadUiType("pytrader.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # PyTrader 최초 실행 시 주문 여부 False
        self.trade_stocks_done = False
        # PyTrader 프로그램이 실행될 때 키움 로그인이 진행되도록 생성자에서 키움 객체를 생성한 후 comm_connect 메서드를 호출
        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()

        # 매수매도 종목 파일 읽기
        self.load_buy_sell_list()

        self.lineEdit.textChanged.connect(self.code_changed)    # lineEdit 객체에 종목코드를 입력


        accounts_num = int(self.kiwoom.get_login_info("ACCOUNT_CNT"))
        accounts = self.kiwoom.get_login_info("ACCNO")
        accounts_list = accounts.split(';')[0:accounts_num]
        self.comboBox.addItems(accounts_list)       # 계좌를 combobox에 출력
        self.pushButton.clicked.connect(self.send_order)        # 현금주문 클릭 시 send_order 실행
        self.pushButton_2.clicked.connect(self.check_balance)   # 보유종목 현황 클릭 check_balance 실행

        # Timer1
        self.timer = QTimer(self)
        self.timer.start(1000)      # 1초마다 주기적으로 timeout 시그널 발생
        self.timer.timeout.connect(self.timeout)    # timeout 시그널 처리할 슬롯으로 self.timeout 설정

        # Timer2
        # [실시간 조회] 체크박스를 체크하면 10초에 한 번씩 데이터가 자동으로 갱신
        # 다른 TR의 요청이 많은 경우에는 주의(TR 요청 초과 될수도 있으므로)
        self.timer2 = QTimer(self)
        self.timer2.start(1000 * 10)
        self.timer2.timeout.connect(self.timeout2)

    def timeout(self):
        market_start_time = QTime(9, 0, 0)
        current_time = QTime.currentTime()

        if current_time > market_start_time and self.trade_stocks_done is False:
            self.trade_stocks()
            self.trade_stocks_done = True

        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간: " + text_time

        state = self.kiwoom.get_connect_state()
        if state == 1:
            state_msg = "서버 연결 중"
        else:
            state_msg = "서버 미 연결 중"

        self.statusbar.showMessage(state_msg + " | " + time_msg)

    def timeout2(self):
        if self.checkBox.isChecked():
            self.check_balance()

    def code_changed(self):
        code = self.lineEdit.text()
        name = self.kiwoom.get_master_code_name(code)
        self.lineEdit_2.setText(name)

    def send_order(self):
        # 각 값에 해당하는 정수값으로 변환하여 키움증권 APi에 전달
        order_type_lookup = {'신규매수': 1, '신규매도': 2, '매수취소': 3, '매도취소': 4}
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        account = self.comboBox.currentText()
        order_type = self.comboBox_2.currentText()
        code = self.lineEdit.text()
        hoga = self.comboBox_3.currentText()
        num = self.spinBox.value()
        price = self.spinBox_2.value()

        self.kiwoom.send_order("send_order_req", "0101", account, order_type_lookup[order_type], code, num, price,
                               hoga_lookup[hoga], "")

    def check_balance(self):
        self.kiwoom.reset_opw00018_output()
        account_number = self.kiwoom.get_login_info("ACCNO")
        account_number = account_number.split(';')[0]

        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")

        # opw00018 TR은 최대 20개의 보유 종목에 대한 데이터를 리턴
        # 보유 종목이 20개 이상인 경우를 고려해서 반복문을 통해 연속적으로 데이터를 요청
        while self.kiwoom.remained_data:
            time.sleep(0.2)
            self.kiwoom.set_input_value("계좌번호", account_number)
            self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 2, "2000")

        # opw00001: 예수금 데이터
        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00001_req", "opw00001", 0, "2000")

        # balance
        # 예수금 데이터를 QTableWidget에 출력하기 위해 먼저 self.kiwoom.d2_deposit에 저장된 예수금 데이터를 QTableWidgetItem 객체로 만듦
        item = QTableWidgetItem(self.kiwoom.d2_deposit)
        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tableWidget.setItem(0, 0, item)

        for i in range(1, 6):
            item = QTableWidgetItem(self.kiwoom.opw00018_output['single'][i - 1])
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            self.tableWidget.setItem(0, i, item)

        # 아이템의 크기에 맞춰 행의 높이를 조절
        self.tableWidget.resizeRowsToContents()

        # Item list
        # 보유 종목별 평가 잔고 데이터를 QTableWidget에 추가
        item_count = len(self.kiwoom.opw00018_output['multi'])
        self.tableWidget_2.setRowCount(item_count)
        for j in range(item_count):
            row = self.kiwoom.opw00018_output['multi'][j]
            for i in range(len(row)):
                item = QTableWidgetItem(row[i])
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.tableWidget_2.setItem(j, i, item)

        self.tableWidget_2.resizeRowsToContents()

    def load_buy_sell_list(self):
        f = open("buy_list.txt", 'rt')
        buy_list = f.readlines()
        f.close()

        f = open("sell_list.txt", 'rt')
        sell_list = f.readlines()
        f.close()

        # 매수/매도 종목 각각에 대한 데이터 개수를 확인한 후 이 두 값을 더한 값을 QTableWidet 객체의 setRowCount 메서드로 설정
        row_count = len(buy_list) + len(sell_list)
        self.tableWidget_4.setRowCount(row_count)

        # buy list(매수 종목)
        for j in range(len(buy_list)):
            row_data = buy_list[j]
            split_row_data = row_data.split(';')
            split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rsplit())    # 종목코드를 종목명으로 변경

            for i in range(len(split_row_data)):
                item = QTableWidgetItem(split_row_data[i].rstrip())
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.tableWidget_4.setItem(j, i, item)

        # sell list(매도 종목)
        for j in range(len(sell_list)):
            row_data = sell_list[j]
            split_row_data = row_data.split(';')
            split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rstrip())

            for i in range(len(split_row_data)):
                item = QTableWidgetItem(split_row_data[i].rstrip())
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                self.tableWidget_4.setItem(len(buy_list) + j, i, item)

        self.tableWidget_4.resizeRowsToContents()   # 행 크기 조절

    def trade_stocks(self):
        """
        trade_stocks(): 각 거래일의 장 시작에 맞춰 정해진 주문 방식에 따라 주문을 수행
        """
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        # 미리 생성된 파일로부터 매수/매도 종목을 읽음
        f = open("buy_list.txt", 'rt')
        buy_list = f.readlines()
        f.close()

        f = open("sell_list.txt", 'rt')
        sell_list = f.readlines()
        f.close()

        # account: 주문할 때 필요한 계좌 정보를 QComboBox 위젯으로부터 얻어옴
        account = self.comboBox.currentText()

        # buy list
        for row_data in buy_list:
            split_row_data = row_data.split(';')
            hoga = split_row_data[2]    # 호가
            code = split_row_data[1]    # 종목코드
            num = split_row_data[3]     # 수량
            price = split_row_data[4]   # 가격

            # 읽어온 데이터의 주문 수행 여부가 ‘매수전’인 경우에만 해당 주문 데이터를 토대로 send_order 메서드를 통해 매수 주문을 수행
            if split_row_data[-1].rstrip() == '매수전':
                self.kiwoom.send_order("send_order_req", "0101", account, 1, code, num, price,
                                       hoga_lookup[hoga], "")

        # sell list
        for row_data in sell_list:
            split_row_data = row_data.split(';')
            hoga = split_row_data[2]
            code = split_row_data[1]
            num = split_row_data[3]
            price = split_row_data[4]

            if split_row_data[-1].rstrip() == '매도전':
                self.kiwoom.send_order("send_order_req", "0101", account, 2, code, num, price,
                                       hoga_lookup[hoga], "")

        # buy list
        for i, row_data in enumerate(buy_list):
            buy_list[i] = buy_list[i].replace("매수전", "주문완료")

        # file update
        f = open("buy_list.txt", 'wt')
        for row_data in buy_list:
            f.write(row_data)
        f.close()

        # sell list
        for i, row_data in enumerate(sell_list):
            sell_list[i] = sell_list[i].replace("매도전", "주문완료")

        # file update
        f = open("sell_list.txt", 'wt')
        for row_data in sell_list:
            f.write(row_data)
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()