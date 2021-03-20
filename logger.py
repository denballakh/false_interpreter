__all__ = ['Logger']

class Logger:
    def __init__(self, s=''):
        self.data = s

    def log(self, *msg):
        items = [str(item) for item in msg]
        for item in items:
            self.data += item

    def print(self):
        print(self.data)

    def __str__(self):
        return self.data

    def __repr__(self):
        return f'Logger({self.data})'


if __name__ == "__main__":
    print("This module is not for direct call!")
