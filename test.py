from time import sleep
import msvcrt

while 1:
    try:
        line = msvcrt.getch()
        if line == 'w':
            forwardDrive()
        if line == 's':
            reverseDrive()
        if line == 'a':
            spinLeft()
        if line == 'd':
            spinLeft()
        if line == 'q':
            forwardLeft()
        if line == 'e':
            forwardRight()
        if line == '1':
            forwardTurnLeft()
        if line == '3':
            forwardTurnRight()
        if line == 'z':
            reverseLeft()
        if line == 'c':
            reverseRight()
        if line == 'v':
            reverseTurnLeft()
        if line == 'b':
            reverseTurnRight()
        else:
            allStop()
            sleep(0.1)

    except:
        print('failed')