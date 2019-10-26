from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

print(datetime.now());

pir = MotionSensor(4)
camera = PiCamera()

timestamp = "{0:%Y}-{0:%m}-{0:%d}".format(datetime.now());
record_file_path = "/home/pi/Desktop/"
record_file = record_file_path + timestamp + "-intruder.h264";


while True:
    pir.wait_for_motion()
    print("YEYY...Motion Detected...")

    camera.start_recording(record_file)    
        
    pir.wait_for_no_motion()
    print("---No Motion Detected---")
    camera.stop_recording()





def start_camera_pic_action():
    camera.capture('/home/pi/Desktop/campic.png')
    camera.start_preview()
    camera.stop_preview()
