# 커밋 번역기

[ko](docs/README_ko.md) | [jp](docs/README_jp.md)

이 스크립트는 한국어 및 일본어로 작성된 커밋 메시지를 영어로 번역하고, 일반적인 커밋 규칙에 맞게 포맷합니다.

## 기능
- 한국어와 일본어로 작성된 커밋 메시지를 영어로 번역합니다.
- 커밋 타입(feat, fix, chore 등)을 자동으로 결정합니다.
- 커밋하기 전에 확인 프롬프트를 제공합니다.

## 사용 방법
1. Poetry를 설치합니다.
2. 리포지토리를 클론합니다:
```bash
git clone https://github.com/BoYeonJang/commit-translator.git
cd commit-translator
```
3. 가상환경을 설정합니다:
```bash
poetry install
```
4. 스크립트에 OpenAI API 키를 설정합니다.
5. cmtl 명령어를 사용하여 번역하고 커밋합니다:
```bash
cmtl "한국어 또는 일본어로 된 커밋 메시지"
```

## 설치
스크립트를 전역적으로 설치하려면 다음을 사용할 수 있습니다:

```bash
sudo cp translate.py /usr/local/bin/cmtl
```