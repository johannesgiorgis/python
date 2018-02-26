# author: Michael Chen
from googletrans import Translator
from gtts import gTTS
import os

language = 'en'
in_string = 'vía con dios'
translator = Translator()
oput = translator.translate(in_string, dest=language)
myobj = gTTS(text=oput.text, lang=language, slow=False)
myobj.save('translationtest.mp3')

# need mpg321 application to work fully
#os.system("mpg321 translationtest.mp3")