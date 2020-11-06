"""
        BASE CONVERTER USER INTERFACE

"""

from tkinter import messagebox
from tkinter import *
from tkinter import ttk



class Converter:

    def __init__(self, master):
        super().__init__()
        self.initUI(master)
    
    def initUI(self, master):

    #/---------------------------------Master and Frame--------------------------------/    

        self.master = master
        master.geometry("480x540")
        master.title("Base Converter")

        self.frame = Frame(master, bg="papaya whip")
        self.frame.pack(fill=BOTH, expand=True)

    #/------------------------------------Labels------------------------------------/

        self.enter_number = Label(self.frame, text="Enter Number: ", font=("helvetica 15"), bg="papaya whip")
        self.enter_number.place(x=80, y=80)

        self.from_base = Label(self.frame, text="From Base: ", font=("helvetica 15"), bg="papaya whip")
        self.from_base.place(x=80, y=140)

        self.to_base = Label(self.frame, text="To Base: ", font=("helvetica 15"), bg="papaya whip")
        self.to_base.place(x=80, y=200)

        self.result = Label(self.frame, text="Result: ", font=("helvetica 15"), bg="papaya whip")
        self.result.place(x=80, y=350)

    #/----------------------------------Button------------------------------------/

        self.convert_button = Button(self.frame, width=10, text="Convert", font=("helvetica 10"), bd=3, comman=self.add_result)
        self.convert_button.place(x=120, y=280)

        self.reset_button = Button(self.frame, width=10, text="Reset", font=("helvetica 10"), bd=3, comman=self.reset)
        self.reset_button.place(x=250, y=280)

    #/-----------------------------------Entries-------------------------------------/

        self.number_entry = Entry(self.frame, width=16, font=("helvetica 12"))
        self.number_entry.place(x=240, y=82)

        self.result_entry = Entry(self.frame, width=16, font=("helvetica 12"))
        self.result_entry.place(x=240, y=352)


        self.box_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

        self.from_base_text = StringVar()
        self.from_base_text.set("From Base")
        self.from_base_box = ttk.Combobox(self.frame, width = 15, values=self.box_list, textvariable=self.from_base_text, state="readonly", font="verdana 10")
        self.from_base_box.place(x=240, y=142)

        self.to_base_text = StringVar()
        self.to_base_text.set("To Base")
        self.to_base_box = ttk.Combobox(self.frame, width = 15, values=self.box_list, textvariable=self.to_base_text, state="readonly", font="verdana 10")
        self.to_base_box.place(x=240, y=202)

    #/-----------------------------------------Functions---------------------------------------/

    def convert_to_decimal(self):

        self.check_valid = True
        self.digit_list = [int(digits) for digits in (sorted(set(list(str(self.number_entry.get())))))]

        for index in self.digit_list:
            if index >= int(self.from_base_box.get()):
                self.check_valid = False
    
        if self.check_valid == True:
            self.result = 0
            self.length = len(str(self.number_entry.get())) - 1

            for num in str(self.number_entry.get()):
                self.result  += int(num) * (int(self.from_base_box.get()) ** self.length)
                self.length -= 1
            return self.result

        elif self.check_valid == False:
            return "invalid number"

    def convert_from_decimal(self): 

        self.number1 = self.convert_to_decimal()
        self.stack = []
        self.hex_dict = {10 : 'A' , 11 : 'B' , 12 : 'C' , 13 : 'D' , 14 : 'E' , 15 : 'F'}

        if self.convert_to_decimal() == "invalid number":
            messagebox.showinfo("invalid number", "invalid number !")
            self.result_entry.delete(0, END)
            self.number_entry.delete(0, END)

        else:

            while self.number1 > 0:
                self.reminder = self.number1 % int(self.to_base_box.get())
                self.number1 = self.number1 // int(self.to_base_box.get())
                self.stack.append(self.reminder)

            self.stack = self.stack[::-1]

            if int(self.to_base_box.get()) > 10:
                for index in range(len(self.stack)):
                    for key, value in self.hex_dict.items():
                        if self.stack[index] == key:
                            self.stack[index] = value

            return "".join([str(i) for i in self.stack])

    def add_result(self):

        self.result_entry.insert(END, str(self.convert_from_decimal()))
    

    def reset(self):

        self.number_entry.delete(0, END)
        self.result_entry.delete(0, END)
        self.from_base_box.set("From Base")
        self.to_base_box.set("To Base")


def main():

    tk = Tk()
    tk.resizable(False, False)
    ConverterApp = Converter(tk)
    tk.mainloop()

if __name__ == "__main__":

    main()