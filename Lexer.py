import re

TOKEN_SPEC = [
    ("MODULE", r"\bmodule\b"),
    ("LET", r"\blet\b"),
    ("VAL", r"\bval\b"),
    ("FUNCTION_DEF", r"\bfunc\b"),
    ("COMMENT", r"\/\/.*"),
    ("COMMENT_BLOCK", r"/\*[\s\S]*?\*/"),
    ("L_BRACE", r"{"),
    ("R_BRACE", r"}"),
    ("L_BRACKET", r"\["),
    ("R_BRACKET", r"\]"),
    ("L_PAREN", r"\("),
    ("R_PAREN", r"\)"),

    # Types
    ("SIGNED_INT_8_TYPE", r"\bi8\b"),
    ("UNSIGNED_INT_8_TYPE", r"\bu8\b"),
    ("SIGNED_INT_16_TYPE", r"\bi16\b"),
    ("UNSIGNED_INT_16_TYPE", r"\bu16\b"),
    ("SIGNED_INT_32_TYPE", r"\bi32\b"),
    ("UNSIGNED_INT_32_TYPE", r"\bu32\b"),
    ("SIGNED_INT_64_TYPE", r"\bi64\b"),
    ("UNSIGNED_INT_64_TYPE", r"\bu64\b"),
    ("FLOAT_32_TYPE", r"\bf32\b"),
    ("FLOAT_64_TYPE", r"\bf64\b"),
    ("BOOL_TYPE", r"\bbool\b"),
    ("CHAR_TYPE", r"\bchar\b"),
    ("STRING_TYPE", r"\bstr\b"),

    # Literals
    ("TRUE_LITERAL", r"\btrue\b"),
    ("FALSE_LITERAL", r"\bfalse\b"),
    ("CHAR_LITERAL", r"'(\\.|[^\\'])'"),

    # Float before integer to prevent splitting floats
    ("FLOAT_LITERAL", r"\b\d+\.\d+\b"),
    ("INTEGER_LITERAL", r"\b\d+\b"),

    # Operators and symbols
    ("EQ", r"=="),                # equality operator before assign
    ("NEQ", r"!="),
    ("LTE", r"<="),
    ("GTE", r">="),
    ("ASSIGN", r"="),             # fixed typo from ASIGN

    ("LT", r"<"),
    ("GT", r">"),
    
    ("POINTER", r"\^"),
    ("POINTER_DEREFERENCE", r"\*"),
    ("ADDRESS_OPERATOR", r"&"),
    ("COLON", r":"),
    ("SIMI_COLON", r";"),
    ("COMMA", r","),
    ("DOT", r"\."),
    ("ARROW", r"->"),

    # Arithmetic
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULTIPLY", r"\*"),
    ("DIVIDE", r"/"),
    ("MODULO", r"%"),

    # Logical
    ("AND", r"\band\b"),
    ("OR", r"\bor\b"),
    ("NOT", r"\bnot\b"),

    # Control flow
    ("IF", r"\bif\b"),
    ("ELSE", r"\belse\b"),
    ("WHILE", r"\bwhile\b"),
    ("FOR", r"\bfor\b"),
    ("RETURN", r"\breturn\b"),
    ("BREAK", r"\bbreak\b"),
    ("CONTINUE", r"\bcontinue\b"),

    # Identifiers (last so keywords are matched before)
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),

    # Whitespace and newlines (ignored)
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t\r]+"),
]

TOKEN_REGEX = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)
token_re = re.compile(TOKEN_REGEX)

def lex(text):
    for mo in token_re.finditer(text):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP' or kind == 'NEWLINE':
            continue
        yield (kind, value)


test_code = """
module test_module

let x: i32 = 42;
let y: f64 = 3.14;
func add(a: i32, b: i32) -> i32 {
    return a + b;
}

// This is a comment
/* This is a block comment */

if x == 42 and y > 3.0 {
    return true;
} else {
    return false;
}
"""

for token in lex(test_code):
    print(token)
