import win32api as wapi
import threading
import time
"""
   press f11 to start capture
   press f11 again to stop catpure
   press f9 to end
"""

key_str = "WASDFJKLIUOH1234".lower()

keys_state = {k : 0 for k in key_str}
mouse_state = [0, 0, 0, 0]

def get_state():
   kstate = ""
   for k in key_str:
      kstate = kstate + str(keys_state[k]) + ", "
      
   kstate = kstate + str(mouse_state[2]) + ", "
   kstate = kstate + str(mouse_state[3]) + "\n"
      
   return kstate

def update_state():
   while True:
      for k in key_str:
         keys_state[k] = wapi.GetAsyncKeyState(ord(k))
      (x, y) = wapi.GetCursorPos()
      mouse_state[2:4] = [x-mouse_state[0],y-mouse_state[1]]
      mouse_state[0:2] = [x,y]

      time.sleep(0.01)
   

key_thread = threading.Thread(target=update_state)
key_thread.start()


print('key_script done')
