import webbrowser
import time
from pykeyboard import PyKeyboard

count = 0
urls = ['http://usheethe.com/j26W']
k = PyKeyboard()

while count != 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        k.press_keys(['Command','W'])
        count = count + 1 
    
else:
    pass