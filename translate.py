import sys
import os
import yaml
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("API 키가 설정되지 않았습니다. 환경 변수를 확인하세요.")

# API 키를 사용하여 OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)

def load_commit_types(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

commit_types = load_commit_types('commit_types.yaml')

def get_commit_type(message):
    message = message.lower()

    for commit_type, keywords in commit_types.items():
        if any(keyword in message for keyword in keywords):
            return commit_type

    return "chore"  # 기본값

def translate_to_english(message, api_key):
    message = message.replace("생성", "추가")
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Please translate the following message to English: {message}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    input_message = " ".join(sys.argv[1:])
    commit_type = get_commit_type(input_message).lower()
    english_message = translate_to_english(input_message, api_key)
    final_message = f"{commit_type}: {english_message.lower()}"
    print(final_message)