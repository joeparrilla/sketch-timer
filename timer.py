import time
from os import listdir
from PIL import Image

dir_list = listdir("/home/joe/Pictures")

duration = int(input("How many minutes?")) * 60
inp = input("Press any key to start the timer...")
counter = 0
img_index = 0

curr_time = time.time()
start_time = curr_time

while curr_time - start_time < duration:
        if curr_time + 1 < time.time():
                print(duration - counter)

                im = Image.open(f"/home/joe/Pictures/{dir_list[img_index]}")
                im.show()
                img_index += 1

                counter+=1
                curr_time = time.time()

        