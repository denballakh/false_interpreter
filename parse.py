from constants import STATES, CHARS, TOKEN_TYPES
from token import Token, TokenList

__all__ = ['parse', ]

def parse(code):
    n = '\n'
    print(f"PARSING {code.replace(n, '')}")
    code += ' '

    result = TokenList()

    i = 0
    state = STATES.NONE
    buff = ''
    stop = False
    counter = None
    while i < len(code):
        char = code[i]
        prev = code[i-1] if i > 0 else ''
        # next = code[i+1] if i < len(code) - 1 else ''

        if state == STATES.NONE:
            if char == '[':
                buff = ''
                state = STATES.LAMBDA
                counter = 1

            elif char == '{':
                buff = ''
                state = STATES.COMMENT
                counter = 1

            elif char == ']' or char == '}':
                raise SyntaxError(f'Unbalanced brackets!')

            elif char in CHARS.NUMBER:
                buff = char
                state = STATES.NUMBER

            elif char in CHARS.STRING:
                buff = char
                state = STATES.NAME

            elif char == '\'':
                state = STATES.CHAR

            elif char == '"':
                state = STATES.STRING

            elif char in CHARS.EMPTY:
                pass

            else:
                result.append(Token(TOKEN_TYPES.SYMBOL, char))

        elif state == STATES.NUMBER:
            if char in CHARS.NUMBER:
                buff += char
            else:
                result.append(Token(TOKEN_TYPES.NUMBER, buff))
                buff = ''
                state = STATES.NONE
                stop = 1

        elif state == STATES.NAME:
            if char in CHARS.STRING:
                buff += char

            else:
                result.append(Token(TOKEN_TYPES.NAME, buff))
                buff = ''
                state = STATES.NONE
                stop = 1

        elif state == STATES.LAMBDA:
            if char == '[':
                buff += char
                counter += 1
            elif char == ']':
                counter -= 1
                if counter < 0:
                    raise SyntaxError(f'Unbalanced brackets!')
                elif counter == 0:
                    counter = None
                    result.append(Token(TOKEN_TYPES.LAMBDA, parse(buff)))
                    buff = ''
                    state = STATES.NONE
                else:
                    buff += char
            else:
                buff += char

        elif state == STATES.CHAR:
            result.append(Token(TOKEN_TYPES.CHAR, char))
            state = STATES.NONE

        elif state == STATES.STRING:
            if char == '"':
                if prev == '\\':
                    buff += char
                else:
                    result.append(Token(TOKEN_TYPES.STRING, buff))
                    buff = ''
                    state = STATES.NONE
            elif char == '\\':
                if prev == '\\':
                    buff += char
                else:
                    pass
            else:
                buff += char

        elif state == STATES.COMMENT:
            if char == '{':
                counter += 1
            elif char == '}':
                counter -= 1
                if counter < 0:
                    raise SyntaxError(f'Unbalanced brackets!')
                elif counter == 0:
                    result.append(Token(TOKEN_TYPES.COMMENT, buff))
                    counter = None
                    buff = ''
                    state = STATES.NONE
            else:
                buff += char


        if stop:
            stop = False
        else:
            i += 1

    if state != STATES.NONE:
        raise SyntaxError(f'Invalid state: {state}')

    return result

if __name__ == "__main__":
    print("This module is not for direct call!")

# print(parse('10'))
