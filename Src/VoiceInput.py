import speecch_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
  print(' Use "Turn on Strike zone" and "Turn off strike zone" to activate and disactivate strike zone box & tracking ')
  audio = r.listen(source)

  try:
    command = r.recognize_google(audio)
    if "turn on strike zone" in command:
       pass
    if "turn off strike zone" in command:
       pass 
  except sr.UnknownValueError:
    print("FATAL SERVER ERROR: @repo:sawyerWetson/SmartUmpires/Src/VoiceInput.py "System can not resolve audio" ")
  
     
