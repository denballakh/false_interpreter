from constants import TOKEN_TYPES
from value_types import Value_Int, Value_Bool, Value_String, Value_Lambda, Value_Name

__all__ = ['Token', 'TokenList', ]

class TokenList:
    def __init__(self, data=None):
        self.data = data if data is not None else []
        self.cnt = -1

    def append(self, value):
        self.data.append(value)

    def copy(self):
        return TokenList([t.copy() for t in self.data])

    def get(self):
        if len(self.data) == 0:
            return None

        if self.is_empty():
            return None

        if self.cnt == -1:
            self.cnt = 0
            return self.data[0]

        if self.data[self.cnt].stop:
            self.data[self.cnt].stop = False
        else:
            self.cnt += 1

        if self.is_empty():
            return None

        return self.data[self.cnt]

    def is_empty(self):
        return self.cnt >= len(self.data)

    def __str__(self):
        s = ''
        for token in self.data:
            s += str(token)
        return s

    def __repr__(self):
        return f'TokenList({self.data!r})'

    def __bool__(self):
        return bool(len(self.data))

class Token:
    def __init__(self, token_type, code):
        self.token_type = token_type
        self.code = code

        self.stop = False
        self.state = 0
        self.data = None

    def copy(self):
        return Token(self.token_type, self.code)

    def __str__(self):
        if self.token_type == TOKEN_TYPES.LAMBDA:
            return '[' + f'{self.code}' + ']'
        if self.token_type == TOKEN_TYPES.COMMENT:
            return '{' + f'{self.code}' + '}'
        if self.token_type == TOKEN_TYPES.STRING:
            return '"' + f'{self.code}' + '"'
        return self.code

    def __repr__(self):
        return f'Token({self.token_type!r},{self.code!r})'

    def eval(self, machine):
        tp = self.token_type
        code = self.code
        stack = machine.stack
        output = machine.output

        if tp == TOKEN_TYPES.NUMBER:
            stack.push(Value_Int(code))
        elif tp == TOKEN_TYPES.NAME:
            stack.push(Value_Name(code))
        elif tp == TOKEN_TYPES.LAMBDA:
            stack.push(Value_Lambda(code))
        elif tp == TOKEN_TYPES.CHAR:
            stack.push(Value_String(code))
        elif tp == TOKEN_TYPES.STRING:
            output.log(f'{code}')
        elif tp == TOKEN_TYPES.COMMENT:
            # print(f'comment: {code}')
            pass
        elif tp == TOKEN_TYPES.SYMBOL:
            if code == '+':
                a = stack.pop()
                b = stack.pop()
                stack.push(b + a)
            elif code == '-':
                a = stack.pop()
                b = stack.pop()
                stack.push(b - a)
            elif code == '*':
                a = stack.pop()
                b = stack.pop()
                stack.push(b * a)
            elif code == '/':
                a = stack.pop()
                b = stack.pop()
                stack.push(b / a)
            elif code == '_':
                a = stack.pop()
                stack.push(-a)
            elif code == '$':
                a = stack.pop()
                stack.push(a)
                stack.push(a)
            elif code == '%':
                a = stack.pop()
            elif code == '\\':
                a = stack.pop()
                b = stack.pop()
                stack.push(a)
                stack.push(b)
            elif code == '@':
                a = stack.pop()
                b = stack.pop()
                c = stack.pop()
                stack.push(b)
                stack.push(a)
                stack.push(c)
            elif code == 'ø':
                n = stack.pop()
                stack.push(stack.data[~n])
            elif code == '=':
                a = stack.pop()
                b = stack.pop()
                stack.push(b == a)
            elif code == '>':
                a = stack.pop()
                b = stack.pop()
                stack.push(b > a)
            elif code == '&':
                a = stack.pop()
                b = stack.pop()
                stack.push(b & a)
            elif code == '|':
                a = stack.pop()
                b = stack.pop()
                stack.push(b | a)
            elif code == '~':
                a = stack.pop()
                stack.push(Value_Bool(not a))
            elif code == ':':
                name = stack.pop()
                value = stack.pop()
                if not isinstance(name, Value_Name): raise TypeError(f'Invalid operands type (>{type(name)}< and {type(value)}) for symbol {code}')
                if not isinstance(value, Value_Lambda): raise TypeError(f'Invalid operands type ({type(name)} and >{type(value)}<) for symbol {code}')
                machine.storage[name] = value
            elif code == ';':
                name = stack.pop()
                if not isinstance(name, Value_Name): raise TypeError(f'Invalid operand type ({type(name)}) for symbol {code}')
                stack.push(machine.storage[name])
            elif code == '!':
                func = stack.pop()
                machine.push_code(func)
            elif code == '?':
                func = stack.pop()
                cond = stack.pop()
                if cond:
                    machine.push_code(func)
            elif code == '#':
                if self.state == 0:
                    self.stop = True
                    self.state = 1

                    func = stack.pop()
                    cond = stack.pop()
                    self.data = (func, cond)
                    machine.push_code(cond)
                elif self.state == 1:
                    func, cond = self.data

                    condval = stack.pop()
                    if condval:
                        self.stop = True
                        self.state = 2

                        machine.push_code(func)
                    else:
                        self.state = -1
                elif self.state == 2:
                    func, cond = self.data
                    self.stop = True
                    self.state = 1

                    machine.push_code(cond)
            elif code == '.':
                output.log(f'{stack.pop()}')
            elif code == ',':
                x = stack.pop()
                if isinstance(x, Value_Int):
                    output.log(f'{chr(x.value)}')
                elif isinstance(x, Value_String):
                    if len(str(x)) != 1: raise ValueError(f'Cannot print char with len != 1. {x}')
                    output.log(f'{x}')
                else:
                    raise TypeError(f'Cannot print non-int and non-char value: {x}')
            elif code == '^':
                stack.push(machine.read_char())
            elif code == 'ß':
                output.log('<flush>')

if __name__ == "__main__":
    print("This module is not for direct call!")
