import argparse
import sys
from mbti.test import run_test
from mbti.results import save_results
from mbti.i18n.core import translator

SUPPORTED_LANGUAGES = {
    'zh': '简体中文',
    'en': 'English (US)',
    # 可扩展其他语言
}

def main():
    parser = argparse.ArgumentParser(description='MBTI Personality Test Command Line Program')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
    parser.add_argument('--short', action='store_true', help='Run the 28-question version')
    parser.add_argument('--long', action='store_true', help='Run the 93-question version')
    parser.add_argument('--save', action='store_true', help='Save results to a CSV file')
    parser.add_argument('--lang', choices=SUPPORTED_LANGUAGES.keys(), default='zh', help=f"Available languages: {', '.join(SUPPORTED_LANGUAGES.values())}")

    args = parser.parse_args()

    # Determine which test to run
    if args.short and args.long:
        print("Error: Cannot specify both --short and --long")
        return
    elif args.short:
        test_version = 'quick'
    elif args.long:
        test_version = 'standard'
    else:
        # Default to short if neither is specified
        test_version = 'quick'

    try:
        translator.set_language(args.lang)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Run the test
    results = run_test(test_version, args.lang)

    # Save results if requested
    if args.save and results:
        save_results(results, args.lang)

if __name__ == "__main__":
    main()