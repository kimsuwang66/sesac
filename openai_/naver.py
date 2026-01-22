import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

def extract_keyword(user_sentence):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", 
             "content": "사용자의 문장에서 네이버 뉴스 검색에 가장 적합한 핵심 키워드 딱 하나만 뽑아주세요. "},
            {"role": "user", "content": user_sentence}
        ]
    )
    keyword = response.choices[0].message.content.strip()
    print(f"\n[AI가 추출한 검색어: {keyword}]")
    return keyword


def chat_with_streaming(news_text):
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    URL = "https://api.openai.com/v1/chat/completions"
    model = "gpt-4o-mini"
    print(f"뉴스 요약 시작\n")
    print("답변: ", end="")
    client = OpenAI()
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 뉴스 요약 전문가입니다. 100개면 100개 모두 간결하게 요약해 주세요. 뉴스 출처는 링크 말고 한글로 꼭 적어주세요. "},
            {"role": "user", "content": news_text}
            ],
        stream=True
    )

    for chunk in stream:
            # [수정] 최신 라이브러리 형식에 맞춰 content를 추출합니다.
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)

    print("\n\n--- 스트리밍 종료 ---")



def naver_news_search():
    url = "https://openapi.naver.com/v1/search/news.json" #검색어

    headers = {
        "X-Naver-Client-Id" : os.getenv('NAVER_CLIENT_ID'),
    
        "X-Naver-Client-Secret" : os.getenv('NAVER_CLIENT_SECRET')
    }

    # print(os.getenv('NAVER_CLIENT_ID'))
    # print(os.getenv('NAVER_CLIENT_SECRET'))
    search=extract_keyword(input(f"검색하고 싶은 내용을 입력하세요 : "))
    if not search:
        print("검색어가 입력되지 않았습니다.")
        return None
    params = {"query" : search, "display": 50
              }
    response = requests.get(url, headers=headers, params=params)


    if response.status_code == 200:
        data = response.json()  # 텍스트가 아닌 파이썬 딕셔너리로 바로 변환!
        items = data.get('items', [])

        context=""

        for i, item in enumerate(items):
            context += f"뉴스 {i+1} 제목: {item['title']}\n요약: {item['description']}\n 출처: {item['link']}\n"
        print("===================================")
        print(len(items))
        return context

    else:
        print(f"에러 발생: {response.status_code}")

news_context=naver_news_search()
if news_context:
    chat_with_streaming(news_context)