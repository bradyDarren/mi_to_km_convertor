from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

kilometer_results_label = Label(text= '0')
kilometer_results_label.grid(column= 1, row= 1)

kilometer_label = Label(text='Km')
kilometer_label.grid(column=2, row=1)
 
def button_clicked(): 
    miles = float(miles_input.get())
    kilometer = miles * 1.609
    kilometer_results_label.config(text=f'{kilometer}')

calculate_button = Button(text = 'Calculate', command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()