import re

def replace_special_characters(text):
    # Define a dictionary mapping special characters to their names
    special_characters = {
        '!': 'exclamation',
        '@': 'at',
        '#': 'hash',
        '$': 'dollar',
        '%': 'percent',
        '^': 'caret',
        '&': 'and',
        '*': 'asterisk',
        '(': 'left_parenthesis',
        ')': 'right_parenthesis',
        '_': 'underscore',
        '-': 'hyphen',
        '+': 'plus',
        '=': 'equal',
        '{': 'left_brace',
        '}': 'right_brace',
        '[': 'left_square_bracket',
        ']': 'right_square_bracket',
        '|': 'pipe',
        '\\': 'backslash',
        ':': 'colon',
        ';': 'semicolon',
        '"': 'double_quote',
        "'": 'single_quote',
        '<': 'less_than',
        '>': 'greater_than',
        ',': 'comma',
        '.': 'dot',
        '?': 'question',
        '/': 'slash',
        ' ': '+'
    }

    # Define regular expression pattern to find special characters
    pattern = re.compile(r'[' + re.escape(''.join(special_characters.keys())) + ']')

    # Replace special characters with their names
    replaced_text = pattern.sub(lambda x: special_characters[x.group()], text)

    return replaced_text

# Example usage:
text = input("Enter your text here::")
result = replace_special_characters(text)
print(result)
