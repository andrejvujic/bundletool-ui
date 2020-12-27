
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
