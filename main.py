from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.image import Image

from backend.ics import Ics
import time
import os

from connected import Connected
from register import Register
from status import Status
from administration import Administration
from start import Start

from kivy.core.window import Window

class Login(Screen):

    def __init__(self, **kwargs):
        self.name='login'
        super(Screen,self).__init__(**kwargs)
        #softinput_mode = 'pan'
        #Window.softinput_mode = softinput_mode
        print("Constructor Works")
        self.app1 = App.get_running_app()
        self.app1.backend.attach('idle_on_enter',self.resetForm)
    


        
    def do_login(self, loginText, passwordText):
        
        
        self.app1.dict["email"] = loginText
        self.app1.dict["password"] = passwordText

        if( self.ids['login'].text == "" or self.ids['password'].text == ""):
            Factory.ErrorPopup().open()
        else:    


            self.app1.backend.attach('userAuthentificated', self.go_pickuptime)
            self.app1.backend.attach('adminAuthentificated', self.go_admin)
            self.app1.backend.loginStateMachine.onLogin(username = self.ids['login'].text, password = self.ids['password'].text)
            

        
        

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

    def do_register(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "register"

    def go_pickuptime(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'
        
    def go_admin(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'administration'

class LoginApp(App):
    email = StringProperty(None)
    password = StringProperty(None)
    name = StringProperty(None)
    surname = StringProperty(None)
    phone = StringProperty(None)
    backend = Ics()
    #Window.softinput_mode = 'pan'


    dict = {"email": email, "password": password, "name": name, "surname": surname, "phone": phone}
    
    def build(self):
        
        self.backend.attach('authorizing_on_enter',self.update)
        self.manager = ScreenManager()
        
        self.manager.add_widget(Start(name='start'))
        self.manager.add_widget(Login(name='login'))
        self.manager.add_widget(Administration(name='administration'))
        self.manager.add_widget(Connected(name='connected'))
        self.manager.add_widget(Register(name='register'))
        self.manager.add_widget(Status(name='status'))

        return self.manager

    def update(self, *args, **kwargs):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'
        
    


if __name__ == '__main__':
    LoginApp().run()
