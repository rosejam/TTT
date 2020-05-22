0518한것
- 깃, 지라 이번주 정리
- 환경설정(가상환경 설정 및 api설치)
- flask공부 마무리

# 윈도우 서버 설정

conda create -n quantroa_382 python=3.8.2 django

## pip install 
flask
psutil
pytz(장고에 포함된 것)
tornado
pandas

aws웹 말고 os내에서 방화벽과 백신프로그램의 방화벽 꺼줘야함!!(우분투꺼도 내부에서 열어주기!)

## 크레온 restapi (flask로 구현됨)
conda activate quantroa_382
cd C:\Users\Administrator\git\quantroa\trading_tutorial\김동주\systrader
(처음 시작 때, set FLASK_app=bridge_flask.py)
flask run --host=0.0.0.0

## 키움 restapi (tornado로 구현됨)
conda activate quantroa_382
cd C:\Users\Administrator\git\quantroa\trading_tutorial\김동주\systrader
(처음 시작 전 root아래 빈 logs폴더 만들어야 서버가 실행되며 서버 로그가 저장된다!)
python restful/kiwoom_restful.py
한 후 뜨는 창 로그인

# 우분투 서버 설정

conda 설치 후 
conda create -n TTT python=3.6.9 django pandas numpy scipy pytz sqlparse scikit-learn joblib
가상환경 (TTT) 생성 및 활성화
conda activate TTT 
pip install djangorestframework 