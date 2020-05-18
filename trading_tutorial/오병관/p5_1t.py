import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import book.p5_1 as stock

print(stock.author)

print(stock.cal_upper(10000))

