import launchpad_py as launchpad
import pygame
import cv2 as cv
import time
import config

# Find my Launchpad
if launchpad.LaunchpadPro().Check(0):
    lp = launchpad.LaunchpadPro()
    lp.Open()
    lp.Reset()
else: 
    print('\n\033[91mError: Launchpad not found.\033[97m\n')
    exit()

# Launchpad color test
if config.test == True:
    for i in range(128):
        lp.LedAllOn(i)
        print('[COLOR TEST]: Tested ', i,'. color.')
        time.sleep(0.1)
    print('\n\033[92m[COLOR TEST]: END\033[97m')
    lp.ButtonFlush()
    lp.Reset()
else: print('\033[93m[COLOR TEST]: Skipped\033[97m')

capture = cv.VideoCapture(config.vidLocation)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    frame_resized = cv.resize(frame, (8, 8), interpolation = cv.INTER_CUBIC)
    cv.imshow('Video', frame) #<- The original video frame
    #cv.imshow('Video resized', frame_resized) #<- The modified video frame for launchpad

    # The pixels
    for i in range(7):
        i=i+1
        lp.LedCtrlXY(0, i, frame_resized[i, 0, 0], frame_resized[i, 0, 1], frame_resized[i, 0, 2])
        lp.LedCtrlXY(1, i, frame_resized[i, 1, 0], frame_resized[i, 1, 1], frame_resized[i, 1, 2])
        lp.LedCtrlXY(2, i, frame_resized[i, 2, 0], frame_resized[i, 2, 1], frame_resized[i, 2, 2])
        lp.LedCtrlXY(3, i, frame_resized[i, 3, 0], frame_resized[i, 3, 1], frame_resized[i, 3, 2])
        lp.LedCtrlXY(4, i, frame_resized[i, 4, 0], frame_resized[i, 4, 1], frame_resized[i, 4, 2])
        lp.LedCtrlXY(5, i, frame_resized[i, 5, 0], frame_resized[i, 5, 1], frame_resized[i, 5, 2])
        lp.LedCtrlXY(6, i, frame_resized[i, 6, 0], frame_resized[i, 6, 1], frame_resized[i, 6, 2])
        lp.LedCtrlXY(7, i, frame_resized[i, 7, 0], frame_resized[i, 7, 1], frame_resized[i, 7, 2])
        lp.LedCtrlXY(i, 8, frame_resized[7, i, 0], frame_resized[7, i, 1], frame_resized[7, i, 2]) #last line
        lp.LedCtrlXY(0, 8, frame_resized[7, 0, 0], frame_resized[7, 0, 1], frame_resized[7, 0, 2]) #1 pixel bugfix

    if cv.waitKey(1) & 0xFF==ord('d'):
        break

# End the stream
capture.release()
cv.destroyAllWindows()
print('\n\033[92mVideo ended.\033[97m')

# Reset Launchpad
lp.ButtonFlush()
lp.Reset()
print('\033[92mLaunchpad flushed and reset.\033[97m\n')