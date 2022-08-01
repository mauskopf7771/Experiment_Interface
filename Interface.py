# INTERFACE FOR LOADING PSYCHOPY EXPERIMENTS

from tkinter import *
import webbrowser 
from PIL import Image 
from PIL import ImageTk
import os
#import sym
#import StroopExp
#import Stroop_Experiment.py
#import stroop_experiment

#Jack is a cunt

os.chdir('/Users/[REDACTED]/Desktop')
#Get working directory and stuff
# To import stuff from other python code - you simply do from [python file] import * or probably just do import [python file].

root = Tk()
root.title = '[REDACTED]'

#root.iconbitmap() Puts an icon in the corner thing

#Get screen width and height
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry('%dx%d' %(height, width))
root.resizable(True, True)

## IMAGES ##
# You can make these the background of buttons if you want - so that's very useful
# Load the image
#image=Image.open('users/[REDACTED]/desktop/open_day_interface/[REDACTED].jpg')
#img=image #.resize((250, 150))
# Conver the image in TkImage
#my_img=ImageTk.PhotoImage(img)
# Display the image with label
#label=Label(root, image=my_img)
#label.place(relx = 0.35, rely = 0) #relx = 0.349

#stroopimage = PhotoImage(file = r'stroop.gif')
stickfigureimage = print('coming soon') #just make sure after text you have image = stickfigureimage
emotionaldotprobeimage = print('coming soon too') #same detail

def Gotostroop():
    webbrowser.open('https://www.duckduckgo.com') #Actual site redacted

# Create four very large buttons for each experiment
#image = stroopimage
Stroopbutton = Button(root, text = 'STROOP', command = Gotostroop, padx = 50, pady = 50) #pad changes the size of the button - then we need to get a graphic of the experiment
Stroopbutton.place(anchor=E, relheight=0.30, relwidth=0.30, relx=0.65, rely = 0.8)

def GotoEmotionalDotProbe():
    webbrowser.open('https://www.duckduckgo.com') #Actual site redacted

exp2button = Button(root, text = 'Emotional Dot Probe', command = GotoEmotionalDotProbe, padx = 50, pady = 50) #pad changes the size of the button - then we need to get a graphic of the experiment
exp2button.place(anchor=E, relheight=0.30, relwidth=0.30, relx= 1, rely = 0.8)

def GotoStickFigureTask():
    #sym.suckyourmum()
    #StroopExp()
    webbrowser.open('https://www.duckduckgo.com') #Actual site redacted

exp3button = Button(root, text = 'Stick Figure Task', command = GotoStickFigureTask, padx = 50, pady = 50) #pad changes the size of the button - then we need to get a graphic of the experiment
exp3button.place(anchor=E, relheight=0.30, relwidth=0.30, relx=0.3, rely = 0.8)

#def Gotoexperiment4():
#    webbrowser.open('https://www.wikipedia.org')

#exp4button = Button(root, text = 'EXP_4', command = Gotoexperiment4, padx = 50, pady = 50) #pad changes the size of the button - then we need to get a graphic of the experiment
#exp4button.place(anchor=E, relheight=0.25, relwidth=0.25, relx=0.85, rely = 0.25)

#def Gotoexperiment4():
#    webbrowser.open('https://www.wikipedia.org')

#exp4button = Button(root, text = 'EXP_4', command = Gotoexperiment4, padx = 50, pady = 50) #pad changes the size of the button - then we need to get a graphic of the experiment
#exp4button.place(anchor=E, relheight=0.25, relwidth=0.25, relx=0.85, rely = 0.25)

#def Gotoexperiment5():
#    webbrowser.open('https://www.youtube.com')

#exp5button = Button(root, text = 'EXP_2', command = Gotoexperiment5, padx = 50, pady = 50) #pad changes the size of the button - then we need to get a graphic of the experiment
#exp5button.place(anchor=E, relheight=0.25, relwidth=0.25, relx=0.85, rely = 0.75)

#def Gotoexperiment6():
#    webbrowser.open('https://www.youtube.com')

#exp6button = Button(root, text = 'EXP_2', command = Gotoexperiment6, padx = 50, pady = 50) #pad changes the size of the button - then we need to get a graphic of the experiment
#exp6button.place(anchor=E, relheight=0.25, relwidth=0.25, relx=0.85, rely = 0.75)



#Doesn't work
#import webview
#webview.start()
##webview.create_window('Geeks for Geeks', 'https://google.com')

#webbrowser.open('https://www.google.com')

### QuitButton = Button(root, text = 'quit', command = root.quit)

#Make label Widget 
#myLabel = Label(root, text ='University of East London')
#Put label on screen
#myLabel.pack(padx = 200, pady = 200)

#Making clicks
#You need to make a function so it'd be someting like:
#define myClick():
    #Then we'd want it to do something like open a psychopy experiment. This is defined in the button - so we just need a few large buttons on a screen
    #Then just ways of making it looks nice
    #


#Buttons (example code)
#myButton = Button(root, text = 'Click me!', command = [function_name], padx = 50, pady = 50) pad changes the size of the button - then we need to get a graphic of the experiment
#myButton.place()

root.mainloop()