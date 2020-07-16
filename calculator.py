import tkinter as tk

def calculate(x,y,z):
    if z == '+':
        calc = (x + y)
        return calc
    elif z == '-':
        calc = (x - y)
        return calc
    elif z == '*':
        calc = (x * y)
        return calc
    elif z == '/':
        calc = (x / y)
        return calc
    else:
        calc = 'error'

def onClick(x):
    if x == 1:
        outputBox.insert(tk.END,x)
    elif x == 2:
        outputBox.insert(tk.END,x)
    elif x == 3:
        outputBox.insert(tk.END,x)
    elif x == 4:
        outputBox.insert(tk.END,x)
    elif x == 5:
        outputBox.insert(tk.END,x)
    elif x == 6:
        outputBox.insert(tk.END,x)
    elif x == 7:
        outputBox.insert(tk.END,x)
    elif x == 8:
        outputBox.insert(tk.END,x)
    elif x == 9:
        outputBox.insert(tk.END,x)
    elif x == 0:
        outputBox.insert(tk.END,x)
    else:
        eqOne = outputBox.get('1.0',tk.END)
        opget = outputBox.get(tk.END)
        global eqOneInt
        eqOneInt = int(eqOne)
        outputBox.delete('1.0',tk.END)
        outputBox.insert(tk.END,x)
        global operator
        operator = str(x)
        outputBox.delete('1.0',tk.END) 
    
def resultClick():
    eqTwoInt = 0
    eqTwo = outputBox.get('1.0',tk.END)
    eqTwoInt = int(eqTwo)
    result = calculate(eqOneInt,eqTwoInt,operator)
    outputBox.delete('1.0',tk.END)
    outputBox.insert(tk.END,result)

def clearClick():
    outputBox.delete('1.0',tk.END)
    

calculator = tk.Tk()
calculator.title('Calculator')
calculator.geometry('320x430')

outputFrame = tk.Frame(width=245,height=85)
outputFrame.grid(row=0,column=1,columnspan=3)
outputFrame.columnconfigure(0,weight=10)
outputFrame.grid_propagate(False)

outputBox = tk.Text(outputFrame)
outputBox.bind('<Key>',lambda e: 'break')
outputBox.grid(row=0,column=0)

input1 = tk.Button(calculator,text='1',height=5,width=10,command=lambda:onClick(1))
input2 = tk.Button(calculator,text='2',height=5,width=10,command=lambda:onClick(2))
input3 = tk.Button(calculator,text='3',height=5,width=10,command=lambda:onClick(3))
input4 = tk.Button(calculator,text='4',height=5,width=10,command=lambda:onClick(4))
input5 = tk.Button(calculator,text='5',height=5,width=10,command=lambda:onClick(5))
input6 = tk.Button(calculator,text='6',height=5,width=10,command=lambda:onClick(6))
input7 = tk.Button(calculator,text='7',height=5,width=10,command=lambda:onClick(7))
input8 = tk.Button(calculator,text='8',height=5,width=10,command=lambda:onClick(8))
input9 = tk.Button(calculator,text='9',height=5,width=10,command=lambda:onClick(9))
input0 = tk.Button(calculator,text='0',height=5,width=10,command=lambda:onClick(0))


inputClear = tk.Button(calculator,text='CLR',height=5,width=10,command=clearClick)
inputPlus = tk.Button(calculator,text='+',height=5,width=10,command=lambda:onClick('+'))
inputMinus = tk.Button(calculator,text='-',height=5,width=10,command=lambda:onClick('-'))
inputMultiply = tk.Button(calculator,text='*',height=5,width=10,command=lambda:onClick('*'))
inputDivide = tk.Button(calculator,text='/',height=5,width=10,command=lambda:onClick('/'))
inputResult = tk.Button(calculator,text='=',height=5,width=22,command=resultClick)

input1.grid(row=3,column=0)
input2.grid(row=3,column=1)
input3.grid(row=3,column=2)
input4.grid(row=2,column=0)
input5.grid(row=2,column=1)
input6.grid(row=2,column=2)
input7.grid(row=1,column=0)
input8.grid(row=1,column=1)
input9.grid(row=1,column=2)
input0.grid(row=4,column=0)

inputPlus.grid(row=1,column=3)
inputMinus.grid(row=2,column=3)
inputMultiply.grid(row=3,column=3)
inputResult.grid(row=4,column=2,columnspan=2)
inputDivide.grid(row=4,column=1)
inputClear.grid(row=0,column=0)

tk.mainloop()
