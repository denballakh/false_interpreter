from enum import Enum, unique

@unique
class STATES(Enum):
    NONE = 'NONE'
    NUMBER = 'NUMBER'
    NAME = 'NAME'
    LAMBDA = 'LAMBDA'
    CHAR = 'CHAR'
    STRING = 'STRING'
    COMMENT = 'COMMENT'

@unique
class TOKEN_TYPES(Enum):
    NUMBER = 'NUMBER'
    NAME = 'NAME'
    LAMBDA = 'LAMBDA'
    CHAR = 'CHAR'
    STRING = 'STRING'
    COMMENT = 'COMMENT'
    SYMBOL = 'SYMBOL'

class CHARS:
    NUMBER = '0123456789'
    STRING = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    EMPTY = ' ' + '\t' + '\n' + '\r'

# @unique
# class VALUE_TYPES(Enum):
#     INT = 'int'
#     FLOAT = 'float'
#     STRING = 'str'
#     LAMBDA = 'lambda'
#     NAME = 'id'

if __name__ == "__main__":
    print("This module is not for direct call!")
