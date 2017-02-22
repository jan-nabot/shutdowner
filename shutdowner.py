'''Learning Python, conserving energy, scheduling shutdown easily, falling asleep without knowledge of .bat's or powershell ;) '''

import tkinter
from subprocess import Popen

def main():
    GUI()

def setit(time):
    command = Popen('shutdown.exe -s -t {}'.format(time), shell = True)

def abortit(entryinput):
    command = Popen('shutdown.exe -a', shell = True)

def GUI():
    def proceeder(entryinput): # bind probably pass something here, because with 0 arguments function throw TypeError
        if custopt0.get() != '':
            takeout = int(custopt0.get()) * 60
            setit(takeout)
            custopt0.delete('0','end')
        else:
            setit(cvar.get() * 60) 

    window = tkinter.Tk()
    window.title = 'Shutdowner'    
    cvar = tkinter.IntVar() # 'when rb is selected, variable is set to its current value'. needed to decide which button is selected.
    defoptlab = tkinter.Label(window, text = 'Default delays: ').grid(row = 0, column = 0) 
    # doing .grid and others in same line as declaring button variable leads to issues
    custoptlab = tkinter.Label(window, text = 'Custom delay: ').grid(row = 0, column = 1)
    defopt0 = tkinter.Radiobutton(window, text = '150 min', value = 150, variable = cvar)
    defopt0.select()
    defopt0.grid(row = 1, column = 0)
    defopt1 = tkinter.Radiobutton(window, text = '60 min', value = 60, variable = cvar).grid(row = 2, column = 0)
    defopt2 = tkinter.Radiobutton(window, text = '90 min', value = 90, variable = cvar).grid(row = 3, column = 0)
    defopt3 = tkinter.Radiobutton(window, text = '240 min', value = 240, variable = cvar).grid(row = 4, column = 0)
    custopt0 = tkinter.Entry(window, width = 15)
    custopt0.grid(row = 1, column = 1)
    custopt1 = tkinter.Button(window, text = 'PROCEED')
    custopt1.grid(row = 2, column = 1)
    custopt1.bind('<Button-1>', proceeder)
    abortopt0 = tkinter.Button(window, text = 'ABORT')
    abortopt0.grid(row = 3, column = 1)
    abortopt0.bind('<Button-1>', abortit)
    window.mainloop()
    
    
main()
