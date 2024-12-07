import torch
from model_loader import load_model_1, load_model_2, load_model_3, load_model_4, load_model_5

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

def get_translations_ko_to_en(korean_text):
    """
    한국어를 영어로 번역하는 함수.
    """
    tokenizer_1, model_1 = load_model_1()
    tokenizer_2, model_2 = load_model_2()
    tokenizer_3, model_3 = load_model_3()

    translated_text_1 = translate_korean_to_english(tokenizer_1, model_1, korean_text)
    translated_text_2 = translate_korean_to_english(tokenizer_2, model_2, korean_text, "m2m100")
    translated_text_3 = translate_korean_to_english(tokenizer_3, model_3, korean_text, "nllb")

    return translated_text_1, translated_text_2, translated_text_3


def translate_english_to_korean(tokenizer, model, english_text, model_type="default"):
    """
    주어진 모델과 토크나이저를 사용하여 영어를 한국어로 번역합니다.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    
    if model_type == "m2m100":
        inputs = tokenizer(english_text, return_tensors="pt").to(device)
        generated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.get_lang_id("ko"),
            max_length=128
        )
    elif model_type == "nllb":
        tokenizer.src_lang = "eng_Latn"
        inputs = tokenizer(english_text, return_tensors="pt").to(device)
        generated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids("kor_Hang"),
            max_length=128
        )
    else:
        inputs = tokenizer(english_text, return_tensors="pt").to(device)
        generated_tokens = model.generate(**inputs, max_length=128)
    
    translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    return translated_text

def get_translations_en_to_ko(english_text):
    """
    영어를 한국어로 번역하는 함수.
    """
    tokenizer_4, model_4 = load_model_4()
    tokenizer_5, model_5 = load_model_5()
    tokenizer_3, model_3 = load_model_3()

    translated_text_4 = translate_english_to_korean(tokenizer_4, model_4, english_text)
    translated_text_5 = translate_english_to_korean(tokenizer_5, model_5, english_text, "m2m100")
    translated_text_3 = translate_english_to_korean(tokenizer_3, model_3, english_text, "nllb")

    return translated_text_4, translated_text_5, translated_text_3
