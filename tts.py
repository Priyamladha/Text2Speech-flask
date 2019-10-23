from gtts import gTTS 

# mytext = 'mrahank'
def changetoaudio(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("static/welcome.mp3")

