from api.file_handler import FileHandler
from api.bundletool_api import BundletoolApi
from tkinter import Tk, Button, Label, Entry, messagebox
import threading

FONT = ('Arial', 12)
ALIGNMENT = 'W'
PADDING = 10

handler = FileHandler()
bundletool = BundletoolApi()


def startCreating(isUniversal=False):
    if (len(handler.CHOOSEN_FILE)):
        thread = threading.Thread(target=lambda: bundletool.createAPKs(
            handler.CHOOSEN_FILE, buttonAPKs, buttonUnviersalAPK, isUniversal))
        thread.start()
        buttonAPKs.configure(state='disabled')
        buttonUnviersalAPK.configure(state='disabled')
    else:
        print('[bundletool-ui] No App Bundle Selected')


def startInstalling():
    if (len(handler.CHOOSEN_FILE)):
        print('[bundletool-ui] Installing APKs...')
        deviceId = ADBdeviceId.get() or ''
        bundletool.installAPKs(handler.CHOOSEN_FILE, deviceId)
    else:
        print('[bundletool-ui] No App Bundle Selected')


win = Tk()
win.title('bundletool-ui')
win.resizable(True, False)
Button(win, font=FONT, text='Choose an App Bundle (.aab)',
       relief='groove', command=lambda: handler.chooseFile(fileLabel=fileLabel)).grid(row=0, column=0, sticky=ALIGNMENT)
fileLabel = Label(
    win, font=FONT, text=f'{handler.CHOOSEN_FILE if len(handler.CHOOSEN_FILE) > 0 else handler.NO_FILE}')
fileLabel.grid(row=1, column=0, sticky=ALIGNMENT, pady=PADDING)

buttonAPKs = Button(win, font=FONT, text='Create APKs', width=35,
                    relief='groove', command=lambda: startCreating(False))
buttonAPKs.grid(row=2, column=0, sticky=ALIGNMENT)

buttonUnviersalAPK = Button(win, font=FONT, text='Create Universal APK',
                            width=35, relief='groove', command=lambda: startCreating(True))
buttonUnviersalAPK.grid(row=3, column=0, sticky=ALIGNMENT)

ADBdeviceId = Entry(win, font=FONT, relief="groove", borderwidth=2, width=37)
ADBdeviceId.grid(row=4, column=0, sticky=ALIGNMENT, pady=PADDING)
ADBdeviceId.insert(0, 'adb device id')

installAPKs = Button(win, font=FONT, text='Install APKs', width=35,
                     relief='groove', command=startInstalling)
installAPKs.grid(row=5, column=0, sticky=ALIGNMENT)
win.mainloop()
