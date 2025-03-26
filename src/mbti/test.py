import os
from mbti.questions import load_questions
from mbti.calculator import calculate_mbti_type
from mbti.results import display_results
from mbti.i18n.core import translator
try:
    from colorama import init, Fore, Style
    init(autoreset=True)  # 自动重置颜色状态
except ImportError:
    pass

# 终端颜色配置（兼容无colorama环境）
COLORS = {
    'title': '\033[1;36m',
    'question': '\033[1;97m',
    'option': '\033[1;92m',
    'progress': '\033[1;34m',
    'error': '\033[1;31m',
    'highlight': '\033[1;33m',
    'reset': '\033[0m'
}

def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_progress(current, total, lang):
    """显示本地化进度条"""
    bar_length = 30
    progress = current / total
    filled = int(bar_length * progress)
    bar = '▓' * filled + '░' * (bar_length - filled)
    
    progress_text = translator.t(
        'test_ui.progress_title',
        bar=bar,
        current=current,
        total=total
    )
    print(f"{COLORS['progress']}{progress_text}{COLORS['reset']}\n")

def get_localized_question(question, lang):
    """生成本地化题目内容"""
    return {
        'text': question['question'][lang],
        'options': question['options'][lang],
        'dimension': question['dimension']
    }

def run_test(question_count, language='zh'):
    """运行测试主流程"""
    global translator
    try:
        translator.set_language(language)
    except ValueError as e:
        print(f"{COLORS['error']}Language Error: {e}{COLORS['reset']}")
        return None
    
    questions = load_questions(question_count, language)
    answers = []
    total_questions = len(questions)

    # 初始化界面
    clear_screen()
    print(f"{COLORS['title']}{translator.t('test_ui.welcome', version=translator.t(f'test_version.{question_count}'))}{COLORS['reset']}")
    print(f"{COLORS['progress']}{translator.t('test_ui.stats', language=translator.t('meta.language'), count=total_questions)}{COLORS['reset']}\n")
    input(f"{COLORS['highlight']}{translator.t('test_ui.press_start')}{COLORS['reset']}")
    clear_screen()

    # 题目循环
    for idx, question in enumerate(questions, 1):
        clear_screen()
        q = get_localized_question(question, language)
        
        # 显示进度
        show_progress(idx, total_questions, language)

        # 显示题目
        print(f"{COLORS['question']}{translator.t('test_ui.current_question', current=idx)}{COLORS['reset']}")
        print(f"{COLORS['question']}﹂ {q['text']}{COLORS['reset']}\n")

        # 显示选项
        options = q['options']
        for i, option in enumerate(options, 1):
            print(f"  {COLORS['option']}{i}. {option}{COLORS['reset']}")
        print()

        # 获取有效输入
        while True:
            try:
                choice = input(
                    f"{COLORS['highlight']}"
                    f"{translator.t('test_ui.option_prompt', options='1/2')}"
                    f"{COLORS['reset']}"
                )
                if choice not in ('1', '2'):
                    raise ValueError
                
                answers.append({
                    'id': question['id'],
                    'dimension': q['dimension'],
                    'answer': choice
                })
                break
            except ValueError:
                print(f"{COLORS['error']}{translator.t('test_ui.invalid_input', options='1/2')}{COLORS['reset']}\n")
            except KeyboardInterrupt:
                print(f"\n{COLORS['error']}⚠ 测试已中断{COLORS['reset']}")
                return None

    # 显示结果
    clear_screen()
    print(f"{COLORS['title']}\n{translator.t('test_ui.complete')}{COLORS['reset']}\n")
    results = calculate_mbti_type(answers)
    display_results(results, language)
    
    return results