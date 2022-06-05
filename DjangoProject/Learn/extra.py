import os
from gtts import gTTS

text = 'Hello How are you fine thank you'

language = 'fr'

myobj = gTTS(text=text, lang=language, slow=False)

myobj.save("welcome.mp3")
os.system("afplay welcome.mp3")