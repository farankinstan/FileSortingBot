import os
from time import sleep
import shutil


extensions = {

    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv',
              'rm', 'swf', 'vob'],

    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml', 'cfg', 'lua'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],

    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],

    'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],

    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],

    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],

    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],

    'gif': ['gif'],

    'exe': ['exe', 'msi'],

    'theme': ['theme']

}

def config():
    try:
        os.mkdir('C:\\config')
    except:
        pass
    
    try:
        file = open('C:\\config\\config.cfg', 'r')
        return file.readlines()
    except:
        file = open('C:\\config\\config.cfg', 'w')
        file.write('user = auto')
        return file.readlines()

def settings(set):

    #нормализуем информацию
    for line in set:
        normal = line.split('\n')[0]
        set[set.index(line)] = normal
    
    #если юзер установлен не автоматически , то возвращаем его имя
    if set[0].split('user = ')[1] != 'auto':
        return set[0].split('user = ')[1]

    else:
        return 0







#создем нужные папки
def make(ins, docs, image, torr, py, zip, video):
    try:
        os.mkdir(image)
    except:
        pass

    try:
        os.mkdir(video)
    except:
        pass

    try:
        os.mkdir(zip)
    except:
        pass

    try:
        os.mkdir(py)
    except:
        pass

    try:
        os.mkdir(torr)
    except:
        pass
    
    try:
        os.mkdir(docs)
    except:
        pass
    
    try:
        os.mkdir(ins)
    except:
        pass

def main(down, music, video, ins , docs, py, image, torr, zip, dis):
    #получаем список файлов в папке загрузки
    files = os.listdir(down)


    #создем нужные папки
    make(ins, docs, image, torr, py, zip, video)

    #создаем цикл ,который проверяет каждый файл
    for i in files:
        try:
            #получаем расширение файлов
            extl = i.split('.')
            ext = i.split('.')[-1]

            #переносим в нужную папку файл с нужным расширением
            if ext in extensions['audio']:
                shutil.move(down + '\\' + i, music)

            #переносим в нужную папку файл с нужным расширением
            elif ext in extensions['exe']:
                shutil.move(down + '\\' + i, ins)

            #переносим в нужную папку файл с нужным расширением
            elif ext in extensions['presentation'] or ext in extensions['spreadsheet'] or ext in extensions['data'] or ext in extensions['text']:
                shutil.move(down + '\\' + i, docs)

            #переносим в нужную папку файл с нужным расширением
            elif ext in extensions['image']:
                shutil.move(down + '\\' + i, image)
                
            #переносим в нужную папку файл с нужным расширением
            elif ext in extensions['archive']:
                shutil.move(down + '\\' + i, zip)

            #переносим в нужную папку файл с нужным расширением
            elif ext in extensions['video'] or ext in extensions['gif']:
                shutil.move(down + '\\' + i, video)

            #переносим в нужную папку файл с нужным расширением
            elif ext == 'torrent':
                shutil.move(down + '\\' + i, torr)

            #переносим в нужную папку файл с нужным расширением
            elif ext == 'py' or ext == 'pyw':
                shutil.move(down + '\\' + i, py)

            #переносим в нужную папку файл с нужным расширением
            elif extl[-2] in extensions["theme"]:
                shutil.move(down + '\\' + i, dis)

        except:
            pass


if __name__ == '__main__':
    #получаем имя юзера
    Emperor = os.environ.get("USERNAME")

    #создаем конфиг и читаем его
    name = settings(config())

    #устанавливаем пользователя
    if name:
        Emperor = name


    #получаем пути до папок
    down = f"C:\\Users\\{Emperor}\\Downloads"
    music = f"C:\\Users\\{Emperor}\\Music"
    video = f"C:\\Users\\{Emperor}\\Videos\\vid"
    ins = f"C:\\Users\\{Emperor}\\Downloads\\installers"
    docs = f'C:\\Users\\{Emperor}\\Documents\\docs'
    py = f'C:\\Users\\{Emperor}\\Documents\\py'
    image = f'C:\\Users\\{Emperor}\\Pictures\\images'
    torr = f"C:\\Users\\{Emperor}\\Downloads\\torrents"
    zip = f"C:\\Users\\{Emperor}\\Downloads\\zips"
    dis = f'C:\\Users\\{Emperor}\\AppData\\Roaming\\BetterDiscord\\themes'
    
    while True:
        main(down, music, video, ins , docs, py, image, torr, zip, dis)
        sleep(2)