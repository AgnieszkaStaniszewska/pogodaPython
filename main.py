# Aplikacja okienkowa do sprawdzania obecnie panującej pogody w dowolnym mieście na świecie
# Z wykorzystaniem OpenWeatherMap

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
import requests

# kierunek wiatru - konwertowanie stopni na oznaczenia N,E,W,S itd.
def get_cardinal_direction(degree):
    if 337.5 <= degree or degree < 22.5:
        return "N"
    elif 22.5 <= degree < 67.5:
        return "NE"
    elif 67.5 <= degree < 112.5:
        return "E"
    elif 112.5 <= degree < 157.5:
        return "SE"
    elif 157.5 <= degree < 202.5:
        return "S"
    elif 202.5 <= degree < 247.5:
        return "SW"
    elif 247.5 <= degree < 292.5:
        return "W"
    elif 292.5 <= degree < 337.5:
        return "NW"

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Nazwa okna apki
        self.setWindowTitle("Pogoda")

        # Położenie i rozmiar okna aplikacji
        self.setGeometry(750, 250, 400, 200)

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Widgety
        self.city_label = QLabel("Wpisz miasto:")
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton("Pokaż pogodę")
        self.weather_label = QLabel("")

        # Łączenie layoutu z widgetami
        self.layout.addWidget(self.city_label)
        self.layout.addWidget(self.city_input)
        self.layout.addWidget(self.get_weather_button)
        self.layout.addWidget(self.weather_label)

        # Funkcjonalność buttonu "Pokaż pogodę"
        self.get_weather_button.clicked.connect(self.get_weather)



    def get_weather(self):

        # Podanie nazwy miasta z klawiatury
        city = self.city_input.text()

        # Dostęp do danych z OpenWeather Map i tłumaczenie ich na język polski
        api_key = "267abe621357d2e573d21ae50e8ccc4e"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pl"
        response = requests.get(url)

        # Pobieranie danych z serwisu j.w.
        weather_data = response.json()
        print(weather_data)  # Sprawdzamy czy coś pobiera, czy jest jakiś błąd

        # Przypisanie danych do zmiennych
        temperature = round(weather_data["main"]["temp"] - 273.15, 1) #konwertowanie temp na stopnie celsjusza i zaokrąglenie do 1 miejsca po przecinku
        pressure = weather_data["main"]["pressure"]
        wind_speed = weather_data["wind"]["speed"]
        wind_direction = get_cardinal_direction(weather_data["wind"]["deg"])
        description = weather_data["weather"][0]["description"]

        # Wyświetlenie na ekran
        self.weather_label.setText(f"Temperatura: {temperature}°C\nCiśnienie: {pressure} hPa\nSiła wiatru: {wind_speed} m/s\nKierunek wiatru: {wind_direction}\nZachmurzenie: {description}")


if __name__ == "__main__":
    app = QApplication([])
    get_weather = WeatherApp()
    get_weather.show()
    app.exec_()
