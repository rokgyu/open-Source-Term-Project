import torch
from model_loader import load_model_1, load_model_2, load_model_3

def translate_korean_to_english(tokenizer, model, korean_text, model_type="default"):
    """
    주어진 모델과 토크나이저를 사용하여 한국어를 영어로 번역합니다.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    
    if model_type == "m2m100":
        inputs = tokenizer(korean_text, return_tensors="pt").to(device)
        generated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.get_lang_id("en"),
            max_length=128
        )
    elif model_type == "nllb":
        tokenizer.src_lang = "kor_Latn"
        inputs = tokenizer(korean_text, return_tensors="pt").to(device)
        generated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids("eng_Latn"),
            max_length=128
        )
    else:
        inputs = tokenizer(korean_text, return_tensors="pt").to(device)
        generated_tokens = model.generate(**inputs, max_length=128)
    
    translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    return translated_text

def get_translations(korean_text):
    # 모델 로드 (로컬 모델 사용)
    tokenizer_1, model_1 = load_model_1()
    tokenizer_2, model_2 = load_model_2()
    tokenizer_3, model_3 = load_model_3()

    # 각 모델로 번역 실행
    translated_text_1 = translate_korean_to_english(tokenizer_1, model_1, korean_text)
    translated_text_2 = translate_korean_to_english(tokenizer_2, model_2, korean_text, "m2m100")
    translated_text_3 = translate_korean_to_english(tokenizer_3, model_3, korean_text, "nllb")

    return translated_text_1, translated_text_2, translated_text_3
