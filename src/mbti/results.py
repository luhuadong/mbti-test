import csv
import os
from datetime import datetime

def display_results(results, language='zh'):
    messages = {
        'zh': {
            'type': '你的 MBTI 类型结果:',
            'overall': '总体类型',
            'scores': '维度得分',
            'e': '外向 (E)',
            'i': '内向 (I)',
            's': '感知 (S)',
            'n': '直觉 (N)',
            't': '思考 (T)',
            'f': '情感 (F)',
            'j': '判断 (J)',
            'p': '感知 (P)'
        },
        'en': {
            'type': 'Your MBTI Type Results:',
            'overall': 'Overall Type',
            'scores': 'Dimension Scores',
            'e': 'Extraversion (E)',
            'i': 'Introversion (I)',
            's': 'Sensing (S)',
            'n': 'Intuition (N)',
            't': 'Thinking (T)',
            'f': 'Feeling (F)',
            'j': 'Judging (J)',
            'p': 'Perceiving (P)'
        }
    }

    print(f"\n{messages[language]['type']}")
    print(f"{messages[language]['overall']}: {results['type']}")
    print(f"\n{messages[language]['scores']}:")
    print(f"{messages[language]['e']} vs {messages[language]['i']}: {results['scores']['E']} - {results['scores']['I']}")
    print(f"{messages[language]['s']} vs {messages[language]['n']}: {results['scores']['S']} - {results['scores']['N']}")
    print(f"{messages[language]['t']} vs {messages[language]['f']}: {results['scores']['T']} - {results['scores']['F']}")
    print(f"{messages[language]['j']} vs {messages[language]['p']}: {results['scores']['J']} - {results['scores']['P']}")

def save_results(results, language='zh'):
    # Create results directory if it doesn't exist
    current_dir = os.getcwd()
    results_dir = os.path.join(current_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(results_dir, f"mbti_results_{timestamp}.csv")

    # Write results to CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Dimension', 'Score_E', 'Score_I', 'Score_S', 'Score_N', 'Score_T', 'Score_F', 'Score_J', 'Score_P', 'Type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            'Dimension': 'Overall',
            'Score_E': results['scores']['E'],
            'Score_I': results['scores']['I'],
            'Score_S': results['scores']['S'],
            'Score_N': results['scores']['N'],
            'Score_T': results['scores']['T'],
            'Score_F': results['scores']['F'],
            'Score_J': results['scores']['J'],
            'Score_P': results['scores']['P'],
            'Type': results['type']
        })

    print(f"\nResults saved to {filename}")