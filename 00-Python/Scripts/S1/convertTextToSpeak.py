from gtts import gTTS
import vlc

myobj = gTTS(text='مساء الفل ',lang= 'ar',slow= False)

myobj.save("welcome.mp4")

p = vlc.MediaPlayer("./welcome.mp4")
p.play()
while True:
    pass

