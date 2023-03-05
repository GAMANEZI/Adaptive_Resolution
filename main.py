import re
import os
from screeninfo import get_monitors

def adaptive_res(path):
    # path - наш путь к файлу с настройками игры. Для Uderlords он выглядит так (...\SteamLibrary\steamapps\common\Underlords\game\dac\cfg\video.txt)

    # получение разрешения экрана основного монитора
    for m in get_monitors():
        if m.is_primary == True:
            myresW = m.width
            myresH = m.height

    # считывание файла настроек игры
    with open(path, 'r') as f:
        old_data = f.read()
    data = old_data.split('\n')

    # изменение соответствующих параметров согласно полученным значениям разрешения дисплея, с помощью библиотеки регулярных выражений
    new_data = ''
    for item in data:
        #ширина
        if re.search('"setting.defaultres"', item):
            item = f'	\"setting.defaultres\"		\"{myresW}\"'
        #высота
        if re.search('"setting.defaultresheight"', item):
            item = f'	\"setting.defaultresheight\"		\"{myresH}\"'
        #полноэкранный режим, по желанию можно сменить 1 на 0 для перехода в оконный режим
        if re.search('"setting.fullscreen"', item):
            item = f'	\"setting.fullscreen\"		\"{1}\"'
        new_data += item + '\n'

    # запись данных в файл настроек
    with open(path, 'w') as f:
        f.write(new_data)


#применение функции адапивного разрешения
adaptive_res(r"E:\SteamLibrary\steamapps\common\Underlords\game\dac\cfg\video.txt")
#запуск игры
os.system('start open_game.bat')
