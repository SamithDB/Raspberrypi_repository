import picamera

file = "/home/pi/Desktop/cookie"
timestamp_msg="Driver&time"

print("Camera ready!")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture(file)
    print("picture taken")

command = "/user/bin/convert" +file+ " -pointsize 32 \ -fill red -annotate +700+500 '" +timestamp_msg+ "' "+file

#Execute our command
call([command], shell=True)
print("Picture timestamped!")