from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

class Register(Screen):
    def do_cancel(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "login"
        self.manager.get_screen("login").resetForm()


    def do_save(self, nameText, surnameText, emailText, phoneText):
        app = App.get_running_app()

        app.dict["name"] = nameText
        app.dict["surname"] = surnameText
        app.dict["email"] = emailText
        app.dict["phone"] = phoneText
        #just for debugging atm
        print("Name is {}\n".format(app.dict["name"]))
        print("Surname is {}\n".format(app.dict["surname"]))
    
