from mbti.questions import load_questions
from mbti.calculator import calculate_mbti_type
from mbti.results import display_results
import os

# ANSI 颜色代码
COLORS = {
    'reset': '\033[0m',
    'title': '\033[1;36m',     # 青色加粗
    'question': '\033[1;97m',  # 白色加粗
    'option': '\033[1;92m',    # 绿色加粗
    'progress': '\033[1;34m',  # 蓝色加粗
    'error': '\033[1;31m',     # 红色加粗
    'highlight': '\033[1;33m'  # 黄色加粗
}

def clear_screen():
    """清屏函数，兼容不同操作系统"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_progress(current, total):
    """显示进度条"""
    bar_length = 30
    progress = current / total
    filled = int(bar_length * progress)
    bar = '▓' * filled + '░' * (bar_length - filled)
    print(f"{COLORS['progress']}┌{'─' * 32}┐")
    print(f"│ 进度: {bar} {current}/{total} │")
    print(f"└{'─' * 32}┘{COLORS['reset']}\n")

def run_test(version='quick', language='zh'):
    questions = load_questions(version, language)
    answers = []
    total_questions = len(questions)
    
    clear_screen()
    print(f"{COLORS['title']}🎮 MBTI 性格测试 ({'快速' if version == 'quick' else '标准'}版){COLORS['reset']}")
    print(f"{COLORS['progress']}▶ 语言: {language.upper()}")
    print(f"▶ 题目数量: {total_questions}{COLORS['reset']}\n")
    input(f"{COLORS['highlight']}按 Enter 键开始测试...{COLORS['reset']}")
    clear_screen()

    for idx, question in enumerate(questions, 1):
        # 显示进度
        show_progress(idx, total_questions)

        # 显示题目
        print(f"{COLORS['question']}第 {idx} 题{COLORS['reset']}")
        print(f"{COLORS['question']}﹂ {question['question'][language]}{COLORS['reset']}\n")
        
        # 显示选项
        for i, option in enumerate(question['options'][language], 1):
            print(f"  {COLORS['option']}{i}. {option}{COLORS['reset']}")
        print()

        # 获取有效输入
        while True:
            answer = input(f"{COLORS['highlight']}请输入选项 (1/2): {COLORS['reset']}")
            if answer in ('1', '2'):
                answers.append({
                    'id': question['id'],
                    'dimension': question['dimension'],
                    'answer': answer
                })
                clear_screen()  # 清屏准备下一题
                break
            else:
                print(f"{COLORS['error']}⚠ 无效输入，请选择 1 或 2{COLORS['reset']}\n")

    # 显示最终结果
    clear_screen()
    print(f"{COLORS['title']}\n✨ 测试完成！正在生成结果...{COLORS['reset']}\n")
    results = calculate_mbti_type(answers)
    display_results(results, language)
    
    return results