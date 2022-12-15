import os
from time import sleep
import shutil
import json

Directories = {}

def Data(emperor = False, load = False):
    global Directories
    
    if not emperor:
        emperor = os.environ.get("USERNAME")

    if load:
        Directories = load
        return


    Directories = {
        "target" : f"C:\\Users\\{emperor}\\Downloads",

        "user" : f"{emperor}",

        "paths" : {
            f"C:\\Users\\{emperor}\\Videos\\vid": ["gif", 'mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv', 'rm', 'swf', 'vob'],

            f"C:\\Users\\{emperor}\\Music": ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],

            f"C:\\Users\\{emperor}\\Pictures\\images": ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],

            f"C:\\Users\\{emperor}\\Downloads\\zips": ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

            f"C:\\Users\\{emperor}\\Documents\\docs": ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml', 'cfg', 'lua', 'pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt','pptx', 'ppt', 'pps', 'key', 'odp', 'xlsx', 'xls', 'xlsm', 'ods'],

            f"C:\\Users\\{emperor}\\Documents\\py": ["py", "pyw"],

            f"C:\\Users\\{emperor}\\Downloads\\installers": ['exe', 'msi'],

            f"C:\\Users\\{emperor}\\AppData\\Roaming\\BetterDiscord\\themes": ['theme']
            }
    }

def Transfer(file, path):
    b = True

    filel = file.split(".")

    while b:
        try:
            shutil.move(file, path)
            b = False

        except:
            filel[-2] = filel[-2] + "1"
            filen = ".".join(filel)

            filel = filen.split(".")

            os.rename(file,filen)
            os.remove(file)

            file = filen

def GetExtention(ext):
    ext = ext.split('.')
    return ext[-1]

def Create():
    if os.path.exists('C:\\config'):
        with open("C:\\config\\config.json") as file:
            jsn = json.load(file)

            if os.environ.get("USERNAME") != jsn["user"]:
                Data(jsn["user"], jsn)
                return

            Data(load = jsn)
            return

    os.mkdir('C:\\config')

    with open("C:\\config\\config.json", "w") as config:
        Data()
        jsn = json.dumps(Directories, indent = 2)
        config.write(jsn)
        

def Sort():

    for i in Directories["paths"].keys():  

        if not os.path.exists(i):

            try:
                os.mkdir(i)
            except:
                pass

    files = os.listdir(Directories['target'])

    for file in files:
        try:

            extention = GetExtention(file)

            for path in Directories['paths']:
                if extention in Directories['paths'][path]:
                    Transfer(Directories["target"] + "\\" + file, path)

        except:
            pass
    

            


if __name__ == '__main__':
    
    Create()
    
    while True:
        Sort()
        sleep(0.5)

