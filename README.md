# **A105조 주식 자동 매매 웹 서비스**

# 우리 프로젝트의 구조 (임시)
![diagram](/readme/diagram.png)

# 경쟁 어플리케이션 분석
## 로보 어드바이저의 종류
1. 자문형 : 고객 맞춤형 투자자문 제공
    대표회사>디멘젼투자자문, 파운트, 에임
![roboexample2](/readme/roboexample2.png)

2. 일임형 : 자산 배분 후 직접 자산 운용
    대표회사> 밸류시스템자산운용, 아이로보, 쿼터백자산운용
![roboexample](/readme/roboexample.png)

## 우리 프로젝트의 방향
일임형 서비스를 기반으로 시장 위험을 모니터링하여 위험 수준이 높아질 경우 채권 등 안전자산 비중 확대
종목 선정은 알고리즘으로, 추후 웹스크래핑으로 기사 분석 기능 추가.
자문형 기능은 추가 기능으로 넣어 하이브리드형으로 만들 예정

# 증권사 API

# 은행 API
https://www.open-platform.or.kr/apt/content/openapi

# 매매 알고리즘
[링크] (https://lab.ssafy.com/s02-final/s02p31a105/wikis/%5B%EC%9D%B4%EC%9D%80%EA%B7%9C%5D-Zipline%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%B0%B1%ED%85%8C%EC%8A%A4%ED%8C%85-%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98(%EA%B3%A8%EB%93%A0%ED%81%AC%EB%A1%9C%EC%8A%A4/%5B%EC%9D%B4%EC%9D%80%EA%B7%9C%5D-Zipline%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%B0%B1%ED%85%8C%EC%8A%A4%ED%8C%85-%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98(%EA%B3%A8%EB%93%A0%ED%81%AC%EB%A1%9C%EC%8A%A4-%EB%8D%B0%EC%8A%A4%ED%81%AC%EB%A1%9C%EC%8A%A4-%EC%9D%B4%EC%9A%A9))

1. 골든크로스 매수 - 데드크로스 매도 방식
    : 주가 이동평균선을 이용하는 대표적인 기술적 분석 지표
![graph](/readme/graphexample.png)
![cross](/readme/cross.png)

2. zipline을 이용한 알고리즘 백테스팅
    : 과거의 데이터를 바탕으로 테스트하는 것
![back](/readme/back.png)

3. 다른 여러 알고리즘과 딥러닝을 추가적으로 적용할 예정입니다. 

# 깃
![git-flo](/readme/git-flow.png)
master-develop-프론트/백의 3단계 구조
master 브랜치에 Jenkins를 연동하여 CI/CD를 자동화할 예정입니다. 