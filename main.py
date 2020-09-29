import time
from time import ctime
import pywhatkit
import pyfirmata
from notify_run import Notify

current_time = ctime()

notify = Notify()

phone_number_fire_force = "Fire force number" #your nearest fire force number

com_port = 'arduino com port' # arduino com port

msg_to_fire_force = "msg "# your msg to fire force

board = pyfirmata.Arduino(com_port)

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[0].enable_reporting()

sen = board.get_pin('a:0:i')

while True:
	time.sleep(2.0)
	read = sen.read()
	if int(read*100) <= 87:
		print('!!')
		notify.send('Fire !!')
		pywhatkit.sendwhatmsg(phone_number_fire_force,msg_to_fire_force,int(current_time[11:13]),int(current_time[14:16]) + 1)
		break

	else:
		print('..')
board.exit()