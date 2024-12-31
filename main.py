from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

import mysql.connector


# KV Layout code combined inside the Python file
kv = """
FloatLayout:
    Image:
        source: "green2.jpg"  # Image file for the background
        allow_stretch: True
        keep_ratio: False

    Image:
        id: profile_picture
        source: "42797457-removebg-preview.png"
        size_hint: None, None
        size: "80dp", "80dp"
        pos_hint: {"center_x":.5, "center_y": .93}
        allow_stretch: True
        radius: [60]

    MDTextButton:
        text: "User Login"
        size_hint: None, None
        size: "100dp", "50dp"
        pos_hint: {"center_x": .5, "center_y": .85}

    MDTextField:
        id: username_input
        hint_text: "Email or Phone Number"
        font_size: "20dp"
        icon_right: "email"
        size_hint_x: .85
        pos_hint: {"center_x": .5, "center_y": .65}
        mode: "round"
        
        error: False  # To control error highlighting
        hint_text_color_normal: 0, 0, 0, 1
        hint_text_color_focus: 0, 0, 0, 1
        helper_text_color: 0, 0, 0, 1
        line_color_normal: 0, 0, 0, 1
        line_color_focus: 0, 0, 0, 1

    MDTextField:
        id: password_input
        hint_text: "Password"
        font_size: "20dp"
        icon_right: "lock"
        size_hint_x: .85
        pos_hint: {"center_x": .5, "center_y": .5}
        mode: "round"
        password: True
        hint_text_color_normal: 0, 0, 0, 1
        hint_text_color_focus: 0, 0, 0, 1
        line_color_normal: 0, 0, 0, 1
        line_color_focus: 0, 0, 0, 1

    BoxLayout:
        spacing: dp(5)
        size_hint: .85, None
        pos_hint: {"center_x": .5, "center_y": .38}
        height: "30dp"
        MDCheckbox:
            id: my_checkbox
            size_hint: None, None
            size: dp(30), dp(30)
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_press:
                password_input.password = not password_input.password

        MDLabel:
            text: "Show password"
            size_hint_y: None
            height: dp(30)
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1

    BoxLayout:
        orientation: "horizontal"
        size_hint: .85, None
        height: "50dp"
        pos_hint: {"center_x": .5, "center_y": .3}
        spacing: dp(10)

        MDFlatButton:
            text: "SIGN IN"
            font_size: "22dp"
            on_release: app.validate_credentials()

            md_bg_color: 0.722, 0.525, 0.043, 1
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint: 0.45, None
            height: dp(50)
            line_color: 0, 0, 0, 1

    MDLabel:
        id: status_label
        text: ""
        size_hint: None, None
        size: "300dp", "50dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        color: 1, 0, 0, 1  # Red color for error messages
"""

class LoginScreen(MDScreen):
    """Login screen class with validation functionality."""
    
class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def validate_credentials(self):
        email = self.root.ids.username_input.text
        password = self.root.ids.password_input.text
        status_label = self.root.ids.status_label

        if not email or not password:
            status_label.text = "Please fill in both fields."
            return
        
        # Hash the password
        

        try:
            # Connect to the MySQL database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Your MySQL password here
                database="user"  # Your MySQL database here
            )
            cursor = connection.cursor()

            # Insert the new user into the database
            cursor.execute("INSERT INTO user (email, password) VALUES (%s, %s)", (email, password))
            connection.commit()

            status_label.text = "Successfully registered!"

            connection.close()

        except mysql.connector.Error as err:
            status_label.text = f"Error: {err}"

if __name__ == "__main__":
    MyApp().run()
