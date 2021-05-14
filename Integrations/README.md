# What is this?
<br>

This page explains the working of the malwares/cures and what parameters they use and how you can integrate them into your own programs. You can copy the functions from harmless-malwares.py or import them from there

<br>

# Explanation

## cantdeleteme.py
<br>

**How it works:** First of all, it creates a .py file which writes the file you have specified in your specified location every 5 minutes. If the file already exists, then it overwrites it. Then, it creates a .bat file in your specified location which triggers the .py file. Then lastly, it creates a .vbs file in the startup folder of windows (ie `C:\Users\{User}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`) which triggers the .bat file and then, the .bat file executes the .py file. Now since the .vbs file is in the startup folder, it will be executed everytime the victim boots up the device, thus the python file will always be active in the background whenever the device will be running. Now you might ask why didnt i just put the .py or the .bat file in the startup folder instead of making the 3 different files, that is because if we directly put the .py or .bat files in the startup folder, they open up a console, and thus the user can stop the execution of the program anytime by closing that console window. By default, the file is a .jpeg file of jerma sus with the name "When {user} is sus.jpeg"

<br>

**Parameters Required:** 

``file_data``: The bytes form of the file that you will be creating constantly, which the victim wont be able to delete. Must be a string in bytes format. For eg: `b"hello"`

``file_path``: The directory where the file would be created, as well as its name and extension. Must be a string. For eg: `"C:\Users\User\Desktop\sus.jpeg"`

``py_file_path``: The path of the .py file. Must be a string. For eg: `"C:\Users\User\Documents\randomname.py"`

``bat_file_path``: The path of the .bat file. Must be a string. For eg: `"C:\Users\User\Documents\randomname.bat"`

<br>

## epic-rr.py
<br>

**How it works:** It is very very similar to cantdeleteme.py. First of all, it creates a .py file which waits 2 minutes, and the rickrolls the victim (ie opens up the link https://youtu.be/dQw4w9WgXcQ in the default browser) and then, it rickrolls the user again every hour. Then, it creates a .bat file in your specified location which triggers the .py file. Then lastly, it creates a .vbs file in the startup folder of windows (ie `C:\Users\{User}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`) which triggers the .bat file and then, the .bat file executes the .py file. Now since the .vbs file is in the startup folder, it will be executed everytime the victim boots up the device, thus the python file will always be active in the background whenever the device will be running. Now you might ask why didnt i just put the .py or the .bat file in the startup folder instead of making the 3 different files, that is because if we directly put the .py or .bat files in the startup folder, they open up a console, and thus the user can stop the execution of the program anytime by closing that console window

<br>

**Parameters Required:** 

``py_file_path``: The path of the .py file. Must be a string. For eg: `"C:\Users\User\Documents\randomname.py"`

``bat_file_path``: The path of the .bat file. Must be a string. For eg: `"C:\Users\User\Documents\randomname.bat"`

<br>

## linkspam.py
<br>

**How it works:** As soon as the program is executed, it opens a given number of randomly selected links from a given list

<br>

**Parameters Required:** 

``lis``: List of all the links which can be selected. Must have https:// in the beginning. Must be a list or a tuple contaning strings. For eg: `['https://youtu.be/dQw4w9WgXcQ', 'https://youtu.be/Cj8n4MfhjUc', 'https://youtu.be/Mg02NzsXrJk']`

``times``: Number of randomly selected links. Must be an integer. For eg: ``20``

<br>

## photo-rotater.py
<br>

**How it works:** As soon as the program is executed, it goes through the provided list, and for the paths in them, it rotates all the .jpeg .jpg and .png files in that directory and its subdirectory. It rotates them 90° counter-clockwise. The cure just rotates them 90° clockwise

<br>

**Parameters Required:** 

``paths``: List of all paths which the program will go through. Must be a list or a tuple containing strings. For eg: `['C:\Users\User\Desktop', 'C:\Users\User\Pictures']`

<br>

# How do I integrate these into my own program?

You can copy the functions from harmless-malwares.py or import them from there. By doing so, you can customise the parameters and you can integrate these malwares into a logic bomb or a time bomb