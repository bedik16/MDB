from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from backend.ics import Ics
import time
import os

from connected import Connected
from register import Register
from status import Status

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.dict["email"] = loginText
        app.dict["password"] = passwordText

        self.manager.transition = SlideTransition(direction="left")

        self.manager.current = 'connected'

      #  app.config.read(app.get_application_config())
      #  app.config.write()

        print("E-mail address is {}\n".format(app.dict["email"]))
        print("Password is {}\n".format(app.dict["password"]))


    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

    def do_register(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "register"

        

class LoginApp(App):
    email = StringProperty(None)
    password = StringProperty(None)
    name = StringProperty(None)
    surname = StringProperty(None)
    phone = StringProperty(None)


    dict = {"email": email, "password": password, "name": name, "surname": surname, "phone": phone}
    
    def build(self):
        backend = Ics()
        backend.attach(self)
        self.manager = ScreenManager()

        self.manager.add_widget(Login(name='login'))
        self.manager.add_widget(Connected(name='connected'))
        self.manager.add_widget(Register(name='register'))
        self.manager.add_widget(Status(name='status'))

        return self.manager

    def update(self, *args, **kwargs):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'
        
    


if __name__ == '__main__':
    LoginApp().run()
