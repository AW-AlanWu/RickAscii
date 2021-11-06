from img2ascii import to_ascii
import os

try:
    if not os.path.exists('/Users/wangkaiyu/Desktop/rickroll/ascii'):
        os.makedirs('/Users/wangkaiyu/Desktop/rickroll/ascii')

except OSError:
    print('Error: Creating directory of ascii')

for i in range(0,5301):
	with open("/Users/wangkaiyu/Desktop/rickroll/ascii/"+str(i).zfill(4)+".txt", "w") as f:
		name = '/Users/wangkaiyu/Desktop/rickroll/image/'+str(i).zfill(4)+'.jpg'
		print('Converting...' + name)
		f.write(to_ascii(name))
