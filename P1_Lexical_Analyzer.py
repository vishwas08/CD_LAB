import re

def is_operator(char):
    return char in ['+', '-', '*', '/', '>', '<', '=']

def is_valid_identifier(token):
    return token[0].isalpha() and not token.isdigit()

def get_keywords():
    return ["auto", "break", "case", "char", "const", "continue", "default", "do",
            "double", "else", "enum", "extern", "float", "for", "goto", "if",
            "int", "long", "register", "return", "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

def is_integer(token):
    try:
        int(token)
        return True
    except ValueError:
        return False

def lexical_analyzer(input_str):
    tokens = re.findall(r'[a-zA-Z_]\w*|[-+*/<>=]|[(),;]|[0-9]+', input_str)
    print('Tokens: ')
    for token in tokens:
        if token in ['+', '-', '*', '/', '>', '<', '=']:
            print(f"Operator -> {token}")
        elif token in [',', ';', '(', ')']:
            print(f"Delimiter -> {token}")
        elif token in get_keywords():
            print(f"Keyword -> {token}")
        elif is_integer(token):
            print(f"Integer ->  {token}")
        elif is_valid_identifier(token):
            print(f"Identifier ->  {token}")
        else:
            print(f"Unidentified -> {token}")

if __name__ == "__main__":
    input_string = input("Enter a sentence: ")
    lexical_analyzer(input_string)

