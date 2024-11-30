from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

def evaluate_quality(sentence):
    """
    문장의 품질(유창성)을 점수화합니다.
    :param sentence: 평가할 문장 (str)
    :return: 품질 점수 (0~100)
    """
    # 모델과 토크나이저 로드 (로컬에서)
    model_name = "./local_models/gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # 문장을 토큰화 및 입력 데이터 변환
    inputs = tokenizer(sentence, return_tensors="pt")
    
    # 모델의 로그 확률 계산
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss  # 평균 로그 손실 (문장의 유창성을 반영)
    
    # 점수를 0~100 범위로 변환 (작을수록 좋은 문장)
    score = max(0, 100 - (loss.item() * 10))
    return round(score, 2)
