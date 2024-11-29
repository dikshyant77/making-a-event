from tkinter import *
window=Tk()
window.title("event handler")
window.geometry("100x100")

def handle_keypress(event):
    """print the character asscoited with the keypress"""
    print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
    print("the button was clicked")
button=Button(text="click me")
button.pack()
button.bind("<Button>",handle_click)
window.mainloop()