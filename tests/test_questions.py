import os
import json
import pytest
from mbti.questions import load_questions

def test_load_questions_quick_zh():
    # 测试加载28题中文版本
    questions = load_questions(version='quick', language='zh')
    assert len(questions) == 28
    assert 'id' in questions[0]
    assert 'question' in questions[0]
    assert 'options' in questions[0]
    assert 'dimension' in questions[0]
    assert questions[0]['id'] == 1
    assert isinstance(questions[0]['question'], dict)
    assert isinstance(questions[0]['options'], dict)
    assert questions[0]['dimension'] in ['EI', 'SN', 'TF', 'JP']

def test_load_questions_quick_en():
    # 测试加载28题英文版本
    questions = load_questions(version='quick', language='en')
    assert len(questions) == 28
    assert 'id' in questions[0]
    assert 'question' in questions[0]
    assert 'options' in questions[0]
    assert 'dimension' in questions[0]
    assert questions[0]['id'] == 1
    assert isinstance(questions[0]['question'], dict)
    assert isinstance(questions[0]['options'], dict)
    assert questions[0]['dimension'] in ['EI', 'SN', 'TF', 'JP']

def test_load_questions_standard_zh():
    # 测试加载93题中文版本
    questions = load_questions(version='standard', language='zh')
    assert len(questions) == 93
    assert 'id' in questions[0]
    assert 'question' in questions[0]
    assert 'options' in questions[0]
    assert 'dimension' in questions[0]
    assert questions[0]['id'] == 1
    assert isinstance(questions[0]['question'], dict)
    assert isinstance(questions[0]['options'], dict)
    assert questions[0]['dimension'] in ['EI', 'SN', 'TF', 'JP']

def test_load_questions_standard_en():
    # 测试加载93题英文版本
    questions = load_questions(version='standard', language='en')
    assert len(questions) == 93
    assert 'id' in questions[0]
    assert 'question' in questions[0]
    assert 'options' in questions[0]
    assert 'dimension' in questions[0]
    assert questions[0]['id'] == 1
    assert isinstance(questions[0]['question'], dict)
    assert isinstance(questions[0]['options'], dict)
    assert questions[0]['dimension'] in ['EI', 'SN', 'TF', 'JP']