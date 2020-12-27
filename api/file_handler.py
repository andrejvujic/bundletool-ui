from tkinter import filedialog


class FileHandler:
    NO_FILE = 'No App Bundle has been choosen'
    CHOOSEN_FILE = ''

    def chooseFile(self, fileLabel):
        temp_file = filedialog.askopenfilename(
            title='Choose App Bundle', filetypes=[('Android App Bundle', '*.aab'), ('All Files', '*.*')])
        if (len(temp_file) > 0):
            self.CHOOSEN_FILE = temp_file
            fileLabel.configure(text=temp_file)
            print(f'[bundletool-ui] Choosen App Bundle: {temp_file}')

    def dirContainsFile(self, file, files):
        return file.split('/')[-1] in files
