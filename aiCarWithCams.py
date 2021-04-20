import gpiozero
import pygame
import picamera

robot = gpiozero.Robot(left=(22,23), right=(25,24))
camera = picamera.PiCamera()

pygame.init()
pygame.joystick.Joystick(0).init()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                camera.capture('/home/pi/Desktop/img.jpg')
                print("Picture has been saved on Desktop")
            elif event.button == 1:
                camera.start_recording('/home/pi/Desktop/vid.h264')
                print("Recording...")
            elif event.button == 2:
                camera.stop_recording()
                print("Recording is stopped")
            elif event.button == 3:
                camera.start_preview()
                print("preview is running")
        elif event.type == pygame.JOYHATMOTION:
            if event.value == (0,1):
                robot.forward(0.5)
            elif event.value == (0,-1):
                robot.backward()
            elif event.value == (-1,0):
                robot.left()
            elif event.value == (1,0):
                robot.right()
            else:
                robot.stop()
            
            
            
        
    