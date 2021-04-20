import gpiozero
import random
import time

robot = gpiozero.Robot(left=(22,23), right=(25,24))

def get_distance():
    sensor = gpiozero.DistanceSensor(echo=16, trigger=18, max_distance=1)
    distance = sensor.distance * 100
    print(distance)
    return(distance)

def robot_turn():
    robot.backward()
    time.sleep(1)
    rnd = random.randrange(2)
    if rnd == 1:
        robot.left()
        time.sleep(1)
    else:
        robot.right()
        time.sleep(1)
        
while True:
    dist = get_distance()
    if dist <= 30:
        robot_turn()
    else:
        robot.forward()
        time.sleep(0.1)