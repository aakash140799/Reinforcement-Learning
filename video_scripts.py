from vidgear.gears import ScreenGear

options = {"top": 20, "left": 5}
stream = ScreenGear(logging=True, **options).start()

def get_state():
    return stream.read()

print('video_script done')
