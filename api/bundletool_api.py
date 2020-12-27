from .file_handler import FileHandler
from .settings import Settings
from time import sleep
import os

handler = FileHandler()
settings = Settings()


class BundletoolApi:
    userSettings = settings.loadSettings()
    BUNDLETOOL_PATH = userSettings['bundletool_path']

    def createAPKs(self, appBundle, buttonApks, buttonUviersalAPK, universal=False):
        self.deleteOldAPKs(appBundle)
        os.chdir(self.BUNDLETOOL_PATH)
        os.popen(self.getCreateAPKsCommand(appBundle, universal))
        self.waitForFinish(appBundle, buttonApks, buttonUviersalAPK,)

    def getCreateAPKsCommand(self, appBundle, universal):
        UNIVERSAL_MODE = ' --mode=universal'
        NORMAL_MODE = ''

        return f'java -jar bundletool.jar build-apks --bundle={appBundle} --output={self.getAPKsPath(appBundle)}{UNIVERSAL_MODE  if universal else NORMAL_MODE }'

    def getInstallAPKsCommand(self, appBundle, deviceId):
        HAS_DEVICE_ID = f' --device-id={deviceId}'
        NO_DEVICE_ID = ''

        return f'java -jar bundletool.jar install-apks --apks={self.getAPKsPath(appBundle)}{HAS_DEVICE_ID if len(deviceId) > 0 else NO_DEVICE_ID}'

    def installAPKs(self, appBundle, deviceId):
        os.chdir(self.getAPKsDir(appBundle))
        if(handler.dirContainsFile(self.getAPKsPath(appBundle), os.listdir())):
            os.chdir(self.BUNDLETOOL_PATH)
            os.popen(self.getInstallAPKsCommand(appBundle, deviceId))
        else:
            print('[bundletool-ui] APKs not found.')

    def getAPKsPath(self, appBundle):
        return appBundle[::-1].replace('.aab'[::-1], '.apks'[::-1])[::-1]

    def getAPKsDir(self, appBundle):
        return appBundle[::-1][appBundle[::-1].index('/'):][::-1]

    def deleteOldAPKs(self, appBundle):
        file = self.getAPKsPath(appBundle)
        APKs = file.split('/')[-1]

        if (os.path.isfile(file)):
            os.chdir(self.getAPKsDir(appBundle))
            os.popen(f'del {APKs}')
            print('[bundletool-ui] Deleted old APKs.')

    def waitForFinish(self, appBundle, buttonAPKs, buttonUviersalAPK,):
        os.chdir(self.getAPKsDir(appBundle))

        APKsPath = self.getAPKsPath(appBundle)
        print('[bundletool-ui] Creating APKs...')
        while not handler.dirContainsFile(APKsPath, os.listdir()):
            pass

        buttonAPKs.configure(state='normal')
        buttonUviersalAPK.configure(state='normal')
        print('[bundletool-ui] APKs created.')
