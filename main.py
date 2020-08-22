import neural_style
import shelve
import os
import subprocess
from shutil import copyfile, rmtree
from alert import send_alert
from NoSleepScript import *
from send2trash import send2trash

osSleep = None
#in Windows, prevent the OS from sleeping while we run
if os.name == 'nt':
    osSleep = WindowsInhibitor()
    osSleep.inhibit()

spaghetti_bot_path = "./images"
waifu_2x_path = "./waifu2x-caffe/waifu2x-caffe-cui.exe"
iterations = 2000
number_to_process = 7
manual_number = False

try:
    s = shelve.open("data")
    if manual_number:
        image_number = 3750
        first_image_number = image_number
        day_number = 444
    else:
        try:
            image_number = int(s.get("image_number"))
            first_image_number = image_number
            day_number = int(s.get("day_number")) + 1
        except TypeError:
            image_number = 3750
            first_image_number = image_number
            day_number = 444


    day_folder = os.path.join(spaghetti_bot_path, "NEWdone" + str(day_number))
    day_folder_upscaled = os.path.join(spaghetti_bot_path, "NEWdoneupscaled" + str(day_number))
    original_folder = os.path.join(spaghetti_bot_path, "original" + str(day_number))

    try:
        rmtree(day_folder)
        rmtree(day_folder_upscaled)
        rmtree(original_folder)
    except(FileNotFoundError):
        print("Nothing Deleted")

    if not os.path.isdir(day_folder):
        os.mkdir(day_folder)
        os.mkdir(day_folder_upscaled)
        os.mkdir(original_folder)

    for i in range(image_number, image_number + number_to_process):
        current_image = os.path.join(spaghetti_bot_path, "rips4", str(i) + ".jpg")
        progress_message = "FINISHED IMAGE NUMBER " + str((i - image_number) + 1)
        copyfile(current_image, os.path.join(original_folder, str(i) + ".jpg"))
        neural_style.do_spaggy(current_image, spaghetti_bot_path, day_folder, i, progress_message, iterations)

    subprocess.call([waifu_2x_path, "--input_path", day_folder, "-e", ".jpg", "-m", "noise_scale", "-s", "2.0", "-n",
                     "3", "-p", "cudnn", "-q", "97", "-b", "4", "--output_path", day_folder_upscaled])

    send2trash(day_folder)

    s["image_number"] = image_number + number_to_process
    s["first_image_number"] = first_image_number
    s["day_number"] = day_number
    s["new_day"] = True
    s.close()

    if osSleep:
        osSleep.uninhibit()

    print("FINISHED")

except Exception as e:
    send_alert(str(e))
    raise
