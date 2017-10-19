from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os

from connected import Connected
from register import Register

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
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Register(name='register'))

        return manager

    def get_application_config(self):
        if(not self.email):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.email

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()
