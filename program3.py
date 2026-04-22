import tkinter as tk
import tkinter.messagebox as mbox



class MYGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.configure()
        self.main_window.title('long distance calls')
        self.main_window.geometry('500x350')

        # heading
        self.label = tk.Label(self.main_window, text = 'please select the time of your call')
        self.label.pack()

        # int_var object
        self.radio_var = tk.IntVar()

        # set int_var to 1
        self.radio_var.set(1)

        # make radio button widgets
        self.rb1 = tk.Radiobutton(text = 'Daytime (6:00 A.M. through 5:59 P.M.) - $0.02', variable = self.radio_var, value=1)
        self.rb1.pack(pady = 10)
        self.rb2 = tk.Radiobutton(text = 'Evening (6:00 P.M.  through 11:59 P.M.) - $0.12', variable = self.radio_var, value=2)
        self.rb2.pack(pady = 10)
        self.rb3 = tk.Radiobutton(text = 'Off-Peak (midnight through 5:59 P.M.) - $0.05', variable = self.radio_var, value=3)
        self.rb3.pack(pady = 10)

        # make label for entry widget
        self.entry_label = tk.Label(text = 'Please enter the length of your call in minutes')
        self.entry_label.pack()

        # make entry widget
        self.get_call_minutes = tk.Entry(self.main_window, highlightcolor = 'white', highlightthickness = 5)
        self.get_call_minutes.pack()
        self.get_call_minutes.pack(pady = 10)

        # calculate button
        self.calculate_button = tk.Button(self.main_window, text = 'calculate price', command = self.calculate_price)
        self.calculate_button.pack(pady = 10)

        # quit
        self.quit = tk.Button(self.main_window, text = 'quit', command = self.main_window.destroy)
        self.quit.pack(side = 'bottom')

        self.main_window.mainloop()

    def calculate_price(self):
        try:
            minutes = float(self.get_call_minutes.get())

            if self.radio_var.get() == 1:
                rate = 0.02
            elif self.radio_var.get() == 2:
                rate = 0.12
            else:
                rate = 0.05

            charge = minutes * rate

            mbox.showinfo('total charge', f'the total cost of your call is: {charge:.2f}')

        except ValueError:
            mbox.showerror('error', 'please enter a number')






if __name__ == '__main__':
    app = MYGUI()
