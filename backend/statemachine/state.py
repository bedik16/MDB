from transitions.extensions.nesting import NestedState as State
loginState = [
      State(name='locked',on_enter=['failedAuth']),State(name='authorizing',on_enter=['loginAttempt']),{'name':'unlocked','children':['admin','user']}]

loginTransitions = [
    {'trigger':'onFailedAuth','source':'authorizing','dest':'locked','after':'failedAuth'},
    ['onLogin','locked','authorizing'],
    ['onPassedAuth','authorizing','unlocked'],
    ['onLock','unlocked','locked'],
]
icsState = ['idle','error',{'name': 'charging','children' : ['powerOn','negotiating','chargeconfig']}] 
icsTransition = [
    {'trigger':'onStartCharging','source':'idle','dest':'charging','conditions':'userValidated'},
    ['onChargingEnded','charging','idle'],
    ['onError','charging','error'],
    ['onValidationPassed','error','idle'],
    ['onConfigFinish',['charging','charging_chargeconfig'],['charging','charging_negotiating']],
    ['onAgree',['charging','charging_negotiating'],['charging','charging_powerOn']],
    ['onNewCondition',['charging','charging_powerOn'],['charging','charging_negotiating']],
    ['onConfigChanged',['charging','charging_powerOn'],['charging','charging_chargeconfig']],
]
