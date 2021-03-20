from value_types import *
from token import *

__all__ = ['ValueStack', 'CodeStack', 'Storage']

class Storage(dict):
    def __str__(self):
        s = ''
        for k, v in self.items():
            s += f'{k} = {v:}\n'
        return s

class Stack:
    def __init__(self, data=None):
        self.data = data if data is not None else []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            raise ValueError(f'Cannot pop in empty stack!')

        *self.data, result = self.data
        return result

    def is_empty(self):
        return len(self.data) == 0

    def top(self):
        if len(self.data) == 0:
            raise ValueError(f'Stack has no items!')

        return self.data[~0]


class ValueStack(Stack):
    def push(self, value):
        if not any(isinstance(value, t) for t in (Value_Int, Value_Float, Value_Bool, Value_String, Value_Lambda, Value_Name)):
            raise TypeError(f'Pushing invalid value: {value!r}')
        self.data.append(value)

    def __str__(self):
        s = ''
        for x in self.data:
            s += f'{x!s:10}'
        return s

    def __repr__(self):
        s = ''
        for x in self.data:
            s += f'{x!r},'
        return f'ValueStack([{s}])'

class CodeStack(Stack):
    def push(self, value):
        if not any(isinstance(value, t) for t in (TokenList,)):
            raise TypeError(f'Pushing invalid value: {value!r}')
        self.data.append(value)

    def __str__(self):
        s = ''
        for x in self.data:
            s += f'{x!s}\n'
        return s

    def __repr__(self):
        s = ''
        for x in self.data:
            s += f'{x!r},'
        return f'CodeStack([{s}])'

if __name__ == "__main__":
    print("This module is not for direct call!")
