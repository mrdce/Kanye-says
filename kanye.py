import tkinter
import requests


def get_quote():
    new_quote = requests.get(url='https://api.kanye.rest')
    new_quote.raise_for_status()
    canvas.itemconfig(quote, text=new_quote.json()['quote'])


window = tkinter.Tk()
window.title('Kanye says:')
window.config(padx=20, pady=50)

canvas = tkinter.Canvas(width=300, height=430)

image = tkinter.PhotoImage(file='background.png')
canvas.create_image(150, 207, image=image)
quote = canvas.create_text(150, 190, text='Just stop lying about shit. Just stop lying.', font=('Arial', 16, 'bold'), width=280)
canvas.grid(column=0, row=0)

refresh_image = tkinter.PhotoImage(file='kanye.png')
button = tkinter.Button(image=refresh_image, highlightthickness=0, borderwidth=0, command=get_quote)
button.grid(column=0, row=1)

window.mainloop()
