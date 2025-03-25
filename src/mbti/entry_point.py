import argparse
from mbti.test import run_test
from mbti.results import save_results

def main():
    parser = argparse.ArgumentParser(description='MBTI Personality Test Command Line Program')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
    parser.add_argument('--short', action='store_true', help='Run the 28-question version')
    parser.add_argument('--long', action='store_true', help='Run the 93-question version')
    parser.add_argument('--save', action='store_true', help='Save results to a CSV file')
    parser.add_argument('--language', choices=['zh', 'en'], default='zh', help='Choose language (zh for Chinese, en for English)')

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

    # Run the test
    results = run_test(test_version, args.language)

    # Save results if requested
    if args.save and results:
        save_results(results, args.language)

if __name__ == "__main__":
    main()