from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.clock import Clock

class Register(Screen):
    def build(self):
        Clock.schedule_once(self.screensaver_callback, 5)
        
    def do_cancel(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "login"
        self.manager.get_screen("login")


    def do_save(self, nameText, surnameText, emailText, phoneText):
        app = App.get_running_app()

        app.dict["name"] = nameText
        app.dict["surname"] = surnameText
        app.dict["email"] = emailText
        app.dict["phone"] = phoneText
        Factory.MyPopup().open()
        #just for debugging atm
        print("Name is {}\n".format(app.dict["name"]))
        print("Surname is {}\n".format(app.dict["surname"]))

    def screensaver_callback(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "start"
        self.manager.get_screen("start")

        
