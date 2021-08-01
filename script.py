from tkinter import *
from tkinter import messagebox
import subprocess
import sys



window = Tk()
window.wm_title("C++ Compiler")

FILE_NAME = StringVar()

def EDIT_FILE():
    FILE_PATH = str(FILE_NAME.get())
    PATH = f"editor ./src/{FILE_PATH}.cpp"
    CODE = open(f"src/{FILE_PATH}.cpp", "a+")
    if CODE.readlines() == []:
        CODE.write("#include <stdio.h>\n")
        CODE.write("int main () {\n")
        CODE.write("    printf('Hello World');\n")
        CODE.write("    return 0;\n")
        CODE.write("}")
    CODE.close()
    subprocess.Popen(PATH.split())

def CMP_RUN():
    FILE_PATH = str(FILE_NAME.get())
    OPEN = f"./objectfiles/{FILE_PATH}"
    RUN = f"g++ src/{FILE_PATH}.cpp -o objectfiles/{FILE_PATH}"
    subprocess.Popen(RUN.split())
    subprocess.Popen(OPEN.split())

def QUIT_GUI():
    window.destroy()
    sys.exit(0)

LABEL =Label(window,text="Enter File Name")
LABEL.pack()#grid( row = 1, column = 0 )

FIELD = Entry (window, textvariable = FILE_NAME)
FIELD.pack()#grid( row = 0 ,column = 1 )

EDIT = Button(window,text="Edit Code", width=12,command = EDIT_FILE)
EDIT.pack()#grid(row = 3,column = 3)

ACTION = Button(window,text="Build & Run", width=12,command = CMP_RUN)
ACTION.pack()#grid(row = 3,column = 3)
#MESSAGEBOX = messagebox.showinfo("title here", "text here")

QUIT = Button(window,text="Close", width=12,command = QUIT_GUI)
QUIT.pack()#grid(row = 3,column = 3)

window.mainloop()
