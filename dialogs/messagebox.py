#
# This file is part of Project PythonSnacks, code collection for python beginners.
# Copyright (C) 2024  Attila Gallai
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, LGPL 2.1 version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import os


class TXInputBox(simpledialog.Dialog):
    """A simple dialog with a text message.
    """
    def __init__(self, parent, title=None, text=None, size=None, button1="Ok", button2="Cancel", button3=None, buttonWidth=10, defaultButton=1):
        """Initialize the dialog.
        After dialog has been closed the result attribute contains the value of the button pressed.

        Arguments:
        ----------
            parent -- the parent window \n
            title -- the title of the dialog \n
            text -- the text to display \n
            size -- the size of the dialog (optional) \n
            button1 -- the text of the first button \n
            button2 -- the text of the second button \n
            button3 -- the text of the third button \n
            buttonWidth -- the width of the buttons
        """
        self.text    = text
        self.size    = size
        self.result  = None
        self.button1 = button1
        self.button2 = button2
        self.button3 = button3
        self.result  = None
        self.buttonWidth   = buttonWidth
        self.defaultButton = defaultButton

        # Setup the hardcoded logo image
        self.logoFile  = os.path.join(os.path.dirname(__file__), "dragon-logo.png")
        self.logoSize  = (50, 50)
        self.logoImage = Image.open(self.logoFile)
        self.logo = self.logoImage.resize(self.logoSize, resample=Image.Resampling.LANCZOS)
        
        # convert the image to a tkinter image
        self.logo = ImageTk.PhotoImage(self.logo)
        
        super().__init__(parent, title)


    def body(self, master) :
        """Create the dialog.
        
        Arguments:
        ----------
            master -- the parent window \n
        """
        if self.size:
            # set the size of the dialog when it was given
            super().geometry(f"{self.size[0]}x{self.size[1]}")

        # Create the left side logo image of the dialog
        leftImage = tk.Label(master, image=self.logo)
        leftImage.grid(row=0, column=0, padx=10, pady=10)

        self.label = tk.Label(master, text=self.text)
        self.label.grid(row=0, column=1, padx=10, pady=10)
        super().resizable(False, False)


    def buttonbox(self):
        """Create the buttons.
        """
        box = tk.Frame(self)
        box.pack(side=tk.BOTTOM, padx=5, pady=5)

        if self.button3:
            defaultState = tk.ACTIVE if self.defaultButton == 3 else tk.NORMAL
            btn = tk.Button(box, text=self.button3, width=self.buttonWidth, command=self.Onbutton3, default=defaultState)
            btn.pack(side=tk.RIGHT, padx=5, pady=5)

        if self.button2:
            defaultState = tk.ACTIVE if self.defaultButton == 2 else tk.NORMAL
            btn = tk.Button(box, text=self.button2, width=self.buttonWidth, command=self.Onbutton2, default=defaultState)
            btn.pack(side=tk.RIGHT, padx=5, pady=5)

        defaultState = tk.ACTIVE if self.defaultButton == 1 else tk.NORMAL
        btn = tk.Button(box, text=self.button1, width=self.buttonWidth, command=self.Onbutton1, default=defaultState)
        btn.pack(side=tk.RIGHT, padx=5, pady=5)

    
    def Onbutton1(self):
        """Handle the Ok button.
        """
        self.result = 1
        self.ok()


    def Onbutton2(self):
        """Handle the Cancel button.
        """
        self.result = 2
        self.cancel()


    def Onbutton3(self):
        """Handle the third button.
        """
        self.result = 3
        self.cancel()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    # Show a simple message dialog
    longMessage = ['Hey User!', 'This is a long message. It is displayed in a dialog.', 'You can use it to display important information.']
    dialog = TXInputBox(root, title="Message", text="\n".join(longMessage), button2=None, button3=None)
    print("Dialog closed by button{}".format(dialog.result))

    # Show a dialog with two buttons (Yes/No question)
    longMessage = ['You are about to exit the program', '', 'Are you sure to continue?']
    dialog = TXInputBox(root, title="Exit...", text="\n".join(longMessage), button1="Yes", button2="No", defaultButton=2)
    print("Dialog closed by button{}".format(dialog.result))

    # Show a dialog with three buttons
    longMessage = ['The file already exists!', '', 'Would you like to update the file?']
    dialog = TXInputBox(root, title="Save file...", text="\n".join(longMessage), button1="Yes", button2="No", button3="Save as", defaultButton=3)
    print("Dialog closed by button{}".format(dialog.result))




