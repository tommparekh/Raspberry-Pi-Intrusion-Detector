from gpiozero import MotionSensor
from picamera import PiCamera, Color
from datetime import datetime
from time import sleep

print(datetime.now());

pir = MotionSensor(4)
camera = PiCamera()

timestamp = "{0:%Y}-{0:%m}-{0:%d}".format(datetime.now());
record_file_path = "/home/pi/Desktop/"
record_file = record_file_path + timestamp + "-intruder.h264";


def start_camera_preview():
#    camera.start_preview(alpha=100)
    camera.start_preview()
#    camera.brightness = 50
#    camera.contrast=50    
    camera.annotate_background = Color('black')
    camera.annotate_foreground = Color('white')
    camera.annotate_text = " Recording in progress "
    sleep(5)
    camera.stop_preview()

def intruder_video_capture():
    while True:
        pir.wait_for_motion()
        print("YEYY...Motion Detected...")
        camera.start_recording(record_file)              
        pir.wait_for_no_motion()
        print("---No Motion Detected---")
        camera.stop_recording()

def start_camera_pic_capture():
    camera.capture('/home/pi/Desktop/campic.png')

start_camera_preview()
