from tkinter import *

def search():
    pass

app  = Tk()
app.title("WEATHER-app")
app.geometry('700x300')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='search weather', width=12, command= search)
search_btn.pack()

locaction_label = Label(app, text='Location', font=('bold',20))
locaction_label.pack()

image = Label(app, bitmap='')
image.pack()

temperature_label = Label(app, text='temperature')
temperature_label.pack()

weather_label = Label(app, text='weather')
weather_label.pack()




app.mainloop()