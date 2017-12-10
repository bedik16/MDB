from transitions.extensions import HierarchicalMachine as Machine
from backend.statemachine.state import loginState,loginTransitions,icsState,icsTransition
from backend.nfc import Nfc
from backend.conn import Conn
from collections import defaultdict
import time


class Ics:
    nfccontroller = None
    smartpicontroller = None
    loginState = None
    icsState = None
    testclass = None

    def __init__(self):

        self.observers = defaultdict(list)
        self.loginStateMachine = LoginSMachine(self)
        self.icsStateMachine = IcsSMachine(self)
        self.loginState = Machine(model =self.loginStateMachine,states = loginState,transitions = loginTransitions,initial = 'locked',ignore_invalid_triggers = True,send_event=True)
        self.icsState = Machine(model = self.icsStateMachine,states = icsState,transitions = icsTransition,initial = 'idle',ignore_invalid_triggers=True,send_event=True)
        self.connection = Conn(self)

        self.nfccontroller = Nfc()
        self.nfccontroller.setOnNfcPresentCallback(self.loginStateMachine.onLogin)       
        print("starting nfc thread")
        self.nfccontroller.start()
 

    def getLoginState(self):
        return self.loginStateMachine.state
    
    def getIcsState(self):
        return self.icsStateMachine.state
    #attach listener on specific event for notifications
    def attach(self,topic,observer):
        self.observers[topic].append(observer)

    def detach(self,topic,observer):
        if observer in self.observers:
            del self.observers[topic]
    #called to call notify listerner for specficed topic
    def _notify(self,topic):
        #print(self.observers.keys())
        value = self.observers.get(topic,None)
        #print(value)
        if value != None:
            for calling in value:
                calling()
    

class LoginSMachine(object):

    def __init__(self,ics):
        self.caller = ics

    #called when entering autherization in login
    def loginAttempt(self,eventdata):
        nfckey =eventdata.kwargs.get('nfc', 0)
        username = eventdata.kwargs.get('username,',0)
        passwrod = eventdata.kwargs.get('password',0)
        print(nfckey)
        self.caller._notify('authorizing_on_enter')
        self.caller.connection.doLogin(username,passwrod,nfckey,self.caller.loginStateMachine.onPassedAuth)

    def failedAuth(self,eventdata):
        print('failed auth')
        self.caller._notify('after_failedAuth')

class IcsSMachine(object):

    def __init__(self,ics):
        self.caller = ics
       
    #guard for entering charging
    def userValidated(self):
        if self.caller.getLoginState() == 'unlocked':
            return True
        else:
            return False