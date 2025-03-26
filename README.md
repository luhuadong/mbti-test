# MBTI-Test

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![PyPI Version](https://img.shields.io/pypi/v/mbti-test.svg)](https://pypi.org/project/mbti-test/)

[中文](README_zh.md) | [English](README.md)

MBTI-Test is a command line application for taking the MBTI personality test, written in Python.

## Description

This program allows users to take the MBTI personality test directly from the command line. It includes both 28-question and 93-question versions of the test.

## Features

- Multiple test versions: quick (28 questions), common (40 questions) and standard (93 questions)
- Command line interface for easy access
- Result calculation and display
- Option to save results to a CSV file

## Installation

```bash
pip install mbti-test
```

## Usage

mbti-test command line usage examples：

```bash
mbti-test --help                     # Show help information
mbti-test --questions 40             # Run the 40-question version（Default is Chinese）
mbti-test --questions 40 --lang en   # Run the 40-question version（English）
mbti-test --questions 40 --save      # Run the 40-question version, and save results to CSV file
mbti-test --version                  # Show the version
```

## Run Test

Execute the following command to start the test (common version).

```bash
mbti-test --questions 40 --lang en
```

MBTI test interface screenshot:

![](./figures/mbti-test-demo-en.jpg)

MBTI test result output:

```bash
✨ Test complete! Generating results...

Your MBTI Type Results:
Overall Type: INTJ

Dimension Scores:
Extraversion (E) vs Introversion (I): 5 - 6
Sensing (S) vs Intuition (N): 3 - 6
Thinking (T) vs Feeling (F): 6 - 3
Judging (J) vs Perceiving (P): 6 - 5
```

