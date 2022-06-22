import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Bypass import bp
    bp()
elif bit == '32bit':
    os.system('xdg-open https://facebook.com/groups/351076900316263/');time.sleep(2)
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
