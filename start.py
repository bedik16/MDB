from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage

class Start(Screen):
    def on_touch_down(self, touch):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = "login"
        self.manager.get_screen("login")
