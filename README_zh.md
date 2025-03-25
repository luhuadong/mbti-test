# MBTI-Test

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![PyPI Version](https://img.shields.io/pypi/v/mbti-test.svg)](https://pypi.org    /project/mbti-test/)

[English](README.md) | [中文](README_zh.md)

MBTI-Test 是一个用于进行 MBTI 人格测试的命令行应用程序，使用 Python 编写。

## 描述

这个程序允许用户直接在命令行中进行 MBTI 人格测试。它包含了 28 题和 93 题两个版本的测试。

## 功能

- 两个测试版本：快速（28 题）和全面（93 题）
- 简单易用的命令行界面
- 结果计算与展示
- 可将结果保存到 CSV 文件

## 安装

```bash
pip install mbti-test
```

## 使用

```bash
mbti-test --version         # 显示版本信息
mbti-test --help            # 显示帮助信息
mbti-test --short           # 运行 28 题版本
mbti-test --long            # 运行 93 题版本
mbti-test --save            # 将结果保存到 CSV 文件
```

