import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

Connected = 3 # plug connected signal
Charge = 5    #if the car request the charge

#test = 5
sig_13A = 11
sig_20A = 13
sig_32A = 15

lock = 19
unlock = 21
rL = 23

pow_relay = 31
sif_relay = 29

pwm_pin = 37

count = 0
sum = 0 
average = 0

GPIO.setup(Connected,GPIO.IN)
GPIO.setup(Charge,GPIO.IN)
GPIO.setup(rL,GPIO.IN)

#GPIO.setup(test, GPIO.OUT)
GPIO.setup(lock,GPIO.OUT)
GPIO.output(lock, GPIO.LOW)

GPIO.setup(unlock,GPIO.OUT)
GPIO.output(unlock, GPIO.LOW)

GPIO.setup(sig_13A,GPIO.IN)
GPIO.setup(sig_20A,GPIO.IN)
GPIO.setup(sig_32A, GPIO.IN)

GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.output(pwm_pin, GPIO.LOW)

GPIO.setup(pow_relay, GPIO.OUT)
GPIO.output(pow_relay, 0)

my_pwm = GPIO.PWM(pwm_pin, 1000)
my_pwm.start(0)


def MAX_pwm():
        if(GPIO.input(sig_13A)== 0 and \
           GPIO.input(sig_20A)== 0 and \
           GPIO.input(sig_32A)== 0):
                pwm = 10
                return pwm
        elif(GPIO.input(sig_13A)== 1 and \
             GPIO.input(sig_20A)== 0 and \
             GPIO.input(sig_32A)== 0):
             pwm = 20
             return pwm
        elif(GPIO.input(sig_13A)== 1 and \
             GPIO.input(sig_20A)== 1 and \
             GPIO.input(sig_32A)== 0):
             pwm = 30
             return pwm
        elif(GPIO.input(sig_13A)== 1 and \
             GPIO.input(sig_20A)== 1 and \
             GPIO.input(sig_32A)== 1):
             pwm = 50
             return pwm
        else:
                pwm = 0
                return pwm

def Relay_function():
	time.sleep(1)
	GPIO.output(lock, 1)
	time.sleep(1)
	GPIO.output(lock, 0)
	time.sleep(0.01)
	if(GPIO.input(rL) == 0):
		time.sleep(1)
		print("Relay turned on ")
		GPIO.output(pow_relay, 1)
		time.sleep(1)
	else:
		print(" relay is off ")
		GPIO.output(pow_relay, 0)
		GPIO.output(unlock, 1)
		time.sleep(1)
		GPIO.output(unlock, 0)


while(1):
	#GPIO.output(pow_relay,1)
	#time.sleep(1)
	#GPIO.output(pow_relay,0)
	#time.sleep(1)
	while(GPIO.input(Connected) == 1 or GPIO.input(Charge) == 1): #if the plug is connected... CHARGE??
		average = 0
		time.sleep(0.0001)
		if(GPIO.input(Connected) == 1 and GPIO.input(Charge) == 1):
			GPIO.output(pow_relay, 0)
			pwm_value = 100
			my_pwm.ChangeDutyCycle(pwm_value)
			time.sleep(1)
			average = 0
			print("pwm detected, output pwm is 100% ")
		print("pwm detected")
	while(GPIO.input(Connected) == 0 or GPIO.input(Charge) == 0):
		pwm_value = MAX_pwm()
		my_pwm.ChangeDutyCycle(pwm_value)
		time.sleep(0.01)
		sum = 0
		count = 0
		while count < 100:
			time.sleep(0.0001)
			if (GPIO.input(Connected) == 0 and GPIO.input(Charge) == 0):
				sum = sum + 1;
				count += 1
				average = (sum/count)*1
			else:
				GPIO.output(pow_relay, 0)
				average = 0
				break
		print (average)
		if(average == 1):
			pwm_value = MAX_pwm()
			print("pwm value is: ",pwm_value )
			my_pwm.ChangeDutyCycle(pwm_value)
			time.sleep(0.01)
			Relay_function()
		else:
			GPIO.output(pow_relay, 0)
			break
	#	if(GPIO.input(test1) == 1):
	#		my_pwm.ChangeDutyCycle(50)
	#		print("bllalalalala")
	#	else:
	#		my_pwm.ChangeDutyCycle(100)


GPIO.cleanup()
