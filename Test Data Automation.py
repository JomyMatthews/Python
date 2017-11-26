
#Importing Threading Module.
import threading

# Defining the function to print every 100 milli seconds
def printevery100ms():
  threading.Timer(.1,printevery100ms).start()

#Importing Time Module
  import time
  ts = time.time()

#Importing Datetime Module.
  import datetime
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

#Setting up to start receiving Mouse Coordinates
  from ctypes import windll,Structure,c_int,byref

  class POINT(Structure):
      _fields_ = [("x",c_int),("y",c_int)]

#Getting the Cursor position using windows dynamic link library.
  def queryMousePosition():
      pt = POINT()
      windll.user32.GetCursorPos(byref(pt))
      return {"x": pt.x,"y": pt.y}

  pos = queryMousePosition()

#Formatting the print out
  print("Mouse Coordinates & TimeStamp: "'{{\'x\': {}, \'y\': {}}}'.format(pos['x'],pos['y']),st)

#Calling the function to print every 100 milli seconds.
printevery100ms()