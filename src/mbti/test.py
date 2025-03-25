from mbti.questions import load_questions
from mbti.calculator import calculate_mbti_type
from mbti.results import display_results

def run_test(version='quick', language='zh'):
    questions = load_questions(version, language)
    answers = []

    print(f"\nStarting the MBTI test ({version} version) in {language} language")
    print(f"This test contains {len(questions)} questions.")
    input("Press Enter to start...")

    for question in questions:
        print(f"\nQuestion {question['id']}: {question['question'][language]}")
        print("Options:")
        for i, option in enumerate(question['options'][language]):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                answer = input("Your answer (1 or 2): ")
                if answer in ['1', '2']:
                    answers.append({
                        'id': question['id'],
                        'dimension': question['dimension'],
                        'answer': answer
                    })
                    break
                else:
                    print("Invalid input. Please enter 1 or 2.")
            except KeyboardInterrupt:
                print("\nTest interrupted. Exiting...")
                return None

    results = calculate_mbti_type(answers)
    display_results(results, language)

    return results