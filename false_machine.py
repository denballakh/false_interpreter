from value_types import Value_Lambda, Value_String, Value_Int
from token import TokenList
from stacks import ValueStack, CodeStack, Storage
from logger import Logger
from window import Window
from parse import parse

__all__ = ['FalseMachine', ]

class FalseMachine:
    def __init__(self, code=None):
        self.stack = ValueStack()
        self.storage = Storage()
        self.code_stack = CodeStack()
        self.output = Logger()

        self.window = Window(self)
        self.running = False

        if code is not None:
            self.push_code(parse(code))
            self.window.setCode(code)

        self.updateUI()


    def step(self):
        if self.code_stack.is_empty():
            self.pause()
            return

        code = self.code_stack.top()
        token = code.get()
        if token is None:
            # print(f'code: {code}')
            self.code_stack.pop()
        else:
            token.eval(self)
        #     print(f'token: {token.token_type:8} {token}')
        # print(f'stack: {self.stack}')
        # print()
        self.updateUI()

    def btn_run(self):
        self.running = True
        self.updateUI()
        self.run2()
    def btn_step(self):
        self.pause()
        self.step()
    def btn_pause(self):
        self.pause()
    def btn_reset(self):
        self.pause()
        self.stack = ValueStack()
        self.storage = Storage()
        self.code_stack = CodeStack()
        self.output = Logger()
        self.push_code(parse(self.window.getCode()))
        self.updateUI()


    def run2(self):
        if self.running:
            self.step()
            self.window.root.after(1, func=self.run2)
            self.updateUI()

    def pause(self):
        self.running = False
        self.updateUI()



    def updateUI(self):
        self.window.stackLabel.config(text=str(self.stack))
        self.window.codeStackLabel.config(text=str(self.code_stack))
        self.window.storageLabel.config(text=str(self.storage))
        self.window.outputLabel.config(text=str(self.output))

    def push_code(self, code):
        if isinstance(code, Value_Lambda): code = code.value
        if isinstance(code, str):
            raise TypeError(f'code: {code!r}')

        code = code.copy()

        self.code_stack.push(code)

        self.updateUI()

    def terminated(self):
        return len(self.code_stack.data) == 0

    def read_char(self):
        inp = self.window.getInput()
        if len(inp) == 0:
            return self.window.root.after(100, self.read_char)
        char, *inp = inp
        self.window.setInput(inp)
        return Value_Int(ord(char))



if __name__ == "__main__":
    print("This module is not for direct call!")
