import argparse
import sys
from mbti.questions import load_question_registry, validate_question_count
from mbti.test import run_test
from mbti.results import save_results
from mbti.i18n.core import translator

SUPPORTED_LANGUAGES = {
    'zh': '简体中文',
    'en': 'English (US)',
    # 可扩展其他语言
}

def main():
    # 获取可用测试列表
    try:
        available_tests = load_question_registry()
        available_counts = [str(test['question_count']) for test in available_tests]
    except RuntimeError as e:
        available_counts = []
        print(f"Warning: {str(e)}")
    
    if len(sys.argv) == 1:
        sys.argv.append("--help")

    # parser = argparse.ArgumentParser(description='MBTI Personality Test Command Line Program')
    parser = argparse.ArgumentParser(
        description='MBTI Personality Test Command Line Program',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-q', '--questions',
                        type=int,
                        required=True,
                        choices=[test['question_count'] for test in available_tests],
                        metavar='N',
                        help='\n'.join(
                            [f"{test['question_count']} questions: {test['description']['en']}"
                             for test in available_tests]
                        ))
    parser.add_argument('--lang', 
                        choices=SUPPORTED_LANGUAGES.keys(), 
                        default='zh', 
                        help=f"Available languages: {', '.join(SUPPORTED_LANGUAGES.values())}")
    parser.add_argument('--save', action='store_true', help='Save results to a CSV file')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

    args = parser.parse_args()

    try:
        translator.set_language(args.lang)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Run the test
    try:
        results = run_test(args.questions, args.lang)
    except ValueError as e:
        print(f"Error: {str(e)}")
        return

    # Save results if requested
    if args.save and results:
        save_results(results, args.lang)

if __name__ == "__main__":
    main()