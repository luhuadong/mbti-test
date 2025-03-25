def calculate_mbti_type(answers):
    # Initialize scores for each dimension
    scores = {
        'E': 0,
        'I': 0,
        'S': 0,
        'N': 0,
        'T': 0,
        'F': 0,
        'J': 0,
        'P': 0
    }

    # Score each answer
    for answer in answers:
        dimension = answer['dimension']
        choice = int(answer['answer'])

        # For each dimension, answer 1 or 2 affects the score
        if dimension == 'EI':
            if choice == 1:
                scores['E'] += 1
            else:
                scores['I'] += 1
        elif dimension == 'SN':
            if choice == 1:
                scores['S'] += 1
            else:
                scores['N'] += 1
        elif dimension == 'TF':
            if choice == 1:
                scores['T'] += 1
            else:
                scores['F'] += 1
        elif dimension == 'JP':
            if choice == 1:
                scores['J'] += 1
            else:
                scores['P'] += 1

    # Determine the dominant type for each dimension
    # 处理规则：
    # - 当某维度得分相同时，按照 MBTI 官方建议选择后半部分类型 (I/N/F/P)
    # - 此规则基于 Myers-Briggs 基金会建议：https://www.myersbriggs.org/
    mbti_type = ''
    mbti_type += 'E' if scores['E'] > scores['I'] else 'I'  # EI 平分选 I
    mbti_type += 'S' if scores['S'] > scores['N'] else 'N'  # SN 平分选 N
    mbti_type += 'T' if scores['T'] > scores['F'] else 'F'  # TF 平分选 F
    mbti_type += 'J' if scores['J'] > scores['P'] else 'P'  # JP 平分选 P

    return {
        'scores': scores,
        'type': mbti_type
    }