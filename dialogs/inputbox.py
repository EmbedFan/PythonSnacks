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

__version__ = "1.0"


class TXInputBox(simpledialog.Dialog) :
    """A simple dialog with an entry field.
    """
    VALIDATE_NONE    = None
    VALIDATE_INTEGER = 1
    VALIDATE_FLOAT   = 2
    CUSTOM_VALIDATOR = 4

    def __init__(self, parent, title=None, text=None, size=None, variable: tk.Variable = None, buttonWidth=6, defaultButton=1, validate=VALIDATE_NONE, validator=VALIDATE_NONE):
        """Initialize the dialog.
        Mening of defaultButton: 1=OK, 2=Cancel

        Arguments:
        ----------
            parent -- the parent window \n
            title -- the title of the dialog \n
            text -- the text to display \n
            size -- the size of the dialog (optional) \n
            variable -- the variable to store the input \n
            buttonWidth -- the width of the buttons \n
            size -- the size of the dialog (optional)

        """
        self.text     = text
        self.size     = size
        self.variable = variable
        self.buttonWidth   = buttonWidth
        self.defaultButton = defaultButton

        super().__init__(parent, title=title)

    
    def body(self, master: tk.Frame) -> tk.Misc | None:
        """Create the dialog body.

        Arguments:
        ----------
            master -- the parent frame

        Returns:
        --------
            the widget that should have initial focus or None
        """
        if self.size:
            # set the size of the dialog when it was given
            super().geometry(f"{self.size[0]}x{self.size[1]}")

        self.editorFaame = tk.Frame(self)
        self.editorFaame.pack(fill=tk.X, expand=True, side=tk.LEFT, padx=5, pady=5)
        self.resizable(False, False)

        self.text = tk.Label(self.editorFaame, text=self.text, anchor=tk.W, justify=tk.LEFT)
        self.text.grid(row=0, column=0, padx=5, pady=2, sticky=(tk.W, tk.E))  

        self.textEntry = tk.Entry(self.editorFaame, textvariable=self.variable, )
        self.textEntry.grid(row=1, column=0, padx=5, pady=2, sticky=(tk.W, tk.E))
        self.textEntry.bind("<Return>", self.OnOk)

        # reg = self.editorFaame.register(self.IntegerValidator)
        reg = self.editorFaame.register(self.FloatValidator)
        self.textEntry.config(validate="key", validatecommand=(reg, "%P", "%V"))
        self.textEntry.config(validate="focusout", validatecommand=(reg, "%P", "%V"))

        self.editorFaame.columnconfigure(0, weight=1)
        self.editorFaame.rowconfigure(0, weight=1)
        self.editorFaame.rowconfigure(1, weight=1)
        return self.textEntry
    

    def IntegerValidator(self, P, V) :
        """Validate the input as integer.
        """
        try:
            if P == "":
                return True
            int(P)
            return True
        except ValueError:
            return False


    def FloatValidator(self, P, V) :
        """Validate the input as float.
        """
        try:
            if P == "":
                return True
            float(P)
            return True
        except ValueError:
            return False       
         

    def buttonbox(self) :
        """Create the buttons.
        """
        buttonFrame = tk.Frame(self.editorFaame)
        buttonFrame.grid(row=2, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.S))

        defaultState = tk.ACTIVE if self.defaultButton == 2 else tk.NORMAL
        w = tk.Button(buttonFrame, text="Cancel", width=self.buttonWidth, command=self.OnCancel, default=defaultState)
        w.pack(side=tk.RIGHT, padx=5, pady=5)

        defaultState = tk.ACTIVE if self.defaultButton == 1 else tk.NORMAL
        w = tk.Button(buttonFrame, text="OK", width=self.buttonWidth, command=self.OnOk, default=defaultState)
        w.pack(side=tk.RIGHT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        return buttonFrame
    

    def OnOk(self, event=None) :
        """Handle the OK button.
        """
        self.result = self.textEntry.get()
        self.variable.set(self.result)
        self.ok()


    def OnCancel(self, event=None) :
        """Handle the Cancel button.
        """
        self.result = None
        self.cancel()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    variable = tk.StringVar(root, "It will be changed by the dialog.")
    dialog = TXInputBox(root, title="Input Box", text="Please enter your name:", buttonWidth=8, defaultButton=1, size=(300, 100), variable=variable)
    print(f"Dialog result: {dialog.result}")
    print(f"Result in the variable too: {variable.get()}")

