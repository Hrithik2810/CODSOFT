import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from tkinter import ttk, messagebox

root = tk.Tk()
root.title('Weather App')
root.geometry("900x500+300+100")
root.resizable(0, 0)

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def showWeather():
    try:
        city_name = textfield.get()

        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(city_name)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api_key = "24926d658f05cb73bca5d53452db261a"
        weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
        json_data = requests.get(weather_url).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        timezone = json_data['timezone']
        sunrise = json_data['sys']['sunrise']
        sunset = json_data['sys']['sunset']
        cloudy = json_data['clouds']['all']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        t.config(text=(temp, '°C'))
        c.config(text=('Description:',condition, "|","Temprature:",temp, "°C"),fg="#0047AB")
        r.config(text=('Sunrise:',sunrise_time),fg="#008080")
        s.config(text=('Sunset:',sunset_time),fg="#008080")
        cl.config(text=('Cloud:',cloudy),fg="#0047AB")

        w.config(text=wind)
        H.config(text=humidity)
        P.config(text=pressure)
        D.config(text=description)
    except:
        messagebox.showerror("Weather App", "Invalid City Entry!!")

# Search box
Search_box = tk.PhotoImage(file="searchbox.png")
myimage = tk.Label(image=Search_box)
myimage.place(x=200, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="White")
textfield.place(x=270, y=40)
textfield.focus()

Search_icon = tk.PhotoImage(file="Searchicon.png")
myimage_icon = tk.Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", border=0, background="#404040", command=showWeather)
myimage_icon.place(x=575, y=34)

# Weather logo
Weather_logo = tk.PhotoImage(file="Weathericon.png")
logo = tk.Label(image=Weather_logo)
logo.place(x=250, y=135)

# Box
box_image = tk.PhotoImage(file="box.png")
box = tk.Label(image=box_image)
box.pack(side=tk.BOTTOM)

# Time
name = tk.Label(root, font=('Consolas', 25, 'bold'),fg="#023020")
name.place(x=30, y=100)
clock = tk.Label(root, font=('Comic Sans MS', 15),fg='#36454F')
clock.place(x=30, y=140)

# Labels for weather details
detail1 = tk.Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg='white', bg="#1ab5ef")
detail1.place(x=120, y=402)

detail2 = tk.Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg='white', bg="#1ab5ef")
detail2.place(x=250, y=402)

detail3 = tk.Label(root, text="OVERALL", font=("Helvetica", 15, "bold"), fg='white', bg="#1ab5ef")
detail3.place(x=440, y=402)

detail4 = tk.Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg='white', bg="#1ab5ef")
detail4.place(x=660, y=402)

# Labels for weather details values
t = tk.Label(root, font=('arial', 70, 'bold'), fg='Red')
t.place(x=500, y=150)
c = tk.Label(root, font=('arial', 15, 'bold'))
c.place(x=500, y=250)
cl = tk.Label(root, font=('arial', 15, 'bold'))
cl.place(x=500, y=280)
r = tk.Label(root, font=('arial',15,'bold'))
r.place(x=30,y=250)
s = tk.Label(root, font=('arial',15,'bold'))
s.place(x=30,y=275)

w = tk.Label(root, text=".....", font=('arial', 20, 'bold'), bg="#1ab5ef")
w.place(x=120, y=430)

H = tk.Label(root, text=".....", font=('arial', 20, 'bold'), bg="#1ab5ef")
H.place(x=250, y=430)

D = tk.Label(root, text=".....", font=('arial', 20, 'bold'), bg="#1ab5ef")
D.place(x=440, y=430)

P = tk.Label(root, text=".....", font=('arial', 20, 'bold'), bg="#1ab5ef")
P.place(x=660, y=430)

root.mainloop()
