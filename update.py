import shutil
import os
path = r'D:\PycharmProjects\textengines'
files = os.listdir(path)
for file in files:
    if file[-3:] == '.py':
        shutil.copy2(os.path.join(path, file), r'D:\PycharmProjects\ElectroProject\venv\Lib\site-packages\textengines')