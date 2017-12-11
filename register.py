from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.popup import Popup
from kivy.factory import Factory

class Register(Screen):
    def do_cancel(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "login"
        self.manager.get_screen("login")


    def do_save(self, nameText, surnameText, emailText, phoneText):
        if(nameText == "" or surnameText == "" or emailText == "" or phoneText == ""):
            Factory.Error2Popup().open()
        else:
            app = App.get_running_app()
            app.dict["name"] = nameText
            app.dict["surname"] = surnameTexto
            app.dict["email"] = emailText
            app.dict["phone"] = phoneText
            Factory.RegistrationPopup().open()
            #just for debugging atm
            print("Name is {}\n".format(app.dict["name"]))
            print("Surname is {}\n".format(app.dict["surname"]))

    
