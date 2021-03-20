__all__ = ['Value_Int', 'Value_Float', 'Value_Bool', 'Value_String', 'Value_Lambda', 'Value_Name']

class Value:
    value = None
    # def __init__(self, value): self.value = value
    def __str__(self): return str(self.value)
    def __repr__(self): return self.__class__.__name__ + f'({self.value!r})'

class Value_Int(Value):
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        if isinstance(other, Value_Int):    return Value_Int(self.value + other.value)
        # if isinstance(other, Value_Float):  return Value_Float(self.value + other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __sub__(self, other):
        if isinstance(other, Value_Int):    return Value_Int(self.value - other.value)
        # if isinstance(other, Value_Float):  return Value_Float(self.value - other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __mul__(self, other):
        if isinstance(other, Value_Int):    return Value_Int(self.value * other.value)
        # if isinstance(other, Value_Float):  return Value_Float(self.value * other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __truediv__(self, other):
        if isinstance(other, Value_Int):    return Value_Int(self.value // other.value)
        # if isinstance(other, Value_Float):  return Value_Float(self.value / other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __gt__(self, other):
        if isinstance(other, Value_Int):    return Value_Bool(self.value > other.value)
        # if isinstance(other, Value_Float):  return Value_Bool(self.value > other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __eq__(self, other):
        if isinstance(other, Value_Int):    return Value_Bool(self.value == other.value)
        # if isinstance(other, Value_Float):  return Value_Bool(self.value == other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __or__(self, other):
        if isinstance(other, Value_Int):    return Value_Int(self.value | other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __and__(self, other):
        if isinstance(other, Value_Int):    return Value_Int(self.value & other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __bool__(self):
        return bool(self.value)

    def __neg__(self):
        return Value_Int(-self.value)


class Value_Bool(Value_Int):
    def __init__(self, value):
        self.value = bool(value)

    def __bool__(self):
        return self.value

class Value_Float(Value):
    ...
#     def __init__(self, value):
#         self.value = float(value)

#     def __add__(self, other):
#         if isinstance(other, Value_Int):    return Value_Float(self.value + other.value)
#         if isinstance(other, Value_Float):  return Value_Float(self.value + other.value)
#         raise TypeError('Unsupported operation for {self} and {other}.')

#     def __sub__(self, other):
#         if isinstance(other, Value_Int):    return Value_Float(self.value - other.value)
#         if isinstance(other, Value_Float):  return Value_Float(self.value - other.value)
#         raise TypeError('Unsupported operation for {self} and {other}.')

#     def __mul__(self, other):
#         if isinstance(other, Value_Int):    return Value_Float(self.value * other.value)
#         if isinstance(other, Value_Float):  return Value_Float(self.value * other.value)
#         raise TypeError('Unsupported operation for {self} and {other}.')

#     def __truediv__(self, other):
#         if isinstance(other, Value_Int):    return Value_Float(self.value / other.value)
#         if isinstance(other, Value_Float):  return Value_Float(self.value / other.value)
#         raise TypeError('Unsupported operation for {self} and {other}.')

#     def __gt__(self, other):
#         if isinstance(other, Value_Int):    return Value_Bool(self.value > other.value)
#         if isinstance(other, Value_Float):  return Value_Bool(self.value > other.value)
#         raise TypeError('Unsupported operation for {self} and {other}.')

#     def __eq__(self, other):
#         if isinstance(other, Value_Int):    return Value_Bool(self.value == other.value)
#         if isinstance(other, Value_Float):  return Value_Bool(self.value == other.value)
#         raise TypeError('Unsupported operation for {self} and {other}.')

#     def __bool__(self):
#         return bool(self.value)

#     def __neg__(self):
#         return Value_Float(-self.value)

class Value_String(Value):
    def __init__(self, value):
        self.value = str(value)

    def __add__(self, other):
        if isinstance(other, Value_String):    return Value_String(self.value + other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __gt__(self, other):
        if isinstance(other, Value_String):    return Value_Bool(self.value > other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __eq__(self, other):
        if isinstance(other, Value_String):    return Value_Bool(self.value == other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

class Value_Lambda(Value):
    def __init__(self, value):
        self.value = value

    def __str__(self): return f'[{self.value}]'

    def __eq__(self, other):
        if isinstance(other, Value_Lambda):    return Value_Bool(self.value == other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

class Value_Name(Value):
    def __init__(self, value):
        self.value = str(value)

    def __eq__(self, other):
        if isinstance(other, Value_Name):    return Value_Bool(self.value == other.value)
        raise TypeError(f'Unsupported operation for {self!r} and {other!r}.')

    def __hash__(self):
        return hash(self.value)

if __name__ == "__main__":
    print("This module is not for direct call!")
