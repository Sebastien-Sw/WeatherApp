# Weather App in Python
# "weather app.py"


# Replace Emoji Label with PushButton
# Add image to pushbutton
# Add check the weather button to the push button

# Add a settings menu
# Light/Dark mode
# Add ability to add country or postcode
# C / F


# Colour Scheme :
#   Primary : hsl(218, 72%, 45%)
#   Accent : hsl(13, 81%, 61%)
#   Text Main : hsl(45, 29%, 97%)
#   Text Alternate : hsl(218, 20%, 23%)

import webbrowser
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QPixmap

class Weather_App(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowIcon(QIcon("D:/Python/Weather App/App Icon Day.png"))
        self.setGeometry(725, 150, 450, 800)
        self.city_label = QLabel("Enter city name : ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Check Weather")
        self.temperature_label = QLabel(self)
        self.weather_image = QPushButton(self)
        self.description_label = QLabel(self)
        self.settings_button = QPushButton("Settings")
        self.initUI()

    def initUI(self) :
        self.setWindowTitle("Weather App")

        # City Label Font
        Ubuntu_Bold_Italic = QFont("Ubuntu Regular", 30, QFont.Bold, True)
        self.city_label.setFont(Ubuntu_Bold_Italic)

        # City Input Font
        Ubuntu = QFont("Ubuntu", 28)
        self.city_input.setFont(Ubuntu)

        # Get Weather Button Font
        Ubuntu_Bold = QFont("Ubuntu Regular", 17, QFont.Bold)
        self.get_weather_button.setFont(Ubuntu_Bold)
        self.settings_button.setFont(Ubuntu_Bold)

        # Temperature Label Font
        Ubuntu_Bold_Bigger = QFont("Ubuntu Regular", 50, QFont.Bold)
        self.temperature_label.setFont(Ubuntu_Bold_Bigger)

        # Description Label Font
        Ubuntu_Medium = QFont("Ubuntu Medium", 25)
        self.description_label.setFont(Ubuntu_Medium)

        # Main Layout for the App
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Layout for the city label and city input
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.city_label)
        vbox1.addWidget(self.city_input)
        main_layout.addLayout(vbox1)

        # Layout for the get weather button
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.get_weather_button)
        main_layout.addLayout(hbox1)

        # Layout for the temperature label
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.temperature_label)
        main_layout.addLayout(vbox2)

        # Layout for the emoji label
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.weather_image)
        main_layout.addLayout(hbox2)

        # Layout for description label
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.description_label)
        main_layout.addLayout(vbox3)

        # Layout for settings label
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.settings_button)
        main_layout.addLayout(hbox3)

        main_layout.setContentsMargins(15, 20, 15, 15)
        main_layout.setSpacing(15)

        # Aligns all elements Vertically
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.description_label.setObjectName("description_label")

        # Image for Weather Display
        image_icon = QIcon()
        self.weather_image.setIcon(image_icon)
        button_size = QSize(180, 180)
        self.weather_image.setIconSize(button_size)
        self.weather_image.hide()


        # Styling
        self.setStyleSheet("""
                    background-color : hsl(45, 29%, 97%) ;
            """)

        self.city_label.setFixedHeight(100)
        self.city_label.setStyleSheet("""
            background-color : hsl(218, 72%, 52%) ;
            padding : 20px ;
            border-radius : 15px ;
            color : hsl(45, 29%, 97%) ;
            """)

        self.city_input.setStyleSheet("""
            color : hsl(218, 20%, 23%) ;
            border : 3px solid blue ;
            border-color : hsl(218, 72%, 55%) ;
            border-radius : 15px ;
            background-color : hsl(218, 72%, 90%) ;
            padding : 10px ;
            """)

        self.get_weather_button.setFixedWidth(300)
        self.get_weather_button.setStyleSheet("""
            color : hsl(45, 29%, 97%) ;
            padding : 10px ;
            border : 3px solid orange ;
            border-color : hsl(13, 81%, 61%) ;
            border-radius : 15px ;
            background-color : hsl(13, 81%, 61%) ;
            text-align : center ;
            """)

        self.temperature_label.setStyleSheet("""
            color : hsl(218, 20%, 23%) ;
            """)

        self.weather_image.setFixedWidth(200)
        self.weather_image.setFixedHeight(200)
        self.weather_image.setStyleSheet("""
            text-align : center ;
            """)

        self.description_label.setStyleSheet("""
            color : hsl(218, 20%, 23%) ;
            """)

        self.settings_button.setStyleSheet("""
            color : hsl(45, 29%, 97%) ;
            padding : 10px ;
            border : 3px solid orange ;
            border-color : hsl(13, 81%, 61%) ;
            border-radius : 15px ;
            background-color : hsl(13, 81%, 61%) ;
            text-align : center ;
            """)


        self.get_weather_button.clicked.connect(self.get_weather)

        self.weather_image.clicked.connect(self.further_weather)

    def get_weather(self) :
        api_key = "5c9b15efd16228987a83e6e3f992d894"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try :
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200 :
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error :
            match response.status_code :
                case 400 :
                    self.display_error("Bad request :\nPlease check your input")
                case 401 :
                    self.display_error("Unauthorised :\nInvalid API key")
                case 403 :
                    self.display_error("Forbidden :\nAccess is denied")
                case 404 :
                    self.display_error("Not Found :\nCity not found")
                case 500 :
                    self.display_error("Internal Server Error :\nPlease try again later")
                case 502 :
                    self.display_error("Bad Gateway :\nInvalid response from the server")
                case 503 :
                    self.display_error("Service Unavailable :\nServer is down")
                case 504 :
                    self.display_error("Gateway Timeout :\nNo response from the server")
                case _ :
                    self.display_error(f"HTTP error occured :\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error :\nCheck your internet connection and try again")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error :\nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects :\nCheck the URL")

        except requests.exceptions.RequestException as req_error :
            self.display_error(f"Request Error :\n{req_error}")

    def display_error(self, message) :
        self.temperature_label.setStyleSheet("""
            font-size : 30px ;
            color : hsl(218, 20%, 23%) ;
            """)
        self.temperature_label.setText(message)
        self.weather_image.hide()
        self.description_label.clear()

    def display_weather(self, data) :
        self.temperature_label.setStyleSheet("font-size : 75px")
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin * 9/5) - 459.67

        weather_id = data["weather"][0]["id"]

        weather_description = data["weather"][0]["description"]
        description = weather_description.split(' ')
        capitalised_words = []
        for word in description :
            new_word = word.capitalize()
            capitalised_words.append(new_word)
        description_complete = ' '.join(capitalised_words)

        self.temperature_label.setText(f"{temperature_celsius:.0f}℃")
        self.temperature_label.setStyleSheet("""
        color : hsl(218, 20%, 23%) ;
        """)

        weather_pixmap = QPixmap(self.get_weather_pic(weather_id))
        weather_icon = QIcon(weather_pixmap)
        self.weather_image.setIcon(weather_icon)
        self.weather_image.show()
        self.weather_image.setStyleSheet("""
            font-family : Segoe UI Emoji ;
            font-size : 100px ;
            border-radius : 20px ;
            border : 5px solid blue ;
            border-color : hsl(218, 72%, 55%) ;
            """)

        self.description_label.setText(description_complete)

        self.description_label.setStyleSheet("""
            color : hsl(218, 20%, 23%) ;
            """)

    @staticmethod
    def get_weather_pic(weather_id) :
        if 200 <= weather_id <= 232 :
            return "D:/Python/Weather App/Lightening Storm.png"
        elif 300 <= weather_id <= 321 :
            return "D:/Python/Weather App/Rain.png"
        elif 500 <= weather_id <= 504 :
            return "D:/Python/Weather App/Rainy w Sun.png"
        elif weather_id == 511 :
            return "D:/Python/Weather App/Cloud w Snow.png"
        elif 520 <= weather_id <= 531 :
            return "D:/Python/Weather App/Rain.png"
        elif 600 <= weather_id <= 622 :
            return "D:/Python/Weather App/Cloud w Snow.png"
        elif 701 <= weather_id <= 762 :
            return "D:/Python/Weather App/Mist.png"
        elif weather_id == 771:
            return "D:/Python/Weather App/Snow.png"
        elif weather_id == 781:
            return "D:/Python/Weather App/Tornado.png"
        elif weather_id == 800:
            return "D:/Python/Weather App/Sun.png"
        elif weather_id == 801:
            return "D:/Python/Weather App/Sunny w Clouds.png"
        elif weather_id == 802:
            return "D:/Python/Weather App/Cloud w Partial Sun.png"
        elif weather_id == 803:
            return "D:/Python/Weather App/Cloud.png"
        elif weather_id == 804:
            return "D:/Python/Weather App/Cloud.png"

    def further_weather(self) :
        webbrowser.open("https://openweathermap.org/", 2, True)

def main() :
    app = QApplication(sys.argv)
    weather_app = Weather_App()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__" :
    main()