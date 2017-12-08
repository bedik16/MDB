from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.animation import Animation
from kivy.clock import Clock
#from kivy.uix.image import Image
#from kivy.uix.image import AsyncImage
from kivy.uix.video import Video
from kivy.properties import ObjectProperty

class Start(Screen):
    videoPlayer  = ObjectProperty()

    def on_enter(self):
        self.videoPlayer.source = 'carpediem.avi'
        self.videoPlayer.play = True
        self.videoPlayer.options = {'eos': 'loop'}
        
    def on_touch_down(self, touch):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = "login"
        self.manager.get_screen("login")
