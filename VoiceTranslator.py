import googletrans 
import speech_recognition 
import gtts 
import playsound 

input_lang="en"
output_lang="bn"

recognizer=speech_recognition.Recognizer() 
with speech_recognition.Microphone()  as source:
    print("Speak now")
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language="en")
    print(text)
     
translator=googletrans.Translator()
translation=translator.translate(text,dest="bn")
print(translation.text)
#bangla audio
converted_audio=gtts.gTTS(translation.text,lang="bn")
converted_audio.save("audiobn.mp3")
playsound.playsound("audiobn.mp3")

#hindi audio
translator1=googletrans.Translator()
translation1=translator1.translate(text,dest="hi")
print(translation1.text)
converted_audio1=gtts.gTTS(translation1.text,lang="hi")
converted_audio1.save("audiohi.mp3")
playsound.playsound("audiohi.mp3")

#hindi audio
translator2=googletrans.Translator()
translation2=translator1.translate(text,dest="fr")
print(translation2.text)
converted_audio1=gtts.gTTS(translation2.text,lang="fr")
converted_audio1.save("audiofr.mp3")
playsound.playsound("audiofr.mp3")