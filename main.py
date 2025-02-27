import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

# my_label['text'] = 'Cool New Text'
# my_label.config(text="Cool New Text")

# Button

def button_click(): 
    new_text = input.get()
    my_label.config(text=new_text)

button =tkinter.Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

def button_click(): 
    new_text = input.get()
    my_label.config(text=new_text)

button =tkinter.Button(text="Click Me", command=button_click)
button.grid(column=2, row=0)


#Entry 

input = tkinter.Entry(width=10)
input.grid(column = 3, row = 2)

window.mainloop()    