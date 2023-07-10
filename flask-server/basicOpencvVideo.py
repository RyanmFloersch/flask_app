import cv2
import cvlib as cv
# Drawbox draws a box around detected objects
from cvlib.object_detection import draw_bbox

# https://www.youtube.com/watch?v=V62M9d8QkYM

# Sets up the video capture. Allowing access to your camera.  
video = cv2.VideoCapture(0)

while True:
    # With the video capture unpack each frame into a variable called frame.
    ret,frame = video.read()

    # detect object from the frame.
    # use bbox to set up frame around object.
    # label is the label for the object
    # conf is decimal numbers for object identification
    bbox, label, conf = cv.detect_common_objects(frame)
    
    # tell it where to draw the box 
    # draw_bbox
    #   frame - frame/image its making the box around
    #   bbox - the box its going to draw around
    #   label - the object label
    output_image = draw_bbox(frame, bbox, label, conf)

    # Show the image
    cv2.imshow("Object Detection", output_image)

    # If waitKey and user hits q break out of loop.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
 

