from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

class Administration(Screen):
    def do_cancel(self):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = "login"
        self.manager.get_screen("login")
