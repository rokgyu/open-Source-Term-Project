from model_loader_1 import load_model_1  # 첫 번째 모델 로딩 함수
from model_loader_2 import load_model_2  # 두 번째 모델 로딩 함수
from model_loader_3 import load_model_3  # 세 번째 모델 로딩 함수 

# 번역 함수 정의
def translate_korean_to_english(tokenizer, model, korean_text):
    inputs = tokenizer(korean_text, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

if __name__ == "__main__":

    # 모델로드
    tokenizer_1, model_1 = load_model_1()
    tokenizer_2, model_2 = load_model_2()
    tokenizer_3, model_3 = load_model_3()


    # 사용자 입력 받기
    korean_text = input("번역할 한국어 텍스트를 입력하세요: ")


    # 모델 1로만 번역 실행
    translated_text_1 = translate_korean_to_english(tokenizer_1, model_1, korean_text)
    translated_text_2 = translate_korean_to_english(tokenizer_2, model_2, korean_text)
    translated_text_3 = translate_korean_to_english(tokenizer_3, model_3, korean_text)

    # 번역 결과 출력
    print("\n--- 번역 결과 ---")
    print("모델 1 (Helsinki-NLP/opus-mt-ko-en):", translated_text_1)
    print("모델 2 (facebook/m2m100_418M):", translated_text_2)
    print("모델 3 (t5-small):", translated_text_3)
