import lyricsgenius
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout
import pathlib
import os
import json
import glob


lyricPath = pathlib.Path(__file__).parent.absolute()
lyricPath = os.path.join(lyricPath, "lyricFiles")

if not os.path.exists(lyricPath):
    os.mkdir(lyricPath)


opts = Options()
opts.set_headless()
opts.add_argument('log-level=3')
opts.add_experimental_option("prefs", {
    "download.default_directory": lyricPath,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enable": True,
    "profile.content_settings.exceptions.automatic_downloads.*.setting": True})
assert opts.headless

for f in os.listdir(lyricPath):
    #try:
    os.remove(os.path.join(lyricPath, f))
    #except:
       # pass

sentence = "daisy daisy give me your answer do"

data = {}
      
def on_button_clicked():
    browser = Chrome(options=opts)
    for word in sentence.split():
        data['word'] = []
        browser.get('https://www.megalobiz.com/lrc/maker/download-music-lyrics-lrc-generated-files')

        search_form = browser.find_element_by_id('lrc_search_phrase')
        search_form.send_keys(word)
        time.sleep(2)
        #results = browser.find_elements_by_class_name("lyrics_member_box")
        lyricsList = browser.find_element_by_class_name("more_content")
        for lyrics in lyricsList:
            lyrics.click()
            
        
        #print(results[0].text)       
        

        download_button = browser.find_elements_by_class_name("lyrics_button")
        download_button[0].click()
        time.sleep(1)
        listofFiles = glob.glob(os.path.join(lyricPath, "*"))
        latestFile = max(listofFiles, key=os.path.getctime)
        
        latestFile = latestFile.rsplit('\\', 1)[-1]
        print(latestFile)

        

        #time.sleep(5)

    # os.chdir(lyricPath)
    # sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
    # for f in os.listdir(lyricPath):
    #     print(f)


    
        

app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel('Hello'))
button = QPushButton('Speak')
button.clicked.connect(on_button_clicked)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()








#genius = lyricsgenius.Genius("lsBPwepMx8EwcFItbejjEY3JDghXUE8SIIndj03-CHFGtoXBTqOOZASvn_I9ntMw")
#result = genius.search_genius_web("hello", 1)
