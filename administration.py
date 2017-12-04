from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, SlideTransition

class Administration(Screen):
    pwm_value = NumericProperty(0)
    
    def do_cancel(self):
        self.manager.transition = SlideTransition(direction = "left")
        self.manager.current = "login"
        self.manager.get_screen("login")

    def do_increment(self):
        if(self.pwm_value >= 0 and self.pwm_value < 100):
            self.pwm_value += 10
            self.my_label.text = "PWM Value: {}".format(self.pwm_value)
        else:
            self.pwm_value = 0
            self.my_label.text = "PWM Value: {}".format(self.pwm_value)

    def do_decrement(self):
        if(self.pwm_value <= 100 and self.pwm_value > 0):
            self.pwm_value -= 10
            self.my_label.text = "PWM Value: {}".format(self.pwm_value)
        else:
            self.pwm_value = 100
            self.my_label.text = "PWM Value: {}".format(self.pwm_value)

    




