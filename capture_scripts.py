import key_scripts
import video_scripts
import log_scripts
from vidgear.gears import WriteGear
import pynput.keyboard as keyboard
import os
import threading


output_params = {"-vcodec":"MPEG", "-input_framerate": 25}
def capture(out_file):
    vid_out = WriteGear(out_file+'.avi',compression_mode=False,
                        custom_ffmpeg='C:\Program Files (x86)\ffmpeg\bin',**output_params)
    txt_out = open(out_file+'.txt', 'w')
    
    for i in range(512):
        vid_out.write(video_scripts.get_state())
        txt_out.write(key_scripts.get_state())

    vid_out.close()
    txt_out.close()


capture_state = 0
del_it = 0
start = len(os.listdir('data'))//2 + 1
    
def start_capture():
    global start
    global del_it
    global capture_state
    
    while capture_state:
        capture(str(start))
        if del_it:
            log_scripts.log_msg('deleted ' + str(start))
            os.remove(str(start)+'.avi')
            os.remove(str(start)+'.txt')
        else:
            log_scripts.log_msg('saving '+ str(start))
            start = start + 1
            
    log_scripts.log_msg('stoping capture')


capture_thread = None
def alter(key):
    global start
    global del_it
    global capture_state
    global capture_thread

    print('altering')
    if key == keyboard.Key.f11:
        if capture_state == 0:
            log_scripts.log_msg('starting capture')
            capture_state = 1
            capture_thread = threading.Thread(target=start_capture)
            capture_thread.start()
        else:
            capture_state = 0
            capture_thread.join()
    elif key == keyboard.Key.f10:
        del_it = 1
    elif key == keyboard.Key.f9:
        capture_state = 0
        capture_thread.join()
        return False


with keyboard.Listener(on_press=alter) as listener:
    log_script.log_msg('starting with', start)
    listener.join()

