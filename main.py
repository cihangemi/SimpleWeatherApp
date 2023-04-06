from tkinter import *
from PIL import ImageTk,Image
import requests
from getweather import getWeather

icons="https://openweathermap.org/img/wn/{}@2x.png"


def run():
    city=cityEntry.get()
    weather= getWeather(city)
    if weather:
        locationLabel['text']='{},{}'.format(weather[0],weather[1])
        tempLabel['text']= '{}°C'.format(weather[2])
        conditionLabel['text']=weather[4]
        icon=ImageTk.PhotoImage(Image.open(requests.get(icons.format(weather[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon


app = Tk()
app.geometry('300x450')
app.title("Hava Durumu")


cityEntry= Entry(app,justify='center')
cityEntry.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cityEntry.focus()

searchButton = Button(app,text="Arama",font=('Arial',15),command=run)
searchButton.pack(fill=BOTH,ipady=20,padx=20)

iconLabel= Label(app)
iconLabel.pack()

locationLabel = Label(app,font=('Arial',35))
locationLabel.pack()

tempLabel=Label(app,font=('Arial',50))
tempLabel.pack()

conditionLabel = Label(app,font=('Arial',20))
conditionLabel.pack()

app.mainloop()




