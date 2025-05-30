import speecch_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
  print(' Use "Turn on Strike zone" and "Turn off strike zone" to activate and disactivate strike zone box & tracking ')
  audio = r.listen(source)

  try:
    command = 
