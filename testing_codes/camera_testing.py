#only usable with Raspberrypi
import picamera

#setup the camera
print("Camera ready!")
with picamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("i/home/pi/Desktop/cookie/newimage.jpg")

print("picture taken")
