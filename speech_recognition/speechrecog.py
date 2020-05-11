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

if text.startswith('search'):
    x = text.split('search')[-1]
    print(x)
    e_website = f"https://www.google.com/search?q={x}&rlz=1C1APWK_enIN766IN766&oq=yo+&aqs=chrome..69i57j0j69i59l2j69i60l4.1394j0j7&sourceid=chrome&ie=UTF-8"
    webbrowser.open_new(e_website)

if text.startswith('open'):
    y = text.split ('open')[-1]
    y = y.strip()
    print(y)
    c_website = f"https://www.{y}.com"
    webbrowser.open_new(c_website)

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



    











