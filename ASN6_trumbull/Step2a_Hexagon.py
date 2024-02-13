from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

for i in range(0, 7):
    tello.move_forward(50)
    tello.rotate_clockwise(60)
tello.land()
