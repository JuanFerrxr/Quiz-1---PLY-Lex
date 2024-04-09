import ply.lex as lex

tokens = (
    'INT',
    'FLOAT',
    'STR'
)

def t_FLOAT(t):
    r'((((\d+(\_\d+)*)\.(\d+(\_\d+)*)*))|(((\d+(\_\d+)*)*\.(\d+(\_\d+)*)))|(((\d+(\_\d+)*)\.(\d+(\_\d+)*)))|((\d+(\_\d+)*)))([eE][+-]?(\d+(\_\d+)*))?'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+(_\d+)*'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  
    return t

t_ignore  = ' \t'

def getLexer():
    return lex.lex()