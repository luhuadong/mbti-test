# MBTI-Test

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![PyPI Version](https://img.shields.io/pypi/v/mbti-test.svg)](https://pypi.org    /project/mbti-test/)

[中文](README_zh.md) | [English](README.md)

MBTI-Test is a command line application for taking the MBTI personality test, written in Python.

## Description

This program allows users to take the MBTI personality test directly from the command line. It includes both 28-question and 93-question versions of the test.

## Features

- Two test versions: quick (28 questions) and comprehensive (93 questions)
- Command line interface for easy access
- Result calculation and display
- Option to save results to a CSV file

## Installation

```bash
pip install mbti-test
```

## Usage

```bash
mbti-test --version         # Show the version
mbti-test --help            # Show help information
mbti-test --short           # Run the 28-question version
mbti-test --long            # Run the 93-question version
mbti-test --save            # Save results to CSV file
```

