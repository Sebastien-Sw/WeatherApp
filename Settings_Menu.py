import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont, QFontDatabase

class Settings_Menu(QWidget) :
    def __init__ (self, weather_app_window) :
        super().__init__()
        self.weather_app_window = weather_app_window

        self.setWindowIcon(QIcon("D:/Dev/Git/WeatherApp/Weather App Assets/Settings Menu Icon.png"))

        self.setGeometry(725, 150, 450, 800)

        self.header_label = QLabel("Settings Menu :")
        self.temperature_scale_label = QLabel("Temperature Scale")
        self.celcius_scale_button = QPushButton("℃")
        self.fahrenheit_scale_button = QPushButton("℉")
        self.colour_scheme_label = QLabel("Colour Scheme")
        self.light_mode_button = QPushButton("Light Mode")
        self.dark_mode_button = QPushButton("Dark Mode")
        self.city_input_method_label = QLabel("Input Method")
        self.city_name_button = QPushButton("City Name")
        self.city_id_button = QPushButton("City ID")
        self.close_button = QPushButton("Close")

        self.initUI()

    def initUI(self) :
        self.setWindowTitle("Settings Menu")

        main_layout = QVBoxLayout()

        self.setLayout(main_layout)

        main_layout.addWidget(self.header_label)
        main_layout.addWidget(self.temperature_scale_label)

        scale_options = QHBoxLayout()
        scale_options.addWidget(self.celcius_scale_button)
        scale_options.addWidget(self.fahrenheit_scale_button)
        main_layout.addLayout(scale_options)

        main_layout.addWidget(self.colour_scheme_label)

        colour_mode = QHBoxLayout()
        colour_mode.addWidget(self.light_mode_button)
        colour_mode.addWidget(self.dark_mode_button)
        main_layout.addLayout(colour_mode)

        main_layout.addWidget(self.city_input_method_label)

        input_method = QHBoxLayout()
        input_method.addWidget(self.city_name_button)
        input_method.addWidget(self.city_id_button)
        main_layout.addLayout(input_method)

        close_button_layout = QHBoxLayout()
        close_button_layout.addWidget(self.close_button)
        main_layout.addLayout(close_button_layout)

        self.header_label.setAlignment(Qt.AlignCenter)
        self.temperature_scale_label.setAlignment(Qt.AlignCenter)
        self.colour_scheme_label.setAlignment(Qt.AlignCenter)
        self.city_input_method_label.setAlignment(Qt.AlignCenter)

        main_layout.setContentsMargins(15, 20, 15, 5)
        main_layout.setSpacing(5)

        # Fonts

        # Header Font
        Ubuntu_Header = QFont("Ubuntu Regular", 30, QFont.Bold, True)
        self.header_label.setFont(Ubuntu_Header)

        Ubuntu_Medium = QFont("Ubuntu Medium", 20, QFont.Bold)
        self.temperature_scale_label.setFont(Ubuntu_Medium)
        self.colour_scheme_label.setFont(Ubuntu_Medium)
        self.city_input_method_label.setFont(Ubuntu_Medium)

        Ubuntu_Bold = QFont("Ubuntu Regular", 17, QFont.Bold)
        self.close_button.setFont(Ubuntu_Bold)

        Ubuntu_Bold_Small = QFont("Ubuntu Regular", 15, QFont.Bold)
        self.celcius_scale_button.setFont(Ubuntu_Bold_Small)
        self.fahrenheit_scale_button.setFont(Ubuntu_Bold_Small)
        self.light_mode_button.setFont(Ubuntu_Bold_Small)
        self.dark_mode_button.setFont(Ubuntu_Bold_Small)
        self.city_name_button.setFont(Ubuntu_Bold_Small)
        self.city_id_button.setFont(Ubuntu_Bold_Small)

        # Styling
        self.setStyleSheet("""
            background-color : hsl(45, 29%, 97%) ;
            """)
        self.header_label.setFixedHeight(100)
        self.header_label.setStyleSheet("""
            background-color : hsl(218, 72%, 52%) ;
            padding : 20px ;
            border-radius : 15px ;
            color : hsl(45, 29%, 97%) ;
            """)
        self.temperature_scale_label.setFixedHeight(75)
        self.temperature_scale_label.setStyleSheet("""
            background-color : hsl(218, 72%, 52%) ;
            padding : 20px ;
            border-radius : 15px ;
            color : hsl(45, 29%, 97%) ;
            """)
        self.celcius_scale_button.setStyleSheet("""
            QPushButton{
                color : hsl(45, 29%, 97%) ;
                padding : 10px ;
                border : 3px solid orange ;
                border-color : hsl(13, 81%, 61%) ;
                border-radius : 15px ;
                background-color : hsl(13, 81%, 61%) ;
                text-align : center ;
            }
            QPushButton:hover{
                background-color : hsl(13, 81%, 81%) ;
                border-color : hsl(13, 81%, 81%) ;
            }
            """)
        self.fahrenheit_scale_button.setStyleSheet("""
            QPushButton{
                color : hsl(45, 29%, 97%) ;
                padding : 10px ;
                border : 3px solid orange ;
                border-color : hsl(13, 81%, 61%) ;
                border-radius : 15px ;
                background-color : hsl(13, 81%, 61%) ;
                text-align : center ;
            }
            QPushButton:hover{
                background-color : hsl(13, 81%, 81%) ;
                border-color : hsl(13, 81%, 81%) ;
            }
            """)
        self.colour_scheme_label.setFixedHeight(75)
        self.colour_scheme_label.setStyleSheet("""
            background-color : hsl(218, 72%, 52%) ;
            padding : 20px ;
            border-radius : 15px ;
            color : hsl(45, 29%, 97%) ;
            """)
        self.light_mode_button.setStyleSheet("""
            QPushButton{
                color : hsl(45, 29%, 97%) ;
                padding : 10px ;
                border : 3px solid orange ;
                border-color : hsl(13, 81%, 61%) ;
                border-radius : 15px ;
                background-color : hsl(13, 81%, 61%) ;
                text-align : center ;
            }
            QPushButton:hover{
                background-color : hsl(13, 81%, 81%) ;
                border-color : hsl(13, 81%, 81%) ;
            }
            """)
        self.dark_mode_button.setStyleSheet("""
            QPushButton{
                color : hsl(45, 29%, 97%) ;
                padding : 10px ;
                border : 3px solid orange ;
                border-color : hsl(13, 81%, 61%) ;
                border-radius : 15px ;
                background-color : hsl(13, 81%, 61%) ;
                text-align : center ;
            }
            QPushButton:hover{
                background-color : hsl(13, 81%, 81%) ;
                border-color : hsl(13, 81%, 81%) ;
            }
            """)
        self.city_input_method_label.setFixedHeight(75)
        self.city_input_method_label.setStyleSheet("""
            background-color : hsl(218, 72%, 52%) ;
            padding : 20px ;
            border-radius : 15px ;
            color : hsl(45, 29%, 97%) ;
            """)
        self.city_name_button.setStyleSheet("""
            QPushButton{
                color : hsl(45, 29%, 97%) ;
                padding : 10px ;
                border : 3px solid orange ;
                border-color : hsl(13, 81%, 61%) ;
                border-radius : 15px ;
                background-color : hsl(13, 81%, 61%) ;
                text-align : center ;
            }
            QPushButton:hover{
                background-color : hsl(13, 81%, 81%) ;
                border-color : hsl(13, 81%, 81%) ;
            }
            """)
        self.city_id_button.setStyleSheet("""
            QPushButton{
                color : hsl(45, 29%, 97%) ;
                padding : 10px ;
                border : 3px solid orange ;
                border-color : hsl(13, 81%, 61%) ;
                border-radius : 15px ;
                background-color : hsl(13, 81%, 61%) ;
                text-align : center ;
            }
            QPushButton:hover{
                background-color : hsl(13, 81%, 81%) ;
                border-color : hsl(13, 81%, 81%) ;
            }
            """)
        self.close_button.setStyleSheet("""
            QPushButton{
                color : hsl(45, 29%, 97%) ;
                padding : 10px ;
                border : 3px solid orange ;
                border-color : hsl(13, 81%, 61%) ;
                border-radius : 15px ;
                background-color : hsl(13, 81%, 61%) ;
                text-align : center ;
            }
            """)

        self.celcius_scale_button.clicked.connect(self.set_celcius)
        self.fahrenheit_scale_button.clicked.connect(self.set_fahrenheit)

        self.light_mode_button.clicked.connect(self.set_mode_light)
        self.dark_mode_button.clicked.connect(self.set_mode_dark)

        self.city_name_button.clicked.connect(self.set_input_name)
        self.city_id_button.clicked.connect(self.set_input_id)

        self.close_button.clicked.connect(self.close_settings)

    def close_settings(self) :
        self.close()

    def set_celcius(self) :
        pass

    def set_fahrenheit(self) :
        pass

    def set_mode_light(self) :
        pass

    def set_mode_dark(self) :
        pass

    def set_input_name(self) :
        pass

    def set_input_id(self) :
        pass