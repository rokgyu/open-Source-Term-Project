from translator import get_translations_ko_to_en, get_translations_en_to_ko
from quality_evaluator import evaluate_quality
import time

models = ['Helsinki-NLP', 'M2M100', 'NLLB']

x = input("한국어에서 영어 번역을 원하시면 0, 영어에서 한국어 번역을 원하시면 1을 입력하세요: ")
x = int(x)

if x == 0:
    if __name__ == "__main__":
        korean_text = input("번역할 한국어 텍스트를 입력하세요: ")

        print("\n번역이 진행 중입니다...\n")  # 번역 진행 메시지 표시
        time.sleep(1)  # 잠시 대기 효과

        # 번역 실행
        translated_text_1, translated_text_2, translated_text_3 = get_translations_ko_to_en(korean_text)

        # 품질 평가 실행
        score_1 = evaluate_quality(translated_text_1)
        score_2 = evaluate_quality(translated_text_2)
        score_3 = evaluate_quality(translated_text_3)

        # 결과 출력
        print("\n=== 번역 결과 및 품질 점수 ===")
        print(f"1. Helsinki-NLP: {translated_text_1} (점수: {score_1})")
        print(f"2. M2M100: {translated_text_2} (점수: {score_2})")
        print(f"3. NLLB: {translated_text_3} (점수: {score_3})")

        # 최고 품질 문장 선택
        scores = [score_1, score_2, score_3]
        best_index = scores.index(max(scores))
        best_translation = [translated_text_1, translated_text_2, translated_text_3][best_index]

        print(f"\n=== 최종 선택된 번역 ===")
        print(f"{models[best_index]}: {best_translation} (점수: {max(scores)})")

elif x == 1:
    if __name__ == "__main__":
        english_text = input("번역할 영어 텍스트를 입력하세요: ")

        print("\nPlease Wait...\n")  # 번역 진행 메시지 표시
        time.sleep(1)  # 잠시 대기 효과

        # 번역 실행
        translated_text_4, translated_text_5, translated_text_3 = get_translations_en_to_ko(english_text)

        # 품질 평가 실행
        score_1 = evaluate_quality(translated_text_4)
        score_2 = evaluate_quality(translated_text_5)
        score_3 = evaluate_quality(translated_text_3)

        # 결과 출력
        print("\n=== 번역 결과 및 품질 점수 ===")
        print(f"1. Helsinki-NLP: {translated_text_4} (점수: {score_1})")
        print(f"2. M2M100: {translated_text_5} (점수: {score_2})")
        print(f"3. NLLB: {translated_text_3} (점수: {score_3})")

        # 최고 품질 문장 선택
        scores = [score_1, score_2, score_3]
        best_index = scores.index(max(scores))
        best_translation = [translated_text_4, translated_text_5, translated_text_3][best_index]

        print(f"\n=== 최종 선택된 번역 ===")
        print(f"{models[best_index]}: {best_translation} (점수: {max(scores)})")
