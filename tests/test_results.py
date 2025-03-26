import pytest
import tempfile
import csv
import os
from mbti.results import display_results, save_results
from mbti.calculator import calculate_mbti_type

def test_display_results_zh():
    # 测试中文结果显示
    answers = [
        {'id': 1, 'dimension': 'EI', 'answer': '1'},
        {'id': 2, 'dimension': 'TF', 'answer': '1'},
        {'id': 3, 'dimension': 'JP', 'answer': '1'},
        {'id': 4, 'dimension': 'SN', 'answer': '1'},
    ]
    
    results = calculate_mbti_type(answers)
    
    # 重定向标准输出以捕获打印内容
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    display_results(results, language='zh')
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    
    assert "你的 MBTI 类型结果:" in output
    assert "总体类型" in output
    assert "维度得分" in output
    assert "外向 (E)" in output
    assert "内向 (I)" in output
    assert "实感 (S)" in output
    assert "直觉 (N)" in output
    assert "理智 (T)" in output
    assert "情感 (F)" in output
    assert "判断 (J)" in output
    assert "理解 (P)" in output

def test_display_results_en():
    # 测试英文结果显示
    answers = [
        {'id': 1, 'dimension': 'EI', 'answer': '1'},
        {'id': 2, 'dimension': 'TF', 'answer': '1'},
        {'id': 3, 'dimension': 'JP', 'answer': '1'},
        {'id': 4, 'dimension': 'SN', 'answer': '1'},
    ]
    
    results = calculate_mbti_type(answers)
    
    # 重定向标准输出以捕获打印内容
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    display_results(results, language='en')
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    
    assert "Your MBTI Type Results:" in output
    assert "Overall Type" in output
    assert "Dimension Scores" in output
    assert "Extraversion (E)" in output
    assert "Introversion (I)" in output
    assert "Sensing (S)" in output
    assert "Intuition (N)" in output
    assert "Thinking (T)" in output
    assert "Feeling (F)" in output
    assert "Judging (J)" in output
    assert "Perceiving (P)" in output

def test_save_results():
    # 测试保存结果到CSV文件
    answers = [
        {'id': 1, 'dimension': 'EI', 'answer': '1'},
        {'id': 2, 'dimension': 'TF', 'answer': '1'},
        {'id': 3, 'dimension': 'JP', 'answer': '1'},
        {'id': 4, 'dimension': 'SN', 'answer': '1'},
    ]
    
    results = calculate_mbti_type(answers)
    
    # 创建临时目录保存结果
    with tempfile.TemporaryDirectory() as temp_dir:
        # 保存结果
        save_results(results, language='zh')
        
        # 检查文件是否创建
        assert os.path.exists(os.path.join(temp_dir, 'results'))
        
        # 检查CSV文件内容
        csv_files = [f for f in os.listdir(os.path.join(temp_dir, 'results')) if f.endswith('.csv')]
        assert len(csv_files) == 1
        
        csv_file = csv_files[0]
        csv_path = os.path.join(temp_dir, 'results', csv_file)
        
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            assert len(rows) == 1
            assert rows[0]['Dimension'] == 'Overall'
            assert rows[0]['Type'] == 'ESTJ'
            assert int(rows[0]['Score_E']) == 4
            assert int(rows[0]['Score_I']) == 0
            assert int(rows[0]['Score_S']) == 4
            assert int(rows[0]['Score_N']) == 0
            assert int(rows[0]['Score_T']) == 4
            assert int(rows[0]['Score_F']) == 0
            assert int(rows[0]['Score_J']) == 4
            assert int(rows[0]['Score_P']) == 0