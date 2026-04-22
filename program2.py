import tkinter as tk
import tkinter.messagebox as mbox

class MYGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Joe\'s automotive')
        self.main_window.geometry('500x500')

        # heading
        heading = tk.Label(self.main_window, text='Joe\'s automotive\n which services would you like?')
        heading.pack()

        # variables
        self.oil_var = tk.IntVar()
        self.lube_var = tk.IntVar()
        self.radiator_var = tk.IntVar()
        self.transmission_var = tk.IntVar()
        self.inspection_var = tk.IntVar()
        self.muffler_var = tk.IntVar()
        self.tire_var = tk.IntVar()

        # Oil Change
        self.oil_change = tk.Checkbutton (self.main_window, text = 'Oil Change- $30.00', variable = self.oil_var, command = self.show_total)
        self.oil_change.pack(pady=5)

        # Lube Job
        self.lube_job = tk.Checkbutton (self.main_window, text = 'Lube Job- $20.00', variable = self.lube_var, command = self.show_total)
        self.lube_job.pack(pady=5)

        # radiator flush
        self.radiator_flush = tk.Checkbutton (self.main_window, text = 'Radiator Flush- $40.00', variable = self.radiator_var, command = self.show_total)
        self.radiator_flush.pack(pady=5)

        # transmission Fluid
        self.transmission_fluid = tk.Checkbutton (self.main_window, text = 'Transmission Fluid- $100.00', variable = self.transmission_var, command = self.show_total)
        self.transmission_fluid.pack(pady=5)

        # inspection
        self.inspection = tk.Checkbutton (self.main_window, text = 'Inspection- $35.00', variable = self.inspection_var, command = self.show_total)
        self.inspection.pack(pady=5)

        # muffler replacement
        self.muffler_replacement = tk.Checkbutton (self.main_window, text = 'Muffler Replacement- $200.00', variable = self.muffler_var, command = self.show_total)
        self.muffler_replacement.pack(pady=5)

        # tire rotation
        self.tire_rotation = tk.Checkbutton (self.main_window, text = 'Tire Rotation- $20.00', variable = self.tire_var, command = self.show_total)
        self.tire_rotation.pack(pady=5)

        # total title label
        self.total_title_label = tk.Label(self.main_window, text='Total:')
        self.total_title_label.pack(pady=20)

        # total label
        self.total_label = tk.Label(self.main_window, text='$0.00')
        self.total_label.pack(pady=5)

        # quit button
        quit_button = tk.Button(self.main_window, text = 'exit', command = self.main_window.destroy)
        quit_button.pack(pady=15, side = 'bottom')
        
        self.main_window.mainloop()

#     show total
    def show_total(self):
        total = 0
        if self.oil_var.get():
            total += 30
        if self.lube_var.get():
            total += 20
        if self.radiator_var.get():
            total += 40
        if self.transmission_var.get():
            total += 100
        if self.inspection_var.get():
            total += 35
        if self.muffler_var.get():
            total += 200
        if self.tire_var.get():
            total += 20
        self.total_label.config(text=f'Total: ${total:.2f}')


if __name__ == '__main__':
    app = MYGUI()

