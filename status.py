from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.progressbar import ProgressBar

class Status(Screen):
    def do_cancel(self):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = "login"
        self.manager.get_screen("login")
    
