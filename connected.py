from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.garden.circulardatetimepicker import CircularTimePicker

class Connected(Screen):
    def disconnect(self):
        app = App.get_running_app()
        #app.backend.deattach('userAuthentificated', self.go_login)
        #app.backend.deattach('adminAuthentificated', self.go_login)
        app.backend.icsStateMachine.onChargingEnded() #Change the States
        app.backend.loginStateMachine.onLock()
        self.go_login()
        
    def do_save(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'status'
        self.manager.get_screen('status')

    def go_login(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()


