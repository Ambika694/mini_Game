import re
import tempfile
import uuid
import asyncio
import subprocess
import json
import threading
import edge_tts
import pyttsx3  # NEW: offline backup voice (pip install pyttsx3)
from datetime import datetime
import wikipediaapi
import speech_recognition as sr
import webbrowser
import pyscreeze
import pywhatkit
import os
import psutil
import requests
import webview  # pip install pywebview
import comtypes
import time  # comes with pycaw
from pycaw.pycaw import AudioUtilities
import cv2
import pyautogui
import pyjokes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_FILE = os.path.join(BASE_DIR, "jarvis_ui", "index.html")


# ============================================================
# UI BRIDGE  (Python -> HTML orb)
# ============================================================

window = None  # pywebview window, created at the bottom


def ui_state(name):
    """name: idle | listening | thinking | speaking"""
    if window is None:
        return
    try:
        window.evaluate_js(f"window.setState({json.dumps(name)})")
    except Exception:
        pass


def ui_text(who, text):
    """who: 'you' or 'jarvis'"""
    if window is None:
        return
    try:
        window.evaluate_js(f"window.setText({json.dumps(who)}, {json.dumps(text)})")
    except Exception:
        pass


# ============================================================
# WEATHER
# ============================================================
WEATHER_CODES = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Foggy",
    51: "Light Drizzle",
    53: "Drizzle",
    55: "Heavy Drizzle",
    61: "Light Rain",
    63: "Rain",
    65: "Heavy Rain",
    80: "Rain Showers",
    81: "Rain Showers",
    82: "Heavy Rain Showers",
    95: "Thunderstorm",
}


def weather():
    api_url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=19.0760&longitude=72.8777"
        "&current=temperature_2m,weather_code,apparent_temperature,"
        "relative_humidity_2m,wind_speed_10m,precipitation"
    )

    try:
        response = requests.get(api_url, timeout=8)
        data = response.json()
        current = data["current"]
        temperature = current["temperature_2m"]
        weather_code = current["weather_code"]
        feels_like = current["apparent_temperature"]
        humidity = current["relative_humidity_2m"]
    except Exception as error:
        print("WEATHER ERROR:", error)
        speak("Sorry sir, I could not get the weather right now.")
        return

    condition = WEATHER_CODES.get(weather_code, "Cloudy")

    speak(
        f"Temperature is {temperature} degrees Celsius, feels like {feels_like}. "
        f"Weather is {condition}. Humidity is {humidity} percent."
    )


# ============================================================
# JARVIS SETUP
# ============================================================

vol = None
running = True


def init_volume():
    # COM har thread me alag se init karna padta hai (UI ke saath voice loop thread me chalta hai)
    global vol
    comtypes.CoInitialize()
    dev = AudioUtilities.GetSpeakers()
    vol = dev.EndpointVolume


# ============================================================
# TEXT TO SPEECH - OFFLINE BACKUP (pyttsx3)
# ============================================================


def speak(text):

    # pyttsx3.init() yahin andar hai, kyunki voice alag thread me chalti hai
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)  # speed (default ~200)
        engine.setProperty("volume", 1.0)  # 0.0 se 1.0
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as error:
        print("OFFLINE TTS ERROR:", error)


# ============================================================
# TEXT TO SPEECH - EDGE TTS
# ============================================================


# ============================================================
# GREETING
# ============================================================


def wish_me():
    hour = datetime.now().hour

    if 0 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    elif 18 <= hour < 20:
        greeting = "Good evening"
    else:
        greeting = "Good night"

    print("JARVIS:", greeting)
    ui_text("jarvis", greeting)


# ============================================================
# LISTEN
# ============================================================


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("JARVIS: Listening...")
        ui_state("listening")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            # 5 sec tak kuch nahi bola, wapas loop me jao
            ui_state("idle")
            return "none"

    try:
        print("JARVIS: Recognizing...")
        ui_state("thinking")

        query = recognizer.recognize_google(audio)

        print("YOU:", query)
        ui_text("you", query)

        return query.lower()

    except sr.UnknownValueError:
        print("JARVIS: Please say that again.")
        ui_state("idle")
        return "none"

    except sr.RequestError:
        print("JARVIS: Speech service is unavailable.")
        ui_state("idle")
        return "none"


# ============================================================
# VOLUME
# ============================================================


def vol_up(amount):
    try:
        amount = int(amount.replace("increase volume by", "").strip())
        current_vol = int(vol.GetMasterVolumeLevelScalar() * 100)
        new_vol = min(current_vol + amount, 100)
        vol.SetMasterVolumeLevelScalar(new_vol / 100, None)
        print(f"JARVIS: Volume {new_vol}%")
    except ValueError:
        print("JARVIS: Please specify a volume amount.")


def vol_down(amount):
    try:
        amount = int(amount.replace("decrease volume by", "").strip())
        current_vol = int(vol.GetMasterVolumeLevelScalar() * 100)
        new_vol = max(current_vol - amount, 0)
        vol.SetMasterVolumeLevelScalar(new_vol / 100, None)
        print(f"JARVIS: Volume {new_vol}%")
    except ValueError:
        print("JARVIS: Please specify a volume amount.")


def mute_vol():
    vol.SetMute(1, None)
    print("JARVIS: Volume muted.")


def unmute_vol():
    vol.SetMute(0, None)
    print("JARVIS: Volume unmuted.")


# ============================================================
# GOOGLE / YOUTUBE SEARCH
# ============================================================


def search_google(query):
    search_topic = query.replace("search google", "").strip()
    if search_topic:
        webbrowser.open(
            "https://www.google.com/search?q=" + search_topic.replace(" ", "+")
        )


def search_youtube(query):
    search_topic = query.replace("search", "").strip()
    if search_topic:
        pywhatkit.playonyt(search_topic)


# ============================================================
# WIKIPEDIA
# ============================================================

# Kuch common topics jinke "may refer to" page aate hain
WIKI_ALIASES = {
    "python": "Python (programming language)",
    "java": "Java (programming language)",
}


def wiki_search(topic):
    topic = topic.strip()
    if not topic:
        speak("Which topic should I search, sir?")
        return

    topic = WIKI_ALIASES.get(topic.lower(), topic)

    wiki = wikipediaapi.Wikipedia(user_agent="JARVIS/1.0", language="en")
    page = wiki.page(topic)

    if not page.exists():
        speak("Sorry sir, I could not find that on Wikipedia.")
        return

    summary = page.summary

    # "X may refer to:" wale disambiguation page ko pakdo
    is_disambiguation = "may refer to" in summary[:200].lower() or any(
        "disambiguation" in c.lower() for c in page.categories
    )

    if is_disambiguation:
        options = [t for t in page.links if ":" not in t][:3]
        if options:
            speak(
                f"{topic} has many meanings, sir. Did you mean "
                + ", ".join(options)
                + "? Please say it more specifically."
            )
        else:
            speak(f"{topic} has many meanings, sir. Please be more specific.")
        return

    # sirf pehle 2 sentences bolo (lamba text bolne me der lagti hai)
    sentences = re.split(r"(?<=[.!?])\s+", summary)
    short = " ".join(sentences[:2])[:400]

    print("Wikipedia:", short)
    speak(short)


# ============================================================
# JARVIS BRAIN  (free AI API: Gemini ya Groq)
# ============================================================

print("RUNNING FILE:", __file__)


# ============================================================
# COMMAND PROCESSOR
# ============================================================

OPEN_APPS = {
    "chrome": "chrome",  # Windows khud dhoondh leta hai, path ki zarurat nahi
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
}


def open_app(query):
    name = query.lower().replace("open", "").strip()
    for key, target in OPEN_APPS.items():
        if key in name:
            speak(f"Opening {key}")
            try:
                os.startfile(target)
            except Exception as error:
                print("APP ERROR:", error)
                speak("Sorry sir, I could not open that.")
            return
    speak("I don't know that app, sir.")


YOUTUBE_CHANNELS = {
    "mrbeast": "https://www.youtube.com/@MrBeast",
    "carryminati": "https://www.youtube.com/@CarryMinati",
    "t series": "https://www.youtube.com/@tseries",
    "unstop": "https://www.youtube.com/@Unstop2Motiv-19",
}


def open_chel(query):
    naam = query.lower().replace("open channel", "").strip()
    for key, link in YOUTUBE_CHANNELS.items():
        if key in naam:
            print(f"opening {key} ")
            webbrowser.open(link)
            return
    speak("I don't know that Channels, sir")


# take photo
# -------------------------------
def take_pic():
    speak("Taking photo sir")
    vio = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frm = vio.read()
    if ret:
        cv2.imwrite("click.jpg", frm)
        speak("Photo saved sir")
    else:
        speak("Sorry sir, camera nahi khula")
    vio.release()


# -------------------------------

content = {"gkjg": "gk;gkfglkl;kgl;"}


def send_whatsapp(query):
    name = query.lower().replace("send message", "").strip()
    for key, number in content.items():
        if key in name:
            speak("Sending mesange sir")

            pywhatkit.sendwhatmsg_instantly(
                number, "Hello from jarvis", wait_time=15, tab_close=False
            )
            time.sleep(3)
            pyautogui.press("Enter")

            time.sleep(2)
            pyautogui.hotkey("ctrl", "w")
            return
    speak("I don't know this contact, sir.")


# system resrart
def restart_system():
    speak("Are you sure sir? Say yes to confirm")
    reply = listen()

    if "yes" in reply:
        speak("Restarting in 10 seconds, sir. Please save your work.")
        os.system("shutdown /r /t 10")

    else:
        speak("Restart cancelled, sir.")


def shutdown_system():
    speak("Are you sure sir ? Say yes to confirm")
    relpy = license()
    if "yes" in relpy():
        speak(" shutdown  in 10 seconds, sir. Please save your work")
        os.system("stutdown /s /t 10")
    else:
        speak("studown cancelled sir")






speak("Jarvis is online.  how can I help ")



def process_command(query):
    global running

    if query == "none":
        return

    if "hello" in query:
        speak("Hello sir, how can I help")
    elif "open channel" in query:
        open_chel(query)
    elif "send message " in query:
        send_whatsapp(query)

    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "joke" in query:
        speak(pyjokes.pyjokes.get_joke())

    elif "open document" in query:
        speak("Opening documents")
        subprocess.Popen(["explorer", r"C:\Users\ambika\OneDrive\Desktop"])

    elif "open download" in query:
        speak("Opening downloads")
        subprocess.Popen(["explorer", r"C:\Users\hp\Downloads"])

    elif "open work" in query:
        speak("Opening VS Code")
        vscode_path = r"C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        subprocess.Popen([vscode_path, r"C:\Users\hp\OneDrive\Desktop\jarvis"])

    elif "take screenshot" in query:
        speak("Taking screenshot")
        screenshot = pyscreeze.screenshot()
        screenshot.save(r"C:\Users\hp\OneDrive\Desktop\jarvis_screenshot.png")
        print("JARVIS: Screenshot saved.")

    elif "take photo" in query or "photo" in query or "selfie" in query:
        take_pic()

    elif "date" in query or "time" in query:
        now = datetime.now()
        current_date = now.strftime("%d %m %Y")
        current_time = now.strftime("%I:%M %p")
        speak(f"Sir, today is {current_date} and the time is {current_time}")

    elif "wikipedia" in query:
        try:
            topic = query.replace("wikipedia", "").strip()
            wiki_search(topic)
        except Exception as error:
            print(f"Wikipedia error: {error}")
            speak("Sorry sir, Wikipedia is not working right now.")

    elif "file" in query:
        speak("Opening GitHub")
        webbrowser.open("https://github.com/Ambika694/mini_Game")

    elif "chat" in query:
        speak("Opening WhatsApp")
        os.system("start whatsapp:")

    elif "increase volume" in query:
        speak("Increasing volume, sir.")
        vol_up(query)

    elif "decrease volume" in query:
        speak("Decreasing volume, sir.")
        vol_down(query)

    elif "unmute" in query:
        speak("Unmuting the system, sir.")
        unmute_vol()

    elif "mute" in query:
        speak("Muting the system, sir.")
        mute_vol()

    elif "search google" in query:
        speak("Searching Google for you, sir.")
        search_google(query)

    elif "search" in query:
        speak("Searching YouTube for you, sir.")
        search_youtube(query)

    elif "today" in query:
        weather()

    elif "battery" in query:
        battery = psutil.sensors_battery()
        battery_pre = battery.percent
        status = "Charging" if battery.power_plugged else "Not Charging"
        speak(f"Battery Percentage: {battery_pre}% and status: {status}")

    elif query.startswith("open "):
        open_app(query)

    elif "lock" in query:
        speak("Locking system sir")
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif "restart" in query:
        restart_system()
    elif "shutdown" in query:
        shutdown_system()

    elif "quit" in query:
        speak("Understood. Ending the program. Goodbye, sir.")
        running = False
        if window is not None:
            window.destroy()

    else:
        speak("Sorry sir, I don't understand this command.")


# ============================================================
# VOICE LOOP  (background thread me chalta hai)
# ============================================================


def voice_loop():
    # Volume ke liye COM isi thread me init hona chahiye
    try:
        init_volume()
    except Exception as error:
        print("VOLUME INIT ERROR:", error)

    while running:
        ui_state("idle")
        query = listen()  # seedha command suno, wake word nahi
        try:
            process_command(query)
        except Exception as error:
            # koi bhi command fail ho to poora loop band na ho
            print("COMMAND ERROR:", error)
            speak("Sorry sir, something went wrong.")


# ============================================================
# START JARVIS  (UI main thread pe, voice loop alag thread pe)
# ============================================================

if __name__ == "__main__":
    window = webview.create_window(
        "JARVIS",
        UI_FILE,
        width=720,
        height=780,
        background_color="#02060d",
    )

    def on_closed():
        # window band hote hi voice loop ko bhi rok do
        global running
        running = False

    window.events.closed += on_closed
    webview.start(voice_loop)
