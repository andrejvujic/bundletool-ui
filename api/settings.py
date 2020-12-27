import pickle
import os


class Settings:
    FILE_NAME = 'bundletool-ui-settings.txt'
    DEFAULT_SETTINGS = {'bundletool_path': r'C:\Program Files\bundletool'}
    settings = {}

    def loadSettings(self):
        if (os.path.isfile(self.FILE_NAME)):
            with open(file=self.FILE_NAME, mode='rb') as f:
                settings = pickle.load(f)
        else:
            return self.createSettings()

        return settings

    def createSettings(self):
        with open(file=self.FILE_NAME, mode='wb') as f:
            pickle.dump(self.DEFAULT_SETTINGS, f)

        return self.loadSettings()

    def saveSettings(self, settings):
        with open(file=self.FILE_NAME, mode='wb') as f:
            pickle.dump(settings, f)
