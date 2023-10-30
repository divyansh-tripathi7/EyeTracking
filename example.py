"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text1 = ""
    text2 = ""
    
    val1 = gaze.horizontal_ratio()
    cv2.putText(frame, "Horizontal Value:  " + str(val1), (90, 100), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    # 0 top 1 bottom 
    # 0 left 1 right


    # if gaze.is_blinking():
    #     text = "Blinking"
    # elif gaze.is_right():
    #     text = "Looking right"
    # elif gaze.is_left():
    #     text = "Looking left"
    # elif gaze.is_center():
    #     text = "Looking center"

    if val1 is not None and val1 < 0.4:
        text1 = "LEFT"
    elif val1 is not None and val1 > 0.6:
        text1 = "Right"
    else:
        text1 = "Center-H"


    val2 = gaze.vertical_ratio()
    cv2.putText(frame, "Vertical Value:  " + str(val2), (90, 450), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    if val2 is not None and val2 < 0.4:
        text2 = "TOP"
    elif val2 is not None and val2 > 0.6:
        text2 = "BOTTOM"
    else:
        text2 = "Center-V"
    



    cv2.putText(frame, text1, (150, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, text2, (150, 400), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    # val = gaze.horizontal_ratio()
    # cv2.putText(frame, "HOrizontal Value:  " + str(val), (190, 300), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    # left_pupil = gaze.pupil_left_coords()
    # right_pupil = gaze.pupil_right_coords()
    # cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    # cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == "q":
        break
   
webcam.release()
cv2.destroyAllWindows()
