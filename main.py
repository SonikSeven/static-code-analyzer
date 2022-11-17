import sys
import os


def analyze_file(path):
    with open(path) as user_file:
        code = user_file.readlines()

    for n, line in enumerate(code, 1):
        if line == "\n":
            continue
        statement, *comment = line.split("#", 1)
        comment = str(*comment)
        if len(line) > 79:
            print(f"{path}: Line {n}: S001 Too long")
        if (len(statement) - len(statement.lstrip())) % 4:
            print(f"{path}: Line {n}: S002 Indentation is not a multiple of four")
        if statement and statement.rstrip()[-1] == ";":
            print(f"{path}: Line {n}: S003 Unnecessary semicolon")
        if statement and comment and len(statement) - len(statement.rstrip()) < 2:
            print(f"{path}: Line {n}: S004 At least two spaces required before inline comments")
        statement = statement.strip()
        if comment and comment.lower().find("todo") != -1:
            print(f"{path}: Line {n}: S005 TODO found")
        if code[n - 4:n - 1] == ["\n", "\n", "\n"]:
            print(f"{path}: Line {n}: S006 More than two blank lines used before this line")
        if statement.startswith("class"):
            name = statement[5:].strip().split("(")[0]
            if len(statement[5:]) - len(statement[5:].lstrip()) > 1:
                print(f"{path}: Line {n}: S007 Too many spaces after 'class'")
            if name[0].islower() or "_" in statement:
                print(f"{path}: Line {n}: S008 Class name '{name}' should use CamelCase")
        elif statement.startswith("def"):
            name = statement[3:].strip().split("(")[0]
            if len(statement[3:]) - len(statement[3:].lstrip()) > 1:
                print(f"{path}: Line {n}: S007 Too many spaces after 'def'")
            if name.lower() != name:
                print(f"{path}: Line {n}: S009 Function name '{name}' should use snake_case")
            if args := line.split("(")[1].split(")")[0].split(", "):
                args = [tuple(arg.split("=")) for arg in args]
                for arg in args:
                    if arg[0].lower() != arg[0]:
                        print(f"{path}: Line {n}: S010 Argument name '{arg[0]}' should be snake_case")
                    if arg[1:] and arg[1] in ("[]", "{}"):
                        print(f"{path}: Line {n}: S012 Default argument value is mutable")
        elif "=" in statement:
            name = statement.split("=")[0]
            if name.lower() != name:
                print(f"{path}: Line {n}: S011 Variable '{name}' should be snake_case")


def main():
    if sys.argv[1].endswith(".py"):
        return analyze_file(sys.argv[1])
    for root, _, names in os.walk(sys.argv[1]):
        for name in names:
            if name.endswith(".py") and name != "tests.py":
                path = os.path.join(root, name)
                analyze_file(path)


if __name__ == "__main__":
    main()
