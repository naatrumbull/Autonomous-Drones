from djitellopy import Tello
tello = Tello()
tello.takeoff()

for i in range(0, 5):
    tello.move_forward(50)
    tello.rotate_clockwise(72)
    tello.move_forward(50)
    tello.rotate_counter_clockwise(144)
tello.land()
