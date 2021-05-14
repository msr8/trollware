def epic_rr_cure():
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

    try:
        os.remove( f'C:\\Users\\{get_user()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\startup_processes.vbs' )
        print('Succesfully removed')
    except:
        print('File doesnt exist brah')

if __name__ == '__main__':
    epic_rr_cure()
