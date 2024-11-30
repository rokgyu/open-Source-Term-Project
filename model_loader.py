from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import M2M100Tokenizer, M2M100ForConditionalGeneration

def load_model_1():
    """Helsinki-NLP의 Korean-English 번역 모델을 로드합니다 (로컬에서)."""
    model_name = "./local_models/Helsinki-NLP_opus-mt-ko-en"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

def load_model_2():
    """Facebook의 M2M100 다국어 번역 모델을 로드합니다 (로컬에서)."""
    model_name = "./local_models/facebook_m2m100_418M"
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)
    tokenizer.src_lang = "ko"
    return tokenizer, model

def load_model_3():
    """NLLB 다국어 번역 모델을 로드합니다 (로컬에서)."""
    model_name = "./local_models/facebook_nllb-200-distilled-600M"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model
