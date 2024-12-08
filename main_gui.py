import ipywidgets as widgets
from IPython.display import display, clear_output
from translator import get_translations_ko_to_en, get_translations_en_to_ko
from quality_evaluator import evaluate_quality
import time

# 모델 리스트
models = ['Helsinki-NLP', 'M2M100', 'NLLB']

# 번역 방향 선택 드롭다운
direction_dropdown = widgets.Dropdown(
    options=[('한국어 → 영어', 0), ('영어 → 한국어', 1)],
    value=0,
    description='번역 방향:',
)

# 텍스트 입력 위젯
text_input = widgets.Text(
    description='입력:',
    placeholder='번역할 텍스트를 입력하세요.',
)

# 실행 버튼
translate_button = widgets.Button(
    description='🔄 번역 실행',
    button_style='success',
    tooltip='번역을 시작합니다.',
    icon='language',
)

translate_button.layout = widgets.Layout(
    width='200px',
    height='40px',
    margin='10px 0px',
    border='2px solid #28a745',
    border_radius='10px',
    padding='5px'
)

translate_button.style = {
    'font_weight': 'bold',
    'font_size': '14px',
    'text_transform': 'uppercase',
}

# 출력 위젯
output_area = widgets.Output()

# 버튼 클릭 이벤트 처리
def on_translate_button_click(_):
    with output_area:
        clear_output()  # 이전 출력 내용 지우기
        print("\n번역이 진행 중입니다...\n")
        time.sleep(1)  # 대기 효과

        direction = direction_dropdown.value
        input_text = text_input.value

        if not input_text.strip():
            print("입력 텍스트가 비어 있습니다. 다시 입력하세요.")
            return

        try:
            # 번역 실행
            if direction == 0:  # 한국어 → 영어
                translated_texts = get_translations_ko_to_en(input_text)
            elif direction == 1:  # 영어 → 한국어
                translated_texts = get_translations_en_to_ko(input_text)

            # 품질 평가
            scores = [evaluate_quality(text) for text in translated_texts]

            # 결과 출력
            print("\n=== 번역 결과 및 품질 점수 ===")
            for i, (model, translation, score) in enumerate(zip(models, translated_texts, scores)):
                print(f"{i + 1}. {model}: {translation} (점수: {score})")

            # 최고 품질 문장 선택
            best_index = scores.index(max(scores))
            best_translation = translated_texts[best_index]

            print(f"\n=== 최종 선택된 번역 ===")
            print(f"{models[best_index]}: {best_translation} (점수: {max(scores)})")

        except Exception as e:
            print(f"오류 발생: {e}")

# 버튼 클릭 이벤트 연결
translate_button.on_click(on_translate_button_click)

# 전체 UI 표시
display(widgets.VBox([direction_dropdown, text_input, translate_button, output_area]))
