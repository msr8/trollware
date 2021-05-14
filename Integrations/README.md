# What is this?
<br>

This page explains the working of the malwares/cures and what parameters they use and how you can integrate them into your own programs. You can copy the functions from harmless-malwares.py or import them from there

<br>

# Explanation
<br>

## cantdeleteme.py
<br>

**How it works:** First of all, it creates a .py file which writes the file you have specified in your specified location every 5 minutes. Ifthe file already exists, then it overwrites it. Then, it creates a .bat file in your specified location which triggers the .py file. Then lastly, it creates a .vbs file in the startup folder of windows (ie `C:\Users\{User}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`) which triggers the .bat file and then, the .bat file executes the .py file. Now since the .vbs file is in the startup folder, it will be executed everytime the victim boots up the device, thus the python file will always be active in the background whenever the device will be running. Now you might ask why didnt i just put the .py or the .bat file in the startup folder instead of making the 3 different files, that is because if we directly put the .py or .bat files in the startup folder, they open up a console, and thus the user can stop the execution of the program anytime by closing that console window. By default, the file is a .jpeg file of jerma sus with the name "When {user} is sus.jpeg"

<br>

**Parameters Required:** 

``file_data``: The bytes form of the file that you will be creating constantly, which the victim wont be able to delete

``file_path``: The directory where the file would be created, as well as its name and extension. For eg: `C:\Users\User\Desktop\sus.jpeg`

``py_file_path``: The path of the .py file. For eg: `C:\Users\User\Documents\randomname.py`

``bat_file_path``: The path of the .bat file. For eg: `C:\Users\User\Documents\randomname.bat`
