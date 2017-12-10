

class Conn:
    
    def __init__(self,ics):
        self.ref_to_ics = ics
        
    def doLogin(self,username,passw,nfc,onOkcallback):
        print("tets from do Login",username,nfc,passw)
        if nfc != 0:
            onOkcallback()
        elif username == 'test':
            onOkcallback()
        else:
            self.ref_to_ics.loginStateMachine.onFailedAuth()
        
