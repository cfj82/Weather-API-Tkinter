

import tkinter as tk
import json


# create GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("420x220")
root.configure(bg="grey")

def get_weather():
    #api_key = 4b998c307c856e851c23f08fdd34f945
    pass




def clear():
    city_etr.delete(0, END)
    temp_etr.delete(0, END)
    hum_etr.delete(0, END)



# labels
city_lbl = tk.Label(root, font=("Helvetica", 15), text="Enter City")
temp_lbl = tk.Label(root, font=("Helvetica", 15), text="Temperature: ")
hum_lbl = tk.Label(root, font=("Helvetica", 15), text="Humidity: ")

# buttons
tell_btn = tk.Button(root, font=("verdana", 12), anchor="center", relief='raised', border=6,
                 bg="#5DADE2", text="Get the Weather", command=get_weather)
clr_btn = tk.Button(root, font=("verdana", 12), anchor="center", relief='raised', border=6,
                 bg="#5DADE2", text="Clear", command=clear)

# entry
city_etr = tk.Entry(root, font=("verdana", 15), relief='ridge', border=6, justify="center",
              bg="#744697", )
temp_etr = tk.Entry(root)
hum_etr = tk.Entry(root)

# .grid
city_lbl.grid(row=0, column=0, pady=5)
city_etr.grid(row=0, column=1, pady=5)
tell_btn.grid(row=1, column=0, columnspan=2, pady=5)
temp_lbl.grid(row=2, column=0, padx=5)
temp_etr.grid(row=2, column=1, padx=5)
hum_lbl.grid(row=3, column=0, padx=5)
hum_etr.grid(row=3, column=1, padx=5)
clr_btn.grid(row=4, column=0, columnspan=2, pady=5, padx=5)


# create menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# create menu drop down
option_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=option_menu)

option_menu.add_command(label='Clear All', command=clear)
option_menu.add_separator()  # adds line to separate
option_menu.add_command(label='Quit', command=root.quit)

root.mainloop()
