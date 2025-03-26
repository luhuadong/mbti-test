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
            's': '实感 (S)',
            'n': '直觉 (N)',
            't': '理智 (T)',
            'f': '情感 (F)',
            'j': '判断 (J)',
            'p': '理解 (P)',
            'tie_warning': '\n[注意] 某些维度得分相同',
            'tie_note': '根据 MBTI 官方规则选择后半部分类型（I/N/F/P）'
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
            'p': 'Perceiving (P)',
            'tie_warning': '\n[Notice] Some dimensions had tied scores',
            'tie_note': 'Applied default selection per MBTI guidelines (I/N/F/P)'
        }
    }

    # 显示基础结果
    print(f"\n{messages[language]['type']}")
    print(f"{messages[language]['overall']}: {results['type']}")
    print(f"\n{messages[language]['scores']}:")
    print(f"{messages[language]['e']} vs {messages[language]['i']}: {results['scores']['E']} - {results['scores']['I']}")
    print(f"{messages[language]['s']} vs {messages[language]['n']}: {results['scores']['S']} - {results['scores']['N']}")
    print(f"{messages[language]['t']} vs {messages[language]['f']}: {results['scores']['T']} - {results['scores']['F']}")
    print(f"{messages[language]['j']} vs {messages[language]['p']}: {results['scores']['J']} - {results['scores']['P']}")

    # 检测并显示平分提示
    tie_detected = any([
        results['scores']['E'] == results['scores']['I'],
        results['scores']['S'] == results['scores']['N'],
        results['scores']['T'] == results['scores']['F'],
        results['scores']['J'] == results['scores']['P']
    ])

    if tie_detected:
        print(f"{messages[language]['tie_warning']}")
        print(f"{messages[language]['tie_note']}")

def save_results(results, language='zh'):
    # 创建结果目录（保持不变）
    current_dir = os.getcwd()
    results_dir = os.path.join(current_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)

    # 生成带时间戳的文件名（保持不变）
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(results_dir, f"mbti_results_{timestamp}.csv")

    # 写入CSV文件（保持不变）
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Dimension', 'Score_E', 'Score_I', 'Score_S', 'Score_N', 
                     'Score_T', 'Score_F', 'Score_J', 'Score_P', 'Type']
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