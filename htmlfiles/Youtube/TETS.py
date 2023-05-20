from gtts import gTTS

text = "Don't forget to subscribe, hope to see you in the next video byee!"

tts = gTTS(text=text, lang="en" , tld="co.uk")

tts.save("s20.mp3")
