import pydirectinput
import time
import win32api
import os

key_str = "WASDFJKLIUOH1234".lower()

keys_state = {k : 0 for k in key_str}
mouse_state = [600, 600, 0, 0]

def replay_state(state):
   global keys_state
   global mouse_state
   
   for i in range(len(key_str)):
      if state[i] != keys_state[key_str[i]]:
            pydirectinput.keyUp(key_str[i]) if state == 0 else pydirectinput.keyDown(key_str[i])
            keys_state[key_str[i]] = state[i]

   mouse_state[0:2] = [mouse_state[0]+10*int(state[-2]),mouse_state[1]+10*int(state[-1])]
   mouse_state[2:4] = state[-2:]         
   pydirectinput.moveTo(mouse_state[0],mouse_state[1])


def read_logs(out_file):
   logs = open(out_file).read().split('\n')[:-1]
   logs = [[int(i) for i in row.split(',')] for row in logs]
   
   return logs

start = 1
while start < len(os.listdir('data'))/2:
    logs = read_logs('data/'+str(start)+'.txt')
    print('reading : ' +str(start))

    for log in logs:
        replay_state(log)
        time.sleep(0.01)

    if win32api.GetAsyncKeyState(0x78):
       break
        
