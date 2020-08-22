# Spaghentai-Bot

The source code for Spaghentai-Bot on Reddit. https://www.reddit.com/user/Spaghentai-Bot

Before using, Neural Style Transfer must be set up. Instructions for doing this on Windows can be found here: https://www.reddit.com/user/Spaghentai-Bot/comments/alwyor/how_to_make_your_own_spaghetti_images_on_windows/

Running main.py will take images from the ./images/rips4 folder and spaghettify them 7 at a time. The images in the folder must be .jpg, and named sequentially, eg: 20.jpg, 21.jpg, 22.jpg, etc. It will also upscale them using Waifu2X caffe. 

Poster.py posts the images to Reddit. It first uploads the spaghettified and original images to Imgur, then posts them to the /r/SpaghettiHentai subreddit.

Alert.py simply sends an email if an error occurs. I made it because I run Spaghentai-Bot on a remote PC, so if something goes wrong it's easy to miss



Disclaimer: I'm still learning Python, but this is still 100x better than the previous version, which was a giant mess of Python and Batch scripts (I stored variables in text files!). I know it's lacking in-line comments and documentation, but it really isn't intended to be widely used. But, if you have improvments, I definetly welcome any pull requests!
