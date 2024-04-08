import ply.lex as lex

tokens = [
    'INT'
]

t_ignore  = ' \t'

def t_FLOAT(t):
    r'((((\d+(_\d+)).(\d+(_\d+))))|(((\d+(_\d+)).(\d+(_\d+))))|(((\d+(_\d+)).(\d+(_\d+))))|((\d+(_\d+))))([eE][+-]?(\d+(_\d+)))?'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+(_\d+)*'
    t.value = int(t.value)
    return t

def getLexer():
    return lex.lex()