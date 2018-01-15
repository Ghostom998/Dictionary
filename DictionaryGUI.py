import sys
import json
from difflib import get_close_matches
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

# Load dictionary data to read from into a python dictionary
data = json.load(open("data.json"))

def translate(w):
    # interprets all values in lower case
    w = w.lower() 
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        return SimWord(get_close_matches(w,data.keys())[0])
    else:
        return "The word does not exist. Please check your input and try again."

# Create a message for similar words and attempt to prevent errors in that
def SimWord(AltWord):
    Message = "Showing results instead for " + AltWord + ":"
    TempOutput = data[AltWord]
    if Message not in TempOutput:
        TempOutput.insert(0,Message)
        return TempOutput
    else:
        return TempOutput

# Take word from arguement or interface
if len(sys.argv) == 1:
    #word = raw_input("Enter a word: ")
    window = Tk()
    window.title("Dictionary")
elif len(sys.argv) == 2:
    word = sys.argv[1]
    output = translate(word)
else:
    print "Command line takes 0 or 1 arguements.\nFor example try \"python dictionary.py rain\""
    exit()

# Return definition to GUI
def translateGUI():
    t1.delete(1.0,END)
    output = translate(e1_val.get())
    if type(output) == list:
        for item in output:
            print t1.insert(END,item+"\n")
    else:
        print t1.insert(END,output)

'''
GUI Data Below
'''

# Create a variable to store our word in
e1_val = StringVar()
# Make an Entry field (to enter data)
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0,column=0,sticky=W)

# Make a button
b1 = Button(window, text='Define', command=translateGUI)
b1.grid(row=0,column=1,sticky=E)

# Make a scrollbar to add to text
scrollbar = Scrollbar(window)
scrollbar.grid(row=1,column=2,sticky=E)
# Make a text field to display output
t1 = Text(window,height=5,width=40,wrap=WORD,yscrollcommand=scrollbar.set)
t1.grid(row=1,column=0,columnspan=2)

# Renders the window. Must be kept at the end of the code!
window.mainloop()
