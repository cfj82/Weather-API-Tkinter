# https://openweathermap.org/current#current_JSON

import tkinter as tk
import json
import requests


def get_weather(event):
    api_key = '4b998c307c856e851c23f08fdd34f945'
    website = 'http://api.openweathermap.org/data/2.5/find?q='
    # .get from entry
    city_name = city_etr.get()
    # api format:
    # api.openweathermap.org/data/2.5/find?q=London&units=imperial
    api_call = website + city_name + '&units=imperial&appid=' + api_key
    # call api by request
    response = requests.get(api_call)

    if response.status_code == 200:
        # json format data
        info = response.json()
        temp_display.config(text=(str(info["list"][0]["main"]["temp"]) + " deg F"))
        maxt_display.config(text=(str(info["list"][0]["main"]["temp_max"]) + " deg F"))
        mint_display.config(text=(str(info["list"][0]["main"]["temp_min"]) + " deg F"))
        description_display.config(text=info["list"][0]["weather"]["description"])  # todo fix typeError: list indices must be integers or slices, not str

    else:
        weather_lbl.config(text="Error:"+str(response.status_code))  # print response code if error


def clear():  # clear all fields
    city_etr.delete(0, tk.END)
    temp_display.config(text="-")
    maxt_display.config(text="-")
    mint_display.config(text="-")
    description_display.config(text="-")

if __name__=="__main__":
    # create GUI
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("450x340")
    root.configure(bg="grey")

    # labels
    weather_lbl = tk.Label(root, font=("Helvetica", 20),  bg='grey', text="---- Weather ----")
    city_lbl = tk.Label(root, font=("Helvetica", 15),  bg='grey', text="Enter City")
    temp_lbl = tk.Label(root, font=("Helvetica", 15),  bg='grey', text="Temperature: ")
    maxt_lbl = tk.Label(root, font=("Helvetica", 15),  bg='grey', text="Max Temperature: ")
    mint_lbl = tk.Label(root, font=("Helvetica", 15),  bg='grey', text="Min Temperature: ")
    description_lbl = tk.Label(root, font=("Helvetica", 15),  bg='grey', text="Description: ")

    # buttons
    tell_btn = tk.Button(root, font=("verdana", 12), anchor="center", relief='raised', border=6,
                     bg="#5DADE2", text="Get the Weather", command=get_weather)
    tell_btn.bind('<Button-1>', get_weather)   # button bind and enter
    clr_btn = tk.Button(root, font=("verdana", 12), anchor="center", relief='raised', border=6,
                     bg="#5DADE2", text="Clear", command=clear)

    # entry
    city_var=tk.StringVar()
    city_etr = tk.Entry(root, font=("verdana", 15), relief='ridge', border=6, justify="center",
                  bg="#744697", width=17, textvariable=city_var)
    city_etr.bind('<Return>', get_weather)  # button bind and enter


    city_etr.focus()  # focus when open gui
    temp_display = tk.Label(root, font=("verdana", 15), relief='flat', bg='grey', text='-')
    maxt_display = tk.Label(root, font=("verdana", 15), relief='flat', bg='grey', text='-')
    mint_display = tk.Label(root, font=("verdana", 15), relief='flat', bg='grey', text='-')
    dec_display=tk.StringVar()
    dec_display.set("-")
    description_display = tk.Label(root, font=("verdana", 15), relief='flat', bg='grey', textvariable=dec_display)

    # .grid
    weather_lbl.grid(row=0, column=0, columnspan=2, pady=5)
    city_lbl.grid(row=1, column=0, pady=5)
    city_etr.grid(row=1, column=1, pady=5)
    tell_btn.grid(row=2, column=0, columnspan=2, pady=5)
    temp_lbl.grid(row=3, column=0, padx=5)
    temp_display.grid(row=3, column=1, padx=5)
    maxt_lbl.grid(row=4, column=0, padx=5)
    maxt_display.grid(row=4, column=1, padx=5)
    mint_lbl.grid(row=5, column=0, padx=5)
    mint_display.grid(row=5, column=1, padx=5)
    description_lbl.grid(row=6, column=0, padx=5)
    description_display.grid(row=6, column=1, padx=5)
    clr_btn.grid(row=7, column=0, columnspan=2, pady=5, padx=5)


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
