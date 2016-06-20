# #
# a python program to turn off sarlens computer late at night
# #
# #
# The following is how he did Tkinter in my book
# #
#
# from Tkinter import *
#
# class Window(Frame):
#     """ window that says to sleep """
#     def __init__(self, master):
#         """ initialize the frame """
#         Frame.__init__(self, master)
#         self.grid()
#         self.create_widget()
#
#     def create_widget(self):
#         """ create button to display click number """
#         Label(self,
#               text = "Go to bed, Sarlen!"
#               ).grid(row = 0, column = 0, sticky = W)
#
# # main
# root = Tk()
# root.title("Shutdown Reporter")
# root.geometry("400x100")
#
# app = Window(root)
#
# root.mainloop()
#
# #
# here is how I saw how to do Tkinter in the docs
# #

import Tkinter as tk
from time import sleep
from datetime import datetime
import os

# set up window stuff
master = tk.Tk()
master.title("Shutdown Reporter")

w = tk.Label(master, text="Go to bed, Sarlen!",
                    font=("Helvetica", 72),
                    bg="#000000", fg="#ff0000",
                    borderwidth=200)
w.pack()

# debug
#tk.mainloop()

# run main loop always
while True:
    d = datetime.now()
    if d.hour in (23, 0, 1, 2, 3, 4, 5, 6):      # between midnight and 6 am
        os.system("shutdown /s /t 30")      # full shutdown in 30 secs
        
        #debug 
        #os.system("echo goodbye")

        tk.mainloop()   #show window

    sleep(60)   # wait 60 secs before checking again (save cpu)

