from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import SaveAs, asksaveasfilename, askopenfilename
from tkinter import messagebox
import os
import subprocess

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        #self.master.bind("<Control-r>", self.saveRun)

    def init_window(self):
        self.master.title("Flow")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label="Open File...", command=self.OpenFile)
        file.add_command(label="Open Folder...", command=self.OpenFolder)
        file.add_command(label="Save", accelerator="Ctrl+S", command=self.Save)
        file.add_command(label="Save As", command=self.SaveAs)

        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Undo  Ctrl+Z")
        edit.add_command(label="Redo  Ctrl+Y")

        menu.add_cascade(label="Edit", menu=edit)

        view = Menu(menu)
        view.add_command(label="Light Theme", command=self.light)
        view.add_command(label="Darkish Theme", command=self.dark)
        view.add_command(label="Darker Theme", command=self.darker)
        view.add_command(label="Hacker Theme", command=self.hacker)
        view.add_command(label="Slate Theme", command=self.slate)
        view.add_command(label="Gradient Theme", command=self.gradient)
        view.add_command(label="Font", command=self.font)

        menu.add_cascade(label="View", menu=view)

        python = Menu(menu)
        python.add_command(label="Python IDLE", command=self.idle)
        menu.add_cascade(label="Python", menu=python)

        menu.add_command(label="Run", command=self.run)

    def client_exit(self):
        exit()
    
    def OpenFile(event=None):
        #path = askopenfilename(filetypes=[('Python Files', '*.py')])
        path = askopenfilename()
        with open(path, 'r') as file:
            code = file.read()
            text.delete('1.0', END)
            text.insert('1.0', code)
            set_file_path(path)
            root.title("Flow - " + file_path)

    def OpenFolder(event=None):
        filename = filedialog.askdirectory()
        with open(filename, "r") as f:
            return

    def SaveAs(event=None):
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as file:
            code = text.get('1.0', END)
            file.write(code)
            set_file_path(path)

    def Save(self, event=None):
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as file:
            code = text.get('1.0', END)
            file.write(code)
            set_file_path(path)

    def light(self):
        text.configure(bg="white", fg="black", insertbackground="black")
        outputWin.configure(bg="white", fg="black", insertbackground="black")

    def dark(self):
        text.configure(bg="#272727", fg="#F59E06", insertbackground="#F59E06")
        outputWin.configure(bg="#272727", fg="#F59E06", insertbackground="#F59E06")

    def hacker(self):
        text.configure(bg="black", fg="#0EF901", insertbackground="#0EF901")
        outputWin.configure(bg="black", fg="#0EF901",
                            insertbackground="#0EF901")

    def slate(self):
        text.configure(bg="#164962", fg="white", insertbackground="white")
        outputWin.configure(bg="#164962", fg="white", insertbackground="white")

    def darker(self):
        text.configure(bg="black", fg="white", insertbackground="white")
        outputWin.configure(bg="black", fg="white", insertbackground="white")

    def gradient(self):
        bgI = PhotoImage(file="gradient.png")
        label1 = Label(root, image=bgI)
        label1.place(x=0, y=0)
        #text.configure(bg=bgI, fg="white", insertbackground="white")

    def font(self):
        root = Tk()
        root.title("Fonts")
        #root.iconbitmap("flowicon.ico")

        def arial():
            size = e.get('1.0', END)
            text.configure(font=("Arial", size))
            outputWin.configure(font=("Arial", size))

        def georgia():
            size = e.get('1.0', END)
            text.configure(font=("Georgia", size))
            outputWin.configure(font=("Georgia", size))

        def courier():
            size = e.get('1.0', END)
            text.configure(font=("Courier", size))
            outputWin.configure(font=("Courier", size))

        def consolas():
            size = e.get('1.0', END)
            text.configure(font=("Consolas", size))
            outputWin.configure(font=("Consolas", size))

        def customTheme():
            bg = e1.get()
            text.configure(bg=bg)
            outputWin.configure(bg=bg)
            fg = e2.get()
            text.configure(fg=fg)
            outputWin.configure(fg=fg)

        Button(root, text="Consolas\n(Defult)", font="Consolas",
               borderwidth=1, width=10, command=consolas).grid(row=0, column=0)
        Button(root, text="Arial", font="Arial", borderwidth=1,
               width=10, command=arial).grid(row=1, column=0)
        Button(root, text="Georgia", font="Georgia", borderwidth=1,
               width=10, command=georgia).grid(row=2, column=0)
        Button(root, text="Courier", font="Courier", borderwidth=1,
               width=9, command=courier).grid(row=3, column=0)
        Label(root, text="Size:").grid(row=0, column=1)
        e = Text(root, width=5, height=1)
        e.insert('1.0', "11")
        e.grid(row=0, column=2)
        Label(root, text="Custom Theme", font="Georgia 13").grid(row=1, column=1)
        Label(root, text="BG Color:").grid(row=2, column=1)
        e1 = Entry(root, width=10)
        e1.grid(row=2, column=2)
        Label(root, text="Text Color:").grid(row=3, column=1)
        e2 = Entry(root, width=10)
        e2.grid(row=3, column=2)
        Button(root, text="Create Theme",
               command=customTheme).grid(row=4, column=1)

    def syntaxColors(self):
        ###########  BIG WORK IN PROGRESS  ############
        text_area_text = text.get('1.0', END)
        #text.tag_add("import", "1.0", "end-1c")
        #text.tag_configure("import", foreground="red")
        #if "import" in text_area_text:
        #text.tag_add("import")
        #text.tag_configure("import", foreground="red")
    
    def run(self, event=None):
        if file_path == '':
            save_prompt = Toplevel()
            save_prompt.iconbitmap('flowicon.ico')
            text = Label(save_prompt, text='Error: Code Not Saved', padx=20, pady=20)
            text.pack()
            return
        elif ".txt" in file_path:
            save_prompt = Toplevel()
            save_prompt.iconbitmap('flowicon.ico')
            text = Label(save_prompt, text='Error: Not a Python file', padx=20, pady=20)
            text.pack()
            outputWin.insert('1.0', "  Not a Python file!!")
        command = f'python {file_path}'
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        outputWin.insert('1.0', output)
        outputWin.insert('1.0',  error)

    def idle(self):



        import tkinter as tk
        import sys
        import re
        from code import InteractiveConsole
        from contextlib import redirect_stderr, redirect_stdout
        from io import StringIO

        class History(list):
            def __getitem__(self, index):
                try:
                    return list.__getitem__(self, index)
                except IndexError:
                    return

        class TextConsole(tk.Text):
            def __init__(self, master, **kw):
                kw.setdefault('width', 50)
                kw.setdefault('wrap', 'word')
                kw.setdefault('prompt1', '>>> ')
                kw.setdefault('prompt2', '... ')
                banner = kw.pop('banner', 'Python %s\n' % sys.version)
                self._prompt1 = kw.pop('prompt1')
                self._prompt2 = kw.pop('prompt2')
                tk.Text.__init__(self, master, **kw)
                # --- history
                self.history = History()
                self._hist_item = 0
                self._hist_match = ''

                # --- initialization
                self._console = InteractiveConsole()  # python console to execute commands
                self.insert('end', banner, 'banner')
                self.prompt()
                self.mark_set('input', 'insert')
                self.mark_gravity('input', 'left')

                # --- bindings
                self.bind('<Control-Return>', self.on_ctrl_return)
                self.bind('<Shift-Return>', self.on_shift_return)
                self.bind('<KeyPress>', self.on_key_press)
                self.bind('<KeyRelease>', self.on_key_release)
                self.bind('<Tab>', self.on_tab)
                self.bind('<Down>', self.on_down)
                self.bind('<Up>', self.on_up)
                self.bind('<Return>', self.on_return)
                self.bind('<BackSpace>', self.on_backspace)
                self.bind('<Control-c>', self.on_ctrl_c)
                self.bind('<<Paste>>', self.on_paste)

            def on_ctrl_c(self, event):
                """Copy selected code, removing prompts first"""
                sel = self.tag_ranges('sel')
                if sel:
                    txt = self.get('sel.first', 'sel.last').splitlines()
                    lines = []
                    for i, line in enumerate(txt):
                        if line.startswith(self._prompt1):
                            lines.append(line[len(self._prompt1):])
                        elif line.startswith(self._prompt2):
                            lines.append(line[len(self._prompt2):])
                        else:
                            lines.append(line)
                    self.clipboard_clear()
                    self.clipboard_append('\n'.join(lines))
                return 'break'

            def on_paste(self, event):
                """Paste commands"""
                if self.compare('insert', '<', 'input'):
                    return "break"
                sel = self.tag_ranges('sel')
                if sel:
                    self.delete('sel.first', 'sel.last')
                txt = self.clipboard_get()
                self.insert("insert", txt)
                self.insert_cmd(self.get("input", "end"))
                return 'break'

            def prompt(self, result=False):
                """Insert a prompt"""
                if result:
                    self.insert('end', self._prompt2, 'prompt')
                else:
                    self.insert('end', self._prompt1, 'prompt')
                self.mark_set('input', 'end-1c')

            def on_key_press(self, event):
                """Prevent text insertion in command history"""
                if self.compare('insert', '<', 'input') and event.keysym not in ['Left', 'Right']:
                    self._hist_item = len(self.history)
                    self.mark_set('insert', 'input lineend')
                    if not event.char.isalnum():
                        return 'break'

            def on_key_release(self, event):
                """Reset history scrolling"""
                if self.compare('insert', '<', 'input') and event.keysym not in ['Left', 'Right']:
                    self._hist_item = len(self.history)
                    return 'break'

            def on_up(self, event):
                """Handle up arrow key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'end')
                    return 'break'
                elif self.index('input linestart') == self.index('insert linestart'):
                    # navigate history
                    line = self.get('input', 'insert')
                    self._hist_match = line
                    hist_item = self._hist_item
                    self._hist_item -= 1
                    item = self.history[self._hist_item]
                    while self._hist_item >= 0 and not item.startswith(line):
                        self._hist_item -= 1
                        item = self.history[self._hist_item]
                    if self._hist_item >= 0:
                        index = self.index('insert')
                        self.insert_cmd(item)
                        self.mark_set('insert', index)
                    else:
                        self._hist_item = hist_item
                    return 'break'

            def on_down(self, event):
                """Handle down arrow key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'end')
                    return 'break'
                elif self.compare('insert lineend', '==', 'end-1c'):
                    # navigate history
                    line = self._hist_match
                    self._hist_item += 1
                    item = self.history[self._hist_item]
                    while item is not None and not item.startswith(line):
                        self._hist_item += 1
                        item = self.history[self._hist_item]
                    if item is not None:
                        self.insert_cmd(item)
                        self.mark_set('insert', 'input+%ic' %
                                      len(self._hist_match))
                    else:
                        self._hist_item = len(self.history)
                        self.delete('input', 'end')
                        self.insert('insert', line)
                    return 'break'

            def on_tab(self, event):
                """Handle tab key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'input lineend')
                    return "break"
                # indent code
                sel = self.tag_ranges('sel')
                if sel:
                    start = str(self.index('sel.first'))
                    end = str(self.index('sel.last'))
                    start_line = int(start.split('.')[0])
                    end_line = int(end.split('.')[0]) + 1
                    for line in range(start_line, end_line):
                        self.insert('%i.0' % line, '    ')
                else:
                    txt = self.get('insert-1c')
                    if not txt.isalnum() and txt != '.':
                        self.insert('insert', '    ')
                return "break"

            def on_shift_return(self, event):
                """Handle Shift+Return key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'input lineend')
                    return 'break'
                else:  # execute commands
                    self.mark_set('insert', 'end')
                    self.insert('insert', '\n')
                    self.insert('insert', self._prompt2, 'prompt')
                    self.eval_current(True)

            def on_return(self, event=None):
                """Handle Return key press"""
                if self.compare('insert', '<', 'input'):
                    self.mark_set('insert', 'input lineend')
                    return 'break'
                else:
                    self.eval_current(True)
                    self.see('end')
                return 'break'

            def on_ctrl_return(self, event=None):
                """Handle Ctrl+Return key press"""
                self.insert('insert', '\n' + self._prompt2, 'prompt')
                return 'break'

            def on_backspace(self, event):
                """Handle delete key press"""
                if self.compare('insert', '<=', 'input'):
                    self.mark_set('insert', 'input lineend')
                    return 'break'
                sel = self.tag_ranges('sel')
                if sel:
                    self.delete('sel.first', 'sel.last')
                else:
                    linestart = self.get('insert linestart', 'insert')
                    if re.search(r'    $', linestart):
                        self.delete('insert-4c', 'insert')
                    else:
                        self.delete('insert-1c')
                return 'break'

            def insert_cmd(self, cmd):
                """Insert lines of code, adding prompts"""
                input_index = self.index('input')
                self.delete('input', 'end')
                lines = cmd.splitlines()
                if lines:
                    indent = len(re.search(r'^( )*', lines[0]).group())
                    self.insert('insert', lines[0][indent:])
                    for line in lines[1:]:
                        line = line[indent:]
                        self.insert('insert', '\n')
                        self.prompt(True)
                        self.insert('insert', line)
                        self.mark_set('input', input_index)
                self.see('end')

            def eval_current(self, auto_indent=False):
                """Evaluate code"""
                index = self.index('input')
                # commands to execute
                lines = self.get('input', 'insert lineend').splitlines()
                self.mark_set('insert', 'insert lineend')
                if lines:  # there is code to execute
                    # remove prompts
                    lines = [lines[0].rstrip()] + [line[len(self._prompt2):].rstrip()
                                                   for line in lines[1:]]
                    for i, l in enumerate(lines):
                        if l.endswith('?'):
                            lines[i] = 'help(%s)' % l[:-1]
                    cmds = '\n'.join(lines)
                    self.insert('insert', '\n')
                    out = StringIO()  # command output
                    err = StringIO()  # command error traceback
                    with redirect_stderr(err):     # redirect error traceback to err
                        with redirect_stdout(out):  # redirect command output
                            # execute commands in interactive console
                            res = self._console.push(cmds)
                            # if res is True, this is a partial command, e.g. 'def test():' and we need to wait for the rest of the code
                    errors = err.getvalue()
                    if errors:  # there were errors during the execution
                        self.insert('end', errors)  # display the traceback
                        self.mark_set('input', 'end')
                        self.see('end')
                        self.prompt()  # insert new prompt
                    else:
                        output = out.getvalue()  # get output
                        if output:
                            self.insert('end', output, 'output')
                        self.mark_set('input', 'end')
                        self.see('end')
                        if not res and self.compare('insert linestart', '>', 'insert'):
                            self.insert('insert', '\n')
                        self.prompt(res)
                        if auto_indent and lines:
                            # insert indentation similar to previous lines
                            indent = re.search(r'^( )*', lines[-1]).group()
                            line = lines[-1].strip()
                            if line and line[-1] == ':':
                                indent = indent + '    '
                            self.insert('insert', indent)
                        self.see('end')
                        if res:
                            self.mark_set('input', index)
                            # clear buffer since the whole command will be retrieved from the text widget
                            self._console.resetbuffer()
                        elif lines:
                            # add commands to history
                            self.history.append(lines)
                            self._hist_item = len(self.history)
                    out.close()
                    err.close()
                else:
                    self.insert('insert', '\n')
                    self.prompt()

        if __name__ == '__main__':
            root = tk.Tk()
            root.title("Flow IDLE")
            root.iconbitmap('flowicon.ico')
            console = TextConsole(root)
            console.pack(fill='both', expand=True)
            root.mainloop()


root = Tk()

root.geometry("900x500")
root.iconbitmap('flowicon.ico')

#scroll = Scrollbar(root)
#scroll.pack(side=RIGHT, fill=Y)

text = Text(root, padx=5, borderwidth=1, font="Consolas 11", undo=True)
text.pack(expand=True, fill=BOTH)
outputWin = Text(root, padx=0, borderwidth=1, font="Consolas 11", undo=True)
outputWin.pack(expand=True, fill=BOTH)
#yscrollcommand = scroll.set
#scroll.config(command=text.yview)

app = Window(root)

root.bind("<Control-s>", app.Save)
root.bind("<Control-r>", app.run)

root.mainloop()
