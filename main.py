from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

color_bone = "#A47E3B"
color_dark_blue = "#1B2430"

def create_image():
    global i
    profileimage = filedialog.askopenfilename()
    i = ImageTk.PhotoImage(Image.open(profileimage))
    canvas.create_image(0,0,image=i)
    


window = Tk()
window.title("WaterMaker")
window.config(padx=100, pady=50, bg=color_bone)
# Canvas Image
image = PhotoImage(file="Signature.png")
canvas = Canvas(width=400, height=424, bg=color_bone, highlightthickness=0)
canvas.create_image(202, 212, image=image)
canvas.grid(column=1, row=1)
# Title Label
label = Label(text="WaterMarker", fg=color_dark_blue, bg=color_bone, font=("Helvetica", 50, "bold"))
label.grid(column=1, row=0)
# Button
start_button = Button(width=57,text="START",fg=color_bone, bg=color_dark_blue, command=create_image)
start_button.grid(column=1, row=2)



window.mainloop()