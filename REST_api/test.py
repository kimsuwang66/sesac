
import requests
from pprint import pprint
import os
from dotenv import load_dotenv
import asyncio
import aiohttp


load_dotenv()

debug_mode = os.getenv('DEBUG')
secret_key = os.getenv('SECRET_KEY')
server_port = os.getenv('PORT')
TMDB_API = os.getenv('TMDB_API_KEY')


# 1. 미세먼지(`한국환경공단_에어코리아_대기오염정보`)관련 API를 활용하여 다음 질문에 답하시오.
#     1. `시도별 실시간 측정정보 조회`에서  확인가능한 시도 이름을 전부 작성하시오.
#         1. `서울`인지 `서울특별시`인지 등 parameter를 나열하세요
#           시도 이름(전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종)
#     2. `시도별 실시간 측정정보 조회`의 `서울`의 데이터에 대해, 초 미세먼지 농도가 가장 낮은 `stationName`을 찾으시오.
#         1. `시도별 실시간 측정정보 조회`의 `제주`의 데이터에 대해, 초 미세먼지 농도가 가장 낮은 `stationName`을 찾으시오.
#     3. `시도별 실시간 측정정보 조회`의 `서울`의 데이터를 `stationName`으로 접근하기 쉬운 자료구조로 재구성하시오. 
#     4. `종로구`의 미세먼지 농도, 초미세먼지 농도의 1달치 데이터를 정리하시오.
# http://apis.data.go.kr/B552584/RltmKhaiInfoSvc/getMsrstnKhaiRltmDnsty?stationName=종로구& pageNo=1&numOfRows=100&returnType=xml&serviceKey=서비스키

URL = "https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
# URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth"
# URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc"

params = {
    'serviceKey':"868b777ec81664f1a9298f688feaddd06e3367e21f0c70492adebbcf5d93b5db",
    'returnType' : 'json',
    'sidoName' : '전국'
}

headers = {
}

try:
    response = requests.get(URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    data = data
    pprint(data)

except Exception as e:
    print(e)

