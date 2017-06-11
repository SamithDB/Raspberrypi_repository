#only usable with Raspberrypi
import picamera

#setup the camera
print("Camera ready!")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("/home/pi/Desktop/cookie/newimage.jpg")

print("picture taken")
