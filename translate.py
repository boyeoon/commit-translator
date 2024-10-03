import sys
import os
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

def get_commit_type(message):
    message = message.lower()
    
    if "추가" in message or "追加" in message:
        return "feat"
    elif "수정" in message or "修正" in message:
        return "fix"
    elif "빌드" in message or "ビルド" in message:
        return "build"
    elif "자잘한" in message or "雑多な" in message:
        return "chore"
    elif "ci" in message:
        return "ci"
    elif "문서" in message or "ドキュメント" in message:
        return "docs"
    elif "스타일" in message or "スタイル" in message:
        return "style"
    elif "리팩토링" in message or "リファクタリング" in message:
        return "refactor"
    elif "테스트" in message or "テスト" in message:
        return "test"
    elif "성능" in message or "パフォーマンス" in message:
        return "perf"
    return "chore"

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