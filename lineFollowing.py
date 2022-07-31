from gpiozero import Robot, LineSensor
from time import sleep, time

robin = Robot(left=(8, 7), right=(9, 10))

left_sensor = LineSensor(19)
right_sensor = LineSensor(26)

speed = 0.75

duration = 10
end_time = time() + duration

running = True

while running:
    left_detect  = left_sensor.value
    right_detect = right_sensor.value

    # The following rules need an understanding of how the line sensors work.
    # If the line sensor outputs 1, it is detecting a line, if it is 0, it is not detecting a line

    # Rule 1
    # If both sensors output 0, drive both motors forward (value of 1)
    if left_detect == 0 and right_detect == 0:
        left_mot = 1
        right_mot = 1
    # Rule 2
    # If the left senor outputs 1, it needs to turn left (left motor run backwards and right motor runs forwards)
    elif left_detect == 1:
        left_mot = -1
        right_mot = 1
    # Rule 3
    # If the right motor outputs 1, then it need to turn right (right motor run backwards and left motor runs forwards)
    elif right_detect == 1:
        left_mot = 1
        right_mot = -1

    # This changes the motor values in relation to the speed value
    robin.left_motor.value = left_mot * speed
    robin.right_motor.value = right_mot * speed

    # This will end our while loop, stopping it from running forever
    # It will also close every connection in a clean way
    if time() >= end_time:
        running = False
        robin.stop()
        robin.close()
        left_sensor.close()
        right_sensor.close()
