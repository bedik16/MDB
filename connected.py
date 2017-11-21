from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.garden.circulardatetimepicker import CircularTimePicker

class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def do_save(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'status'
        self.manager.get_screen('status')

