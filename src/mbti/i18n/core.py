import json
import os
from pathlib import Path

class Translator:
    def __init__(self, language='zh'):
        self.available_languages = self._get_available_languages()
        self.set_language(language)

    def _load_strings(self, lang):
        current_dir = Path(__file__).parent
        lang_file = current_dir / f"{lang}.json"
        
        try:
            with open(lang_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise ValueError(f"Language pack '{lang}' not found")

    def t(self, key, **kwargs):
        """获取翻译字符串并格式化"""
        keys = key.split('.')
        value = self.strings
        for k in keys:
            value = value.get(k, {})
        
        if not isinstance(value, str):
            raise KeyError(f"Translation key '{key}' not found")
        
        return value.format(**kwargs)
    
    def _get_available_languages(self):
        """获取所有可用语言"""
        return [f.stem for f in Path(__file__).parent.glob('*.json')]

    def set_language(self, lang):
        """动态切换语言"""
        if lang not in self.available_languages:
            raise ValueError(f"Unsupported language: {lang}. Available: {', '.join(self.available_languages)}")
        self.language = lang
        self.strings = self._load_strings(lang)

# 实例化单例
translator = Translator()