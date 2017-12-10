from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, SlideTransition

class Administration(Screen):
    pwm_value = NumericProperty(0)
    current1_value = NumericProperty(0)
    current2_value = NumericProperty(0)
    current3_value = NumericProperty(0)
    voltage1_value = NumericProperty(0)
    voltage2_value = NumericProperty(0)
    voltage3_value = NumericProperty(0)

    def __init__(self, **kwargs):
        self.name = 'administration'
        super(Screen,self).__init__(**kwargs)
        print("Admin Constructor works")
        self.app = App.get_running_app()
        print("getSmartPiRef is: \n")
        print(self.app.backend.getSmartPiRef)
        self.smpi = self.app.backend.getSmartPiRef()
        self.smpi.attach('RMScurrent', self.update_current)
        self.smpi.attach('RMSvoltage', self.update_voltage)
      
    
    def do_cancel(self):
        self.app.backend.icsStateMachine.onChargingEnded()
        self.app.backend.loginStateMachine.onLock()
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

    def update_current(self, **kwargs):
        self.current1_label.text = "Current1: {}".format(kwargs['cur1'])
        self.current2_label.text = "Current2: {}".format(kwargs['cur2'])
        self.current3_label.text = "Current3: {}".format(kwargs['cur3'])

    def update_voltage(self, **kwargs):
        self.voltage1_label.text = "Voltage1: {}".format(kwargs['vol1'])
        self.voltage2_label.text = "Voltage2: {}".format(kwargs['vol2'])
        self.voltage3_label.text = "Voltage3: {}".format(kwargs['vol3'])

    




