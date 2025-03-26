import json
import os
from pathlib import Path
from mbti.i18n.core import translator

def load_question_registry():
    """加载试题注册表"""
    current_dir = Path(__file__).parent
    registry_file = current_dir / "data" / "question_registry.json"
    
    try:
        with open(registry_file, 'r', encoding='utf-8') as f:
            registry = json.load(f)
        return registry['available_tests']
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load question registry: {str(e)}")

def validate_question_count(question_count):
    """验证题目数量是否有效"""
    registry = load_question_registry()
    available_counts = [test['question_count'] for test in registry]
    
    if question_count not in available_counts:
        raise ValueError(
            f"Invalid question count: {question_count}. "
            f"Available options: {available_counts}"
        )

def load_questions(question_count, language='zh'):

    translator.language = language

    validate_question_count(question_count)

    registry = load_question_registry()
    for test in registry:
        if test['question_count'] == question_count:
            filename = test['filename']
            break
    
    current_dir = Path(__file__).parent
    questions_file = current_dir / "data" / filename
    
    try:
        with open(questions_file, 'r', encoding='utf-8') as f:
            return json.load(f)['MBTI_questions']
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Question file {filename} not found for count {question_count}"
        )
