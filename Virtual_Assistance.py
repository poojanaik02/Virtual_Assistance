import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def generate_random_greeting():
    greetings = [
        'Hello! I am Friday, How can I help you!!',
        'Hi there! I am Friday, How can I help you!!',
        'Greetings! I am Friday, How can I help you!!',
        'Hey! I am Friday, How can I help you!!',
        'Howdy! I am Friday, How can I help you!!',
        'Salutations! I am Friday, How can I help you!!'
    ]
    return random.choice(greetings)


random_greeting = generate_random_greeting()
talk(random_greeting)
engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who the is' in command:
        person = command.replace('who the is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    

    elif 'set reminder' in command:
            talk('What should I remind you about?')
            reminder_message = take_command()
            talk('In how many seconds?')
            seconds = take_command()
            time.sleep(int(seconds))
            talk('Reminder: ' + reminder_message)
    
    elif 'calculate' in command:
        expression = command.replace('calculate', '')
        result = eval(expression)
        talk('The result is ' + str(result))

    elif 'open website' in command:
        website = command.replace('open website', '')
        talk('Opening ' + website)
        pywhatkit.search(website)

    

    elif 'stop' in command or 'exit' in command:
        talk('Goodbye!')
        exit()

    else:
        talk('Please say the command again')

while True:
    run_friday()
