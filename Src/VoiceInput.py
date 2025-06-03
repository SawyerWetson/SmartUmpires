import speecch_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
  print(' Use "Turn on Strike zone" and "Turn off strike zone" to activate and disactivate strike zone box & tracking ')
  audio = r.listen(source)

  try:
    command = r.recognize_google(audio)
    if "turn on strike zone" in command:
       with open("strikezone_state.txt", "w") as f:
         f.write("On")
    if "turn off strike zone" in command:
      with open("strikezone_state.txt", "w") as f:
        f.write("off")
      
  except sr.UnknownValueError:
    print(' <Error Stream> stderr: FATAL SERVER ERROR: @repo:sawyerWetson/SmartUmpires/Src/VoiceInput.py "System can not resolve audio" Please report or email to sawyer.wetson@gmail.com or @sawyerwetson at github')
  
     
