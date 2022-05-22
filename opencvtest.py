# Program To Read video
# and Extract Frames
from multiprocessing.connection import wait
import cv2
import datetime
import time 
import numpy as np

# TODO: SET FPS here. If your video is 30fps, VIDEO_FPS should be set to 30 * 3, etc. 
VIDEO_FPS = 180 # skip by 3 seconds; default 60 fps 
# Function to extract frames
def FrameCapture(path):
      
    # Path to video file
    vidObj = cv2.VideoCapture(path)
  
    # Used as counter variable
    count = 0
  
    # checks whether frames were extracted
    success = 1

    # code for getting initlal roi from frame. selectROI pauses program to draw rectangle by user. get coordinates once and hardcode it. 
    # im = cv2.imread("images\\frame4560.jpg")
    # roi = cv2.selectROI(im) # (1967, 5, 584, 377  | (1861, 0, 690, 387) | (1894, 121, 655, 258)
    # print(roi) 
    # img = cv2.imread("images\\valotest2.png")
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # new against KillJoy
    lower_val_yellow = np.array([26, 106, 0]) 
    upper_val_yellow = np.array([32, 135, 255])

    lower_val_green = np.array([73, 87, 123])
    upper_val_green = np.array([91, 125, 194])


    # mask = cv2.inRange(hsv, lower_val_green, upper_val_green)
    # # if there are any white pixels on mask, sum will be > 0
    # hasGreen = np.sum(mask)
    # if hasGreen > 0:
    #     print('green detected!')

    # # Threshold the HSV image - any yellow color will show up as white
    # mask = cv2.inRange(hsv, lower_val, upper_val)
    # # if there are any white pixels on mask, sum will be > 0
    # hasYellow = np.sum(mask)
    # if hasYellow > 0:
    #     print('Duel detected!')


    # # show image 
    # # apply mask to image
    # res = cv2.bitwise_and(img,img,mask=mask)
    # fin = np.hstack((img,res))
    # display image
    # cv2.imshow("Res", fin)
    # cv2.imshow("Mask", mask)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    duelCount = 0 
    y = 0 
    g = 0 
    both = 0 
    while success:
  
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
  
        # Saves the frames with frame-count | remove microseconds. 
        # timestamp = datetime.timedelta(milliseconds=vidObj.get(cv2.CAP_PROP_POS_MSEC))
        # timestamp -= datetime.timedelta(microseconds=timestamp.microseconds) 

        # get timestamp from frames_watched (counter). 
        timestamp = time.strftime('%H_%M_%S', time.gmtime(count // 60))

        # get kill feed bound 
        # select region 
        # image = image[c1:c1+25,r1:r1+25]
        cropped_image = image[121:258+121, 1894: 1894 + 655]
        
        userColorDetected = allyColorDetected = False

        

        # convert image to HSV 
        hsv = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
        # Threshold the HSV image - any yellow color will show up as white
        mask = cv2.inRange(hsv, lower_val_yellow, upper_val_yellow)
        hasYellow = np.sum(mask)
        if hasYellow > 100000:

            userColorDetected = True 
            y += 1 
            # print(hasYellow)
            # cv2.imshow("og", cropped_image)
            # cv2.imshow("yellow", mask)
            # cv2.waitKey()
            # print('Duel detected!', str(timestamp), hasYellow)
            # cv2.imwrite("images\\duel%d_%s.jpg" %(count, str(timestamp)), image)
            # cv2.imwrite("images\\duel%d_%s.jpg" %(count, str(hasYellow)), image)

        # low  113730
        # high 230010

        # if there are any white pixels on mask, sum will be > 0
        mask = cv2.inRange(hsv, lower_val_green, upper_val_green)
        hasGreen = np.sum(mask)
        if 7000000 > hasGreen > 400000:
            allyColorDetected = True 
            g += 1 

        if allyColorDetected and userColorDetected: 
            both += 1 
            # cv2.imshow("og", cropped_image)
            # cv2.imshow("yellow", mask)
            # cv2.waitKey()

            print(str(timestamp))
            # TODO : uncomment below to save "duel detected" frames for debugging
            # cv2.imwrite("images\\test%d_%s.jpg" %(count, str(timestamp)), image)
        # print(count, timestamp)

        count += VIDEO_FPS 
        vidObj.set(cv2.CAP_PROP_POS_FRAMES, count)
  
        # count += 1

    print(duelCount)
  
# Driver Code
if __name__ == '__main__':
  
    # Calling the function
    # TODO: Link recording file here
    # FrameCapture("C:\\Users\\Admin\\Videos\\Valorant\\LINK_RECORDING_HERE.mp4")
