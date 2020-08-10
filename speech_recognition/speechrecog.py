import speech_recognition as sr
import win32com.client as wincl
import webbrowser
import requests 
import json

api_key = "tQWGPCnWxqxL"
project_token = "txW1_a4YW24B"
run_token = "tmkTTU97w4USpip3"

run = True

while run:
    response = requests.get(f"https://www.parsehub.com/api/v2/projects/{project_token}/last_ready_run/data", params={"api_key": api_key})   

    speak = wincl.Dispatch("SAPI.SpVoice")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What would you like to do:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
        except:
            print("Sorry could not recognize what you said")

        if text.startswith('search'):
            x = text.split('search')[-1]
            print(x)
            e_website = f"https://www.google.com/search?q={x}&rlz=1C1APWK_enIN766IN766&oq=yo+&aqs=chrome..69i57j0j69i59l2j69i60l4.1394j0j7&sourceid=chrome&ie=UTF-8"
            webbrowser.open_new(e_website)
            

        if (text == 'exit'):
            run = False

        if text.startswith('what is the total number of coronavirus '):
            y = text.split ('what is the total number of coronavirus')[-1]
            y = y.strip()
            


        if text.startswith('open'):
            y = text.split ('open')[-1]
            y = y.strip()
            print(y)
            c_website = f"https://www.{y}.com"
            webbrowser.open_new(c_website)
        
        if text.startswith('what is '):
            z = text.split('what is ')[-1]
            z = z.strip()
            print(z)
            n_website = f"https://en.wikipedia.org/wiki/{z}"
            webbrowser.open_new(n_website)
            continue
            
            
        if (text == 'calculate'):
            r = sr.Recognizer()
            with sr.Microphone() as source2:
                speak.Speak("Do you want to addd, subtract, multiply or divide")
                audio2 = r.listen(source2)
            try:
                text2 = r.recognize_google(audio2)
                print("You said: {}".format(text2))
            except:
                print("Sorry could not recognize what you said")

            calculate = True

            while calculate:         
                if (text2 == 'add'):
                    x = float(input("Enter first number here: "))
                    y = float(input("Enter second number here: "))
                    z = x + y
                    speak.Speak(f"Your answer is {z}")

                elif (text2 == 'subtract'):
                    x = float(input("Enter first number here: "))
                    y = float(input("Enter second number here: "))
                    z = x - y
                    speak.Speak(f"Your answer is {z}")

                elif (text2 == 'multiply'):
                    x = float(input("Enter first number here: "))
                    y = float(input("Enter second number here: "))
                    z = x * y
                    speak.Speak(f"Your answer is {z}")

                elif (text2 == 'divide'):
                    x = float(input("Enter first number here: "))
                    y = float(input("Enter second number here: "))
                    z = x / y
                    speak.Speak(f"Your answer is {z}")

                elif (text2 =='exit calculator'):
                    calculate = False
                        
                else:
                    print("Unrecognized command. Please try again.")