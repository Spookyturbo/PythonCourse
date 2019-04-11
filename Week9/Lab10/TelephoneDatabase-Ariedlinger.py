#Telephone Database
#Andrew Riedlinger
#April 4th, 2019
#
#An interface for a teleophone database

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Command selection
        Label(self, text = "Command:"
              ).grid(row = 0, column = 0, sticky = W)

        self.selected_command = StringVar()
        self.selected_command.set(None)
        commands = ("Find", "Insert", "Delete")
        column = 1
        for command in commands:
            Radiobutton(self, text = command, variable = self.selected_command,
                        value = command
                        ).grid(row = 0, column = column)
            column += 1
            
        #Name input
        Label(self, text = "Name: "
              ).grid(row = 1, column = 0)
        self.name_entry = Entry(self, width = 40)
        self.name_entry.grid(row = 1, column = 1, columnspan = 3)

        #Address Input
        Label(self, text = "Address/Phone"
              ).grid(row = 3, column = 0, sticky = W)
        self.address_text = Text(self, width = 40, height = 5, wrap = WORD)
        self.address_text.grid(row = 3, column = 1, columnspan = 3)
        

def main():
    root = Tk()
    root.title("Telephone Databse")
    root.geometry("400x200")
    app = Application(root)
    root.mainloop()

main()
    
