from djitellopy import Tello
tello = Tello()
tello.takeoff()

for i in range(0, 2):
    tello.move_forward(50)
    tello.move_up(50)
tello.move_forward(50)
tello.land()
