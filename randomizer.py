import cv2
import random


def show_wait_destroy(name, img):
    cv2.imshow(name, img)
    cv2.moveWindow(name, 0, 0)
    cv2.waitKey(0)
    cv2.destroyWindow(name)


src = cv2.imread('mandle.jpg')
arr_of_colors = cv2.split(src)
random.shuffle(arr_of_colors)

merge_image = cv2.merge(arr_of_colors)
show_wait_destroy('merged', merge_image)
