# translator.py

from model_loader import load_model  # model_loader.py에서 load_model 함수 가져오기

def translate_korean_to_english(tokenizer, model, korean_text):
    inputs = tokenizer(korean_text, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

if __name__ == "__main__":
    model_name = "Helsinki-NLP/opus-mt-ko-en"  # 모델 이름 설정
    tokenizer, model = load_model(model_name)  # 모델 로드

    korean_text = input("번역할 한국어 텍스트를 입력하세요: ")  # 사용자 입력 받기

    translated_text = translate_korean_to_english(tokenizer, model, korean_text)  # 번역 수행
    print("번역된 텍스트:", translated_text)  # 번역 결과 출력
