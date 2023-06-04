from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename ,asksaveasfilename
import subprocess
import os

python_app = Tk()
python_app.title('Python IDLE')
python_app.geometry('1240x630+150+80')
python_app.config(bg='#323846')
python_app.resizable(False,False)

file_path = ''
def set_file_path(path):
    global file_path
    file_path=path

def open_file():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code = file.read()
        code_input.delete('1.0',END)
        code_input.insert('1.0',code)
        set_file_path(path)

def save():
    if file_path=='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path =file_path
    with open(path,'w') as f:
        code = code_input.get('1.0',END)
        f.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        messagebox.showerror('Python IDLE','Save the file')
    command = f'python {file_path}'
    process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    outpt , error = process.communicate()
    code_output.insert('1.0',outpt)
    code_output.insert('1.0',error)
    
###################################Icon image of App####################################
icon = PhotoImage(file='C:\\Users\\Hp\\OneDrive\\Pictures\\gg.png')
python_app.iconphoto(False,icon)


code_input = Text(python_app,font='Sylfaen')
code_input.place(x=180,y=0,width=680,height=720)


code_output = Text(python_app,font='Sylfaen',bg='#323846',fg='lightgreen')
code_output.place(x=860,y=0,width=420,height=700)

##############################################################Menu bar#########################################

Mymenu = Menu(python_app)

filemenu = Menu(Mymenu, tearoff=False)

##################File Menu
Mymenu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='📂 Run File',accelerator='    Ctrl+O',command=run)
filemenu.add_command(label='📂 Open File',accelerator='    Ctrl+O',command=open_file)
filemenu.add_command(label='📁 Save File',accelerator='    Ctrl+s',command=save)
filemenu.add_command(label='✖ Exit',accelerator='    Ctrl+E')


python_app.config(menu=Mymenu)

python_app.mainloop()