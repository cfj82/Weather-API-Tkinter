# https://openweathermap.org/current#current_JSON

import tkinter as tk
import json
import requests

"""dictionary from OpenWeather.org
 {
"coord": {"lon": -0.13,"lat": 51.51},
"weather": [{"id": 300, "main": "Drizzle", 
"description": "light intensity drizzle", "icon": "09d"}],
"base": "stations",
"main": {"temp": 280.32,"pressure": 1012,"humidity": 81,"temp_min": 279.15,"temp_max": 281.15},
"visibility": 10000,
"wind": {"speed": 4.1,"deg": 80},
"clouds": {"all": 90},
"dt": 1485789600,
"sys": {"type": 1,"id": 5091,"message": 0.0103,"country": "GB","sunrise": 1485762037,"sunset": 1485794875},
"id": 2643743,
"name": "London",
"cod": 200
}
"""
# dict for imperial units
"""
{
   "message":"accurate",
   "cod":"200",
   "count":1,
   "list":[
      {
         "id":2643743,
         "name":"London",
         "coord":{
            "lat":51.5085,
            "lon":-0.1258
         },
         "main":{
            "temp":7,
            "pressure":1012,
            "humidity":81,
            "temp_min":5,
            "temp_max":8
         },
         "dt":1485791400,
         "wind":{
            "speed":4.6,
            "deg":90
         },
         "sys":{
            "country":"GB"
         },
         "rain":null,
         "snow":null,
         "clouds":{
            "all":90
         },
         "weather":[
            {
               "id":701,
               "main":"Mist",
               "description":"mist",
               "icon":"50d"
            },
            {
               "id":300,
               "main":"Drizzle",
               "description":"light intensity drizzle",
               "icon":"09d"
            }
         ]
      }
   ]
  }
"""

def get_weather(event):
    api_key = '4b998c307c856e851c23f08fdd34f945'
    website = 'http://api.openweathermap.org/data/2.5/find?q='
    # .get from entry
    city_name = city_etr.get()
    # api format:
    # api.openweathermap.org/data/2.5/find?q=London&units=imperial
    api_call = website + city_name + '&units=imperial' + api_key
    # call api by request
    response = requests.get(api_call)

    if response.status_code != '404':
        # json format data
        info = response.json()
        temp_display.config(text=info['cod'])
    #    maxt_display.config(text=info )
    #    mint_display.config(text=info )
    #    description_display.config(text=info )

    else:
        weather_lbl.config(text="Error:"+str(response.status_code))  # print response code if error


def clear():
    pass
    weather_lbl.config(text="-")
    city_lbl.config(text="-")
    temp_lbl.config(text="-")
    maxt_lbl.config(text="-")
    mint_lbl.config(text="-")
    description_lbl.config(text="-")

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
    clr_btn = tk.Button(root, font=("verdana", 12), anchor="center", relief='raised', border=6,
                     bg="#5DADE2", text="Clear", command=clear)

    # entry
    city_etr = tk.Entry(root, font=("verdana", 15), relief='ridge', border=6, justify="center",
                  bg="#744697", width=17)
    city_etr.bind('<Return>', get_weather)
    city_etr.focus()  # focus when open gui
    temp_display = tk.Label(root, font=("verdana", 15), relief='flat', bg='grey', text='-')
    maxt_display = tk.Label(root, font=("verdana", 15), relief='flat', bg='grey', text='-')
    mint_display = tk.Label(root, font=("verdana", 15), relief='flat', bg='grey', text='-')
    description_display = tk.Label(root, font=("verdana", 15), relief='flat', bg='grey', text='-')

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
