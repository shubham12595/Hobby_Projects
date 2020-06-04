import wolframalpha
import wikipedia
import PySimpleGUI as sg

import pyttsx3
engine = pyttsx3.init()

client = wolframalpha.Client('JVG5UK-2TYAEAYTR9')
sg.theme('DarkBlack1')
layout = [  [sg.Text('Enter your Command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
window = sg.Window('IntelHu', layout)
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
    	wiki = wikipedia.summary(values[0], sentences=2)
    	wolf = next(client.query(values[0]).results).text
    	engine.say(wolf)
    	sg.PopupNonBlocking("Wolfram Result: "+wolf,"Wikipedia Result: "+wiki)
    except wikipedia.exceptions.DisambiguationError:
    	wolf = next(client.query(values[0]).results).text
    	engine.say(wolf)
    	sg.PopupNonBlocking(wolf)
    except wikipedia.exceptions.PageError:
        wolf = next(client.query(values[0]).results).text
        engine.say(wolf)
        sg.PopupNonBlocking(wolf)
    except:
    	wiki_res = wikipedia.summary(values[0], sentences=2)
    	engine.say(wiki_res)
    	sg.PopupNonBlocking(wiki_res)

    

    engine.runAndWait()   #This is used to popup Result
window.close()
	
print()