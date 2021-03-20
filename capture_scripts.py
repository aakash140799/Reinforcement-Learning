import key_scripts
import video_scripts
import log_scripts
from vidgear.gears import WriteGear
import win32api as wapi
import os
import threading
import time

"""
    press f11 to start captuing frames
    press f11 again to stop captuing
    press f10 to delete current capture, and restart immidately
    press f9 to stop program immidately
"""

output_params = {"-vcodec":"MPEG", "-input_framerate": 25}
capture_state = 0
del_it = 0
start = len(os.listdir('data'))//2 + 1


def capture():
    global capture_state
    global del_it
    global start

    
    # while in not_exit mode
    while capture_state != 2:

        out_file = str(start)
        # capture mode
        if capture_state == 1:
            log_scripts.log_msg('capturing : '+out_file)
            
            out_file = 'data\\'+out_file
            vid_out = WriteGear(out_file+'.avi',compression_mode=False,
                                custom_ffmpeg='C:\Program Files (x86)\ffmpeg\bin',**output_params)
            txt_out = open(out_file+'.txt', 'w')

            # capture 512 frames, or stop if altered
            cnt = 0
            while cnt <= 512 and not del_it:
                vid_out.write(video_scripts.get_state())
                txt_out.write(key_scripts.get_state())
                cnt = cnt + 1
            
            vid_out.close()
            txt_out.close()

            # if delete
            if del_it:
                os.remove(out_file+'.avi')
                os.remove(out_file+'.txt')
                del_it = 0
                capture_state = 0
                log_scripts.log_msg('deleting : '+out_file)
                log_scripts.log_msg('state  : False')
                log_scripts.log_msg('Capturing : Stop')
            else:
                log_scripts.log_msg('saving : '+out_file)
                start = start + 1
        else:
            log_scripts.log_msg('at hold')
            time.sleep(2)
    log_scripts.log_msg('capture thread exited')
    exit()
    
            
            
try:
    
    capture_thread = threading.Thread(target=capture)
    capture_thread.start()

    f11_state = 0
    f10_state = 0
    f9_state = 0
    while capture_state != 2:
        f11 = wapi.GetAsyncKeyState(0x7A)
        f10 = wapi.GetAsyncKeyState(0x79)
        f9 = wapi.GetAsyncKeyState(0x78)
        
        if f11 and f11_state == 0:
            print('alter')
            capture_state = 1 if capture_state == 0 else 0
            
        if f10 and f10_state == 0:
            del_it = 1
            
        if f9 and f9_state == 0:
            capture_state = 2

        f11_state = f11
        f10_state = f10
        f9_state = f9


    log_scripts.log_msg('exiting')
    capture_thread.join()
except KeyboardInterrupt:
    exit()

 
