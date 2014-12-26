import bluetooth as BT
import time
from pykeyboard import PyKeyboard
ks = PyKeyboard()
nearBy=BT.discover_devices(lookup_names=True)
for i,(j,k) in enumerate(nearBy):
 print i+1,")",k
x=input("Press Anything to continue")  #Press a keystroke y=to start
addr=nearBy[x-1][0]
print addr,"Chosen\n"
port=1
sock=BT.BluetoothSocket(BT.RFCOMM)
sock.connect((addr,port))
print "Connected"
inp=raw_input()
array=[]
string=""
while(inp!="ex"):
 char=sock.recv(1)
 if(char.replace('\r','').replace('\n','')=='p'):
  print "Prev"
  ks.press_key(ks.alt_key)
  ks.tap_key(ks.left_key)
  ks.release_key(ks.alt_key)
 if(char.replace('\r','').replace('\n','')=='l'):
   print "play"  
   ks.press_key(ks.control_key)
   ks.tap_key(' ')
   ks.release_key(ks.control_key)
 if(char.replace('\r','').replace('\n','') == 'n'):
   print "next"
   ks.press_key(ks.alt_key)
   ks.tap_key(ks.right_key)
   ks.release_key(ks.alt_key)
 

#print len(sock.recv(1024))
sock.close()
