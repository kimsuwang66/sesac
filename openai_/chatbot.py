# import requests
from pprint import pprint
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

URL = "https://api.openai.com/v1/chat/completions"
model = "gpt-4o-mini"

# 대화 내역을 저장할 리스트 초기화
history = [
]

def chat_with_memory(user_input):
    # 1. 사용자 질문을 기록에 추가
    history.append({"role": "user", "content": user_input})
    
    # 2. 전체 기록을 API에 전송
    response = client.chat.completions.create(
        model=model,
        messages=history,
   
    )
    
    # 3. 모델의 답변을 기록에 추가 (이것이 맥락 유지의 핵심)
    answer = response.choices[0].delta.content
    history.append({"role": "assistant", "content": answer})
    
    return answer

while True:
    user_input = input("You: ")
    if user_input == "!q":
        pprint(history)
        pprint("대화를 종료합니다.")
        break
    pprint(chat_with_memory(user_input))