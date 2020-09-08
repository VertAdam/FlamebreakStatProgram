"""import numpy as np
import pyautogui
import imutils
import cv2
import matplotlib.pyplot as plt

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Window name in which image is displayed
window_name = 'image'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()"""

import numpy as np
import cv2
from mss import mss
from PIL import Image

bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1000}

sct = mss()

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break