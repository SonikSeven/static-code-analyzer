# Static Code Analyzer

Welcome to the Static Code Analyzer GitHub project! This tool is designed to help Python developers by conducting static analysis of their Python code files for common style and design issues. It provides immediate feedback on potential improvements, helping ensure adherence to Python's PEP 8 style guide and common best practices.

## Features

The Code Analyzer scans through your Python files and identifies the following issues:

- **S001 Too long**: Line length exceeding 79 characters.
- **S002 Indentation is not a multiple of four**: Ensures consistent code indentation.
- **S003 Unnecessary semicolon**: Identifies redundant semicolons at the end of statements.
- **S004 At least two spaces required before inline comments**: Checks for adequate spacing before comments.
- **S005 TODO found**: Highlights TODO comments in the code.
- **S006 More than two lines used before this line**: Ensures proper use of whitespace.
- **S007 Too many spaces after 'class'/'def'**: Checks for excessive spaces.
- **S008 Class name should use CamelCase**: Enforces CamelCase for class names.
- **S009 Function name should use snake_case**: Enforces snake_case for function names.
- **S010 Argument name should be snake_case**: Enforces snake_case for argument names.
- **S011 Variable be snake_case**: Enforces snake_case for variable names.
- **S012 Default argument value is mutable**: Warns against mutable default argument values.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/static-code-analyzer.git
```

## Usage

Open a terminal and navigate to the directory where the script is located.

To analyze a single Python file:

```
python main.py your_script.py
```

To analyze all Python files in a directory (excluding `tests.py` files):

```
python main.py your_directory_path
```

## License

This project is licensed under the [MIT License](LICENSE.txt).
