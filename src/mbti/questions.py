import json
import os

def load_questions(version='quick', language='zh'):
    # Determine the path to the questions file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, 'data')
    if version == 'quick':
        questions_file = os.path.join(data_dir, 'questions_quick.json')
    else:
        questions_file = os.path.join(data_dir, 'questions_standard.json')

    # Load questions from file
    with open(questions_file, 'r', encoding='utf-8') as f:
        questions_data = json.load(f)

    return questions_data['MBTI_questions']