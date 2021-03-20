Hello, World!Hello, World!import tkinter as tk

__all__ = ['Window', ]

class Window:
    def __init__(self, machine):
        self.machine = machine
        self.root = root = tk.Tk()

        root.minsize(500, 500)

        root.columnconfigure(0, weight=1, minsize=500)

        root.rowconfigure(0, weight=0, minsize=50)
        root.rowconfigure(1, weight=0, minsize=200)
        root.rowconfigure(2, weight=0, minsize=200)
        root.rowconfigure(3, weight=0, minsize=100)
        root.rowconfigure(4, weight=0, minsize=25)
        root.rowconfigure(5, weight=1, minsize=200)
        root.rowconfigure(6, weight=0, minsize=50)


        self.stackLabel = tk.Label(master=root)
        self.codeStackLabel = tk.Label(master=root)
        self.storageLabel = tk.Label(master=root)
        self.outputLabel = tk.Label(master=root)
        buttonsFrame = tk.Label(master=root)
        self.codeText = tk.Text(master=root)
        self.inputText = tk.Text(master=root)


        self.stackLabel.grid(row=0, column=0, sticky='nsew')
        self.codeStackLabel.grid(row=1, column=0, sticky='nsew')
        self.storageLabel.grid(row=2, column=0, sticky='nsew')
        self.outputLabel.grid(row=3, column=0, sticky='nsew')
        buttonsFrame.grid(row=4, column=0, sticky='nsew')
        self.codeText.grid(row=5, column=0, sticky='nsew')
        self.inputText.grid(row=6, column=0, sticky='nsew')

        self.stackLabel.config(
            font=("Consolas", 10),
            bg='black',
            fg='white',
            borderwidth=2,
            relief='groove',
            anchor='nw', justify='left',
            wraplength=500,
        )
        self.codeStackLabel.config(
            font=("Consolas", 10),
            bg='black',
            fg='white',
            borderwidth=2,
            relief='groove',
            anchor='nw', justify='left',
            wraplength=500,
        )
        self.storageLabel.config(
            font=("Consolas", 10),
            bg='black',
            fg='white',
            borderwidth=2,
            relief='groove',
            anchor='nw', justify='left',
            wraplength=500,
        )
        self.outputLabel.config(
            font=("Consolas", 10),
            bg='black',
            fg='white',
            borderwidth=2,
            relief='groove',
            anchor='nw', justify='left',
            wraplength=500,
        )
        buttonsFrame.config(
            borderwidth=2,
            relief='groove',
        )
        self.codeText.config(
            font=("Consolas", 15),
            bg='black',
            fg='white',
            borderwidth=2,
            relief='groove',
            wrap='word',
        )
        self.inputText.config(
            font=("Consolas", 15),
            bg='black',
            fg='white',
            borderwidth=2,
            relief='groove',
            wrap='word',
        )
        buttonsFrame.config(
            bg='black',
        )


        runButton = tk.Button(master=buttonsFrame, text='run', command=self.machine.btn_run, bg='white', fg='black')
        pauseButton = tk.Button(master=buttonsFrame, text='pause', command=self.machine.btn_pause, bg='white', fg='black')
        stepButton = tk.Button(master=buttonsFrame, text='step', command=self.machine.btn_step, bg='white', fg='black')
        resetButton = tk.Button(master=buttonsFrame, text='reset', command=self.machine.btn_reset, bg='white', fg='black')

        runButton.pack(side='left')
        pauseButton.pack(side='left')
        stepButton.pack(side='left')
        resetButton.pack(side='left')

    def getCode(self):
        return self.codeText.get('1.0', 'end')

    def setCode(self, newstring):
        self.codeText.delete('1.0', 'end')
        self.codeText.insert('end', newstring)

    def getInput(self):
        return self.inputText.get('1.0', 'end')

    def setInput(self, newstring):
        self.inputText.delete('1.0', 'end')
        self.inputText.insert('end', newstring)

if __name__ == "__main__":
    print("This module is not for direct call!")
