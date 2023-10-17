import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from decision_tree import Decision_Tree


data = pd.read_csv("./Covid_Dataset.csv")
label = "COVID-19"

dt = Decision_Tree(data, label)

tree = dt.build_tree()
node = tree

Questions = {
    "Breathing Problem": "Do you have any symptoms related to respiratory issues?",
    "Fever": "Have you experienced a fever recently?",
    "Dry Cough": "Do you have a dry cough?",
    "Sore throat": "Are you currently experiencing a sore throat?",
    "Running Nose": "Have you been dealing with a running nose?",
    "Asthma": "Do you have a history of asthma?",
    "Chronic Lung Disease": "Have you been diagnosed with any chronic lung disease?",
    "Headache": "Have you been experiencing headaches lately?",
    "Heart Disease": "Do you have any heart disease or related conditions?",
    "Diabetes": "Have you been diagnosed with diabetes?",
    "Hyper Tension": "Do you have high blood pressure or hypertension?",
    "Fatigue": "Have you been feeling fatigued?",
    "Gastrointestinal": "Have you experienced any gastrointestinal symptoms?",
    "Abroad travel": "Have you traveled abroad recently?",
    "Contact with COVID Patient": "Have you come into contact with someone who has been diagnosed with COVID-19?",
    "Attended Large Gathering": "Have you attended any large gatherings recently?",
    "Visited Public Exposed Places": "Have you visited any public exposed places recently?",
    "Family working in Public Exposed Places": "Does any member of your family work in public exposed places?",
    "Wearing Masks": "Are you consistently wearing masks in public?",
    "Sanitization from Market": "Are you regularly sanitizing yourself and your belongings after visiting markets?",
}

QnA = {
    "hello": "Hello, how can I help you?",
    "hi": "Hello, how can I help you?",
    "good morning": "Hello, how can I help you?",
    "good day": "Hello, how can I help you?",
    "hey": "Hello, how can I help you?",
    "is breathing problems a symptom of covid?": "Yes, having breathing problems can be a symptom of covid, if you want to test yourself for covid, let me know by asking me *Do I have covid?*",
    "does travelling abroad cause covid?": "Travelling abroad will almost certainly infect you with covid, if you need to test yourself for covid, ask me *Do I have corona?*",
    "what is coronavirus?": "Coronaviruses are a family of viruses that typically cause mild respiratory infections like the common cold but also more severe (and potentially deadly) infections. They are zoonotic diseases, meaning they are transmitted from animals to people.",
    "what diseases are caused by coronavirus": "A coronavirus that originated in China led to the Severe Acute Respiratory Syndrome (SARS) outbreak in 2003. Another coronavirus emerged in 2012 in Saudi Arabia, causing Middle East Respiratory Syndrome (MERS)",
    "why does coronavirus cause shortness of breath?": "COVID-19 can cause damage to the lungs that impedes their ability to remove oxygen from the air. A lot of patients develop what’s known as severe acute respiratory distress syndrome. And they really benefit from having additional oxygen, particularly in hospital settings.",
    "why and how should i seek medical attention?": "If you develop any of the following emergency warning signs for COVID-19, get medical attention immediately by calling your doctor's office. Emergency warning signs include (but are not limited to): Troubled breathing, Presistent pain in the chest, Confusion, Bluish lips or face.",
    "how does the virus spread?": "The virus that causes COVID-19 is thought to spread mainly from person to person, mainly through respiratory droplets produced when an infected person coughs, sneezes, or talks. These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs. Spread is more likely when people are in close contact with one another (within about 6 feet).",
    "who are you?": "I am the coronavirus chatbot, I can answer your questions related to coronavirus.\nI can also check you to see if you have covid, just say *start assessment*.",
    "ok": "Do you need anything else?",
    "i want to ask you a question": "Sure, go ahead. I'll answer the best I can.",
    "is fever a symptom of covid?": "Yes, having a fever can be a symptom of coronavirus.\nIf you say *start assessment*, I can help you figure out if you have corona or not.",
    "thank you": "I'm happy to help.",
    "thanks": "Happy I could help.",
    "thx": "I'm glad I could help you.",
}


def get_answer(msg):
    msg = msg.lower()
    no = [
        "nah",
        "nay",
        "negative",
        "not",
        "nope",
        "nix",
        "refusal",
        "denial",
        "decline",
        "rejection",
        "dissent",
        "prohibition",
        "forbidden",
        "disallow",
        "disapprove",
        "oppose",
        "reject",
        "disagree",
        "turn down",
        "no",
        "don't",
        "havn't",
        "never",
    ]
    yes = [
        "yeah",
        "yup",
        "affirmative",
        "absolutely",
        "indeed",
        "certainly",
        "definitely",
        "sure",
        "of course",
        "ofcourse",
        "agreed",
        "positive",
        "aye",
        "ok",
        "okay",
        "roger",
        "right",
        "correct",
        "you bet",
        "absolutely",
        "naturally",
        "yes",
        "ya",
        "mhm",
        "maybe",
        "perhaps",
        "probably",
        "possibily",
        "have",
    ]
    for word in yes:
        if word in msg:
            return "Yes"
    for word in no:
        if word in msg:
            return "No"

    return "unknown"

def get_question():
    global node
    if type(node) != str:
        for key, value in node.items():
            display_message(Questions[key], "received")
            node = node[key]
    else:
        entry.configure(state=tk.DISABLED)
        send_button.configure(state=tk.DISABLED)
        if node == "Yes":
            display_message(
                "I'm really sorry to inform that you've been affected by COVID-19.",
                "received",
            )
        else:
            display_message(
                "Congratulations, you are not affected by COVID-19.", "received"
            )


def logic(msg):
    global node
    if msg == "":
        return
    ans = get_answer(msg)

    if ans == "unknown":
        display_message("Sorry, I can't understand you.", "received")
        return

    node = node[ans]


assessment = False


def send_message(event=None):
    global assessment, QnA
    msg = entry.get()
    display_message("You: " + msg, "sent")
    if (
        msg == "start assessment"
        or msg == "do i have corona?"
        or msg == "do i have covid?"
    ):
        assessment = True
        get_question()
    elif assessment == True:
        logic(msg)
        get_question()
    else:
        if msg in QnA:
            display_message(QnA[msg], "received")
        else:
            display_message("Sorry, I don't understand you.", "received")


def display_message(message, message_type):
    chat_window.configure(state=tk.NORMAL)
    chat_window.tag_config("sent", foreground="#0000FF", justify="right")
    chat_window.tag_config("received", foreground="#0000FF", justify="left")

    if chat_window.get("1.0", tk.END).strip():
        chat_window.insert(tk.END, "\n\n")

    if message_type == "sent":
        chat_window.insert(tk.END, message, message_type)
    elif message_type == "received":
        chat_window.insert(tk.END, message, message_type)

    chat_window.see(tk.END)
    chat_window.configure(state=tk.DISABLED)
    entry.delete(0, tk.END)


# Create main window
window = tk.Tk()
window.title("COVID-19 Chatbot")
window.geometry("500x500")

# Configure ttk style
style = ttk.Style()
style.configure("TFrame", background="#000047")
style.configure(
    "TButton", background="darkblue", foreground="darkblue", font=("Arial", 18, "bold")
)
style.configure("TLabel", background="darkblue", font=("Arial", 18))
style.configure("TEntry", font=("Arial", 18))

# Create chat window
chat_frame = ttk.Frame(window, padding=0, style="TFrame")
chat_frame.pack(fill=tk.BOTH, expand=True)

chat_window = tk.Text(
    chat_frame, state=tk.DISABLED, background="black", font=("Arial", 18)
)
chat_window.pack(fill=tk.BOTH, expand=True)

# Create user input entry
entry_frame = ttk.Frame(window, padding=5, style="TFrame")
entry_frame.pack(fill=tk.X)

entry = ttk.Entry(entry_frame, font=("Arial",30))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.bind("<Return>", send_message)

# Create send button
send_button = ttk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

display_message("hello, how can i help you?", "recived")
# get_question()
# Start GUI main loop
window.mainloop()
