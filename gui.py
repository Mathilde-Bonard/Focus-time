from tkinter import *
from functions import app_block
from config import process_name

def click():
    minutes = entry.get()
    app_block(minutes, process_name)

window = Tk()

# Customize background and text color here
bg_color_custom = '#ec785f'
text_color_custom = 'white'
other_color_custom = '#89220d'
# Green version : bg_color_custom = '#b8e994'

#Customize fonts here
main_font_custom = 'Super Adorable'
sec_font_cutom = 'Calibri'

# Window parameters
window.title("Focus")
window.geometry("720x480")
window.minsize(480,360)
window.iconbitmap("tomate.ico")
window.config(background=bg_color_custom)

# Frame
frame = Frame(window, bg=bg_color_custom)

# Title
title_label = Label(frame, 
    text = "Focus Time !", 
    font=(main_font_custom, 40), 
    bg=bg_color_custom,
    fg=text_color_custom)
title_label.pack(pady= 40)

# Entry instructions
entry_label = Label(frame,
    text = "How long do you want to ONLY code ?", 
    font=(sec_font_cutom, 20), 
    bg=bg_color_custom,
    fg=text_color_custom)
entry_label.pack()

# Entry
entry = Entry(frame,
    font=(sec_font_cutom, 20),
    fg=other_color_custom,
    justify= "center")
entry.config(font="bold")
entry.pack(pady= 15)
entry.focus()

# Start button
start_button = Button(frame,
    text="Start",
    font=(main_font_custom, 25),
    bg=text_color_custom,
    fg=bg_color_custom,
    command=click)
start_button.pack(pady= 40)

# Add frame
frame.pack(expand=YES)

# Window display
window.mainloop()
