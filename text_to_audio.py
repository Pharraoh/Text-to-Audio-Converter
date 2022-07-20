#import libs
import pyttsx3
engine = pyttsx3.init()

speech = input('Input Text: ') #input text
save = input('Input file name(add extension): ') #choose file name(with extension e.g new.mp3) to save with
gender = input('choose gender: ') #choose gender voice(type 0 for male voice and 1 for female voice)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[int(gender)].id)
engine.say(speech)

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 120) #increase and decrease integer to control speech speed

engine.save_to_file(speech, save)
engine.runAndWait()


#coded by Pharraoh
