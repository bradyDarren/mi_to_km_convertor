import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.pack()

# my_label['text'] = 'Cool New Text'
# my_label.config(text="Cool New Text")

# Button

def button_click(): 
    my_label.config(text="Button Got Clicked")

button =tkinter.Button(text="Click Me", command=button_click)
button.pack()

#Entry 

input = tkinter.Entry()
input.pack()


window.mainloop()    