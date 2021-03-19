import pyautogui
import pydirectinput
import pynput.keyboard as keyboard
import pynput.mouse as mouse
import time
"""
   press f11 to start capture
   press f11 again to stop catpure
   press f9 to end
"""


key_listener = None
mouse_listener = None
key_str = "WASDFJKLIUOH1234".lower()

keys_state = {k : 0 for k in key_str}
mouse_state = [0, 0, 0, 0]

def on_press(key):
   global key_listener;
   key = str(key)[1]
   if key in keys_state:
      keys_state[key] = 1
   

def on_release(key):
   global keys_state
   key = str(key)[1]
   if key in keys_state:
      keys_state[key] = 0


move_cnt = 0
def on_move(x, y):
   global mouse_state
   global move_cnt
   if move_cnt == 10:
      mouse_state[2:4] = [x-mouse_state[0],y-mouse_state[1]]
      mouse_state[0:2] = [x,y]
      move_cnt = 0
   move_cnt = move_cnt+1
   

key_listener = keyboard.Listener(on_press=on_press,on_release=on_release)
mouse_listener = mouse.Listener(on_move=on_move)


key_listener.start()
mouse_listener.start()


def get_state():
   kstate = ""
   for k in key_str:
      kstate = kstate + str(keys_state[k]) + ", "
   kstate = kstate + str(mouse_state[2]) + ", "
   kstate = kstate + str(mouse_state[3]) + "\n"
      
   return kstate


def replay_state(state):
   global keys_state
   
   for i in range(len(key_str)):
      if state[i] != keys_state[key_str[i]]:
            pydirectinput.keyUp(key_str[i]) if state == 0 else pydirectinput.keyDown(key_str[i])
            keys_state[key_str[i]] = state[i]

   mouse_state[0:2] = [mouse_state[0]+int(state[-2]),mouse_state[1]+int(state[-1])]
   mouse_state[2:4] = state[-2:]         
   pydirectinput.moveTo(mouse_state[0],mouse_state[1])


print('key_script done')
