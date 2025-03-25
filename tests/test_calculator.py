import pytest
from mbti.calculator import calculate_mbti_type

def test_calculate_mbti_type():
    # 测试计算MBTI类型
    answers = [
        {'id': 1, 'dimension': 'EI', 'answer': '1'},
        {'id': 2, 'dimension': 'TF', 'answer': '1'},
        {'id': 3, 'dimension': 'JP', 'answer': '1'},
        {'id': 4, 'dimension': 'SN', 'answer': '1'},
        {'id': 5, 'dimension': 'JP', 'answer': '1'},
        {'id': 6, 'dimension': 'TF', 'answer': '1'},
        {'id': 7, 'dimension': 'SN', 'answer': '1'},
        {'id': 8, 'dimension': 'EI', 'answer': '1'},
        {'id': 9, 'dimension': 'TF', 'answer': '1'},
        {'id': 10, 'dimension': 'JP', 'answer': '1'},
        {'id': 11, 'dimension': 'SN', 'answer': '1'},
        {'id': 12, 'dimension': 'EI', 'answer': '1'},
        {'id': 13, 'dimension': 'TF', 'answer': '1'},
        {'id': 14, 'dimension': 'JP', 'answer': '1'},
        {'id': 15, 'dimension': 'SN', 'answer': '1'},
    ]
    
    results = calculate_mbti_type(answers)
    
    assert results['type'] == 'ESTJ'
    assert results['scores']['E'] == 7
    assert results['scores']['I'] == 0
    assert results['scores']['S'] == 7
    assert results['scores']['N'] == 0
    assert results['scores']['T'] == 7
    assert results['scores']['F'] == 0
    assert results['scores']['J'] == 7
    assert results['scores']['P'] == 0

def test_calculate_mbti_type_mixed():
    # 测试混合回答的MBTI类型计算
    answers = [
        {'id': 1, 'dimension': 'EI', 'answer': '1'},
        {'id': 2, 'dimension': 'TF', 'answer': '1'},
        {'id': 3, 'dimension': 'JP', 'answer': '1'},
        {'id': 4, 'dimension': 'SN', 'answer': '1'},
        {'id': 5, 'dimension': 'JP', 'answer': '2'},
        {'id': 6, 'dimension': 'TF', 'answer': '2'},
        {'id': 7, 'dimension': 'SN', 'answer': '2'},
        {'id': 8, 'dimension': 'EI', 'answer': '2'},
        {'id': 9, 'dimension': 'TF', 'answer': '1'},
        {'id': 10, 'dimension': 'JP', 'answer': '2'},
        {'id': 11, 'dimension': 'SN', 'answer': '1'},
        {'id': 12, 'dimension': 'EI', 'answer': '1'},
        {'id': 13, 'dimension': 'TF', 'answer': '2'},
        {'id': 14, 'dimension': 'JP', 'answer': '1'},
        {'id': 15, 'dimension': 'SN', 'answer': '2'},
    ]
    
    results = calculate_mbti_type(answers)
    
    assert results['type'] == 'ENFP'
    assert results['scores']['E'] == 3
    assert results['scores']['I'] == 2
    assert results['scores']['S'] == 2
    assert results['scores']['N'] == 3
    assert results['scores']['T'] == 2
    assert results['scores']['F'] == 3
    assert results['scores']['J'] == 2
    assert results['scores']['P'] == 3