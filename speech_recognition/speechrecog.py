import speech_recognition as sr
import win32com.client as wincl
import webbrowser

speak = wincl.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Give commands :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

if (text == 'open Gmail'):
    a_website = "https://www.gmail.com"
    webbrowser.open_new(a_website)

if (text == 'open YouTube'):
    b_website = "https://www.youtube.com"
    webbrowser.open_new(b_website)

if text.startswith('search'):
    x = text.split('search ')
    y = text.split(f'search {x} ')[-1]
    print(y)

if (text == 'open Edmodo'):
    c_website = "https://www.edmodo.com"
    webbrowser.open_new(c_website)

if (text == 'open stackoverflow'):
    d_website = "https://www.stackoverflow.com"
    webbrowser.open_new(d_website)

if (text == 'calculate'):
    with sr.Microphone() as source2:
        speak.Speak('Do you want to add, subtract, multiply or divide.')
        audio2 = r.listen(source2)
        text2 = r.recognize_google(audio2)
        print(text2)
        
    if (text2 == 'add'):
        x = float(input("Enter first number here: "))
        y = float(input("Enter second number here: "))
        z = x + y
        speak.Speak(f"Your answer is {z}")

    if (text2 == 'subtract'):
        x = float(input("Enter first number here: "))
        y = float(input("Enter second number here: "))
        z = x - y
        speak.Speak(f"Your answer is {z}")

    if (text2 == 'multiply'):
        x = float(input("Enter first number here: "))
        y = float(input("Enter second number here: "))
        z = x * y
        speak.Speak(f"Your answer is {z}")

    if (text2 == 'divide'):
        x = float(input("Enter first number here: "))
        y = float(input("Enter second number here: "))
        z = x / y
        speak.Speak(f"Your answer is {z}")



    











