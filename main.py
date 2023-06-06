import tkinter as tk
from time import strftime

def set_light_theme():
    light_frame = tk.Frame(root, bg="white")
    light_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    light_label = tk.Label(light_frame, font=('calibri', 40, 'bold'), background='White', foreground='black')
    light_label.pack(anchor="s")

    def display_time():
        string = strftime('%I:%M:%S %p')
        light_label.config(text=string)
        light_label.after(1000, display_time)
    
    display_time()

def set_dark_theme():
    dark_frame = tk.Frame(root, bg="black")
    dark_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    dark_label = tk.Label(dark_frame, font=('calibri', 40, 'bold'), background='black', foreground='white')
    dark_label.pack(anchor="s")

    def display_time():
        string = strftime('%I:%M:%S %p')
        dark_label.config(text=string)
        dark_label.after(1000, display_time)
    
    display_time()

root = tk.Tk()
root.title("Digital-Clock")
canvas = tk.Canvas(root, height=140, width=400)
canvas.pack()

main_frame = tk.Frame(root, bg='black')
main_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
main_label = tk.Label(main_frame, font=('calibri', 40, 'bold'), background='black', foreground='white')
main_label.pack(anchor="s")

def display_time():
    string = strftime('%I:%M:%S %p')
    main_label.config(text=string)
    main_label.after(1000, display_time)

display_time()

menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Light", command=set_light_theme)
theme_menu.add_command(label="Dark", command=set_dark_theme)
menubar.add_cascade(label="Theme", menu=theme_menu)
root.config(menu=menubar)
root.mainloop()