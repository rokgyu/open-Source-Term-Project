from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GPT2Tokenizer, GPT2LMHeadModel

# Seq2Seq 및 언어 모델 목록
seq2seq_models = [
    "Helsinki-NLP/opus-mt-ko-en",
    "facebook/m2m100_418M",
    "facebook/nllb-200-distilled-600M"
]
language_models = [
    "gpt2"  # 추가된 GPT-2 모델
]

# Seq2Seq 모델 다운로드 및 저장
for model_name in seq2seq_models:
    print(f"Downloading {model_name} (Seq2Seq model)...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # 로컬 경로에 저장
    save_path = f"./local_models/{model_name.replace('/', '_')}"
    tokenizer.save_pretrained(save_path)
    model.save_pretrained(save_path)
    print(f"Model saved at {save_path}")

# 언어 모델 다운로드 및 저장
for model_name in language_models:
    print(f"Downloading {model_name} (Language model)...")
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # 로컬 경로에 저장
    save_path = f"./local_models/{model_name.replace('/', '_')}"
    tokenizer.save_pretrained(save_path)
    model.save_pretrained(save_path)
    print(f"Model saved at {save_path}")
