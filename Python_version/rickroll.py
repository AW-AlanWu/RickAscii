import os
import time
import playsound
from pynput import keyboard
import multiprocessing

a = []
for i in range(0,5301):
	with open('/Users/wangkaiyu/Desktop/rickroll/ascii/'+str(i).zfill(4)+'.txt','r') as f:
		a.append(f.read())

playsound.playsound('/Users/wangkaiyu/Desktop/rickroll/resources/rickroll.mp3', False)

start = time.time()
while True:
	now = time.time()
	if (int)((now-start)*25) > 5300:
		break
	print(a[(int)((now-start)*25)])
	time.sleep(0.04)