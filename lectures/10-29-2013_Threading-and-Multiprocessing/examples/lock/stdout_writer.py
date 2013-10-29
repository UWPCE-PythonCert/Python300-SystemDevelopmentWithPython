import random
import sys
import threading
import time

def write():
    sys.stdout.write( "%s writing.." % threading.current_thread().name)
    time.sleep(random.random())
    sys.stdout.write( "..done\n")
    
    
while True:
    thread = threading.Thread(target=write)
    thread.start()
    time.sleep(.1)
    
