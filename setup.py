from setuptools import setup, find_packages

setup(
    name='mbti-test',
    version='0.3.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        # 添加项目依赖项
    ],
    entry_points={
        'console_scripts': [
            'mbti-test=mbti.entry_point:main'
        ]
    },
    package_data={
        'mbti': [
            'data/questions_28.json',
            'data/questions_40.json',
            'data/questions_93.json'
        ]
    },
    include_package_data=True,
    author='luhuadong',
    author_email='luhuadong@163.com',
    description='A command line application for taking the MBTI personality test',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/luhuadong/mbti-test',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)