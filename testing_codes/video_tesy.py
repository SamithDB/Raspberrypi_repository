import picamera

#setup the camera
with picamera() as camera:
    camera.start_recording("pythonVid.h264")

    sleep(5) #this is for the duration of the video

    camera.stop_recording()