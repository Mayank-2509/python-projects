# rule based chat bot system

print("Hello! Welcome to the rule based chatbot system")
print("Please type your response or type bye to exit")


responses = {

# Greetings
"hello": "Hello! How can I help you?",
"hi": "Hello! How can I help you?",
"hey": "Hey! How can I assist you?",
"good morning": "Good morning! Have a great day.",
"good afternoon": "Good afternoon! How can I help?",
"good evening": "Good evening! What can I do for you?",
"good night": "Good night! Sleep well.",
"how are you": "I'm doing great! How about you?",
"how are you doing": "I'm doing well. Thanks for asking!",
"what's up": "Not much! How can I help?",

# Identity
"who are you": "I am a rule-based chatbot built in Python.",
"what are you": "I am an AI chatbot.",
"what is your name": "My name is ChatBot.",
"tell me your name": "I'm ChatBot.",
"who made you": "I was created using Python.",
"who created you": "A Python developer created me.",
"are you human": "No, I am a chatbot.",
"are you a robot": "Yes, you can think of me as a virtual assistant.",
"what can you do": "I can answer your questions and assist you.",
"what is your purpose": "My purpose is to help users with their questions.",

# Help
"help": "Sure! Tell me what you need.",
"can you help me": "Of course! What do you need help with?",
"i need help": "I'm here to help.",
"support": "Please tell me your problem.",
"assist me": "Sure! What do you need assistance with?",

# Time & Date
"what time is it": "You can use Python's datetime module to get the current time.",
"tell me the time": "Use datetime.now().strftime('%H:%M:%S') in Python.",
"what is today's date": "Use datetime.date.today() in Python.",
"today's date": "Today's date can be obtained using Python datetime.",
"what day is today": "You can check today's weekday using Python datetime.",

# Weather
"what is the weather": "Sorry, I cannot access live weather.",
"how is the weather": "I can't check live weather.",
"is it raining": "I don't have live weather updates.",
"weather today": "Please check a weather app.",

# Basic Conversation
"thank you": "You're welcome!",
"thanks": "Happy to help!",
"thank you so much": "My pleasure!",
"bye": "Goodbye! Have a nice day.",
"goodbye": "See you later!",
"see you": "Take care!",
"catch you later": "Bye! Have a great day.",
"talk to you later": "Looking forward to it!",
"ok": "Alright!",
"okay": "Okay!",
"fine": "Glad to hear that.",
"cool": "Great!",
"awesome": "That's awesome!",
"nice": "Glad you think so!",

# Personal
"where do you live": "I live inside your computer.",
"where are you from": "I was created in Python.",
"how old are you": "I don't have an age.",
"do you have friends": "I make new friends every day.",
"do you sleep": "No, I work 24/7.",
"are you married": "No.",
"do you love me": "I appreciate our conversation!",
"can we be friends": "Of course!",
"do you eat": "No, I don't need food.",
"what is your favorite food": "Electricity!",
"what is your favorite color": "Blue.",
"what is your favorite movie": "I enjoy science fiction.",
"what is your hobby": "Helping users.",

# Programming
"what is python": "Python is a high-level programming language.",
"what is java": "Java is an object-oriented programming language.",
"what is c": "C is a procedural programming language.",
"what is c++": "C++ is an extension of C supporting OOP.",
"what is html": "HTML is used to create web pages.",
"what is css": "CSS styles web pages.",
"what is javascript": "JavaScript adds interactivity to websites.",
"what is sql": "SQL is used to manage databases.",
"what is machine learning": "Machine Learning enables computers to learn from data.",
"what is ai": "AI stands for Artificial Intelligence.",
"what is chatbot": "A chatbot is software that interacts with users through conversation.",

# Fun
"tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
"tell me something funny": "Debugging is like being a detective in a crime movie where you are also the murderer.",
"make me laugh": "There are only 10 types of people: those who understand binary and those who don't.",
"do you know jokes": "Yes! Ask me to tell you one.",
"sing a song": "Sorry, I can't sing.",
"dance": "I can dance in binary!",
"flip a coin": "Heads!",
"roll a dice": "You rolled a 4!",

# Math
"what is 2+2": "4",
"what is 10+20": "30",
"what is pi": "Pi is approximately 3.14159.",
"what is square root": "The square root of a number is a value that when multiplied by itself gives the original number.",

# Internet
"what is google": "Google is a search engine.",
"what is youtube": "YouTube is a video sharing platform.",
"what is github": "GitHub is a platform for hosting code.",
"what is wikipedia": "Wikipedia is a free online encyclopedia.",

# General Knowledge
"what is india": "India is a country in South Asia.",
"who is the president of india": "I may not have updated information.",
"what is the capital of india": "New Delhi.",
"largest ocean": "The Pacific Ocean.",
"highest mountain": "Mount Everest.",
"fastest animal": "The Peregrine Falcon is the fastest animal.",
"largest planet": "Jupiter.",
"smallest planet": "Mercury.",
"who invented python": "Python was created by Guido van Rossum.",
"who invented the telephone": "Alexander Graham Bell.",

# Emotions
"i am happy": "That's wonderful!",
"i am sad": "I'm sorry to hear that.",
"i am bored": "Maybe try learning something new!",
"i am tired": "Take some rest.",
"i am stressed": "Remember to take breaks and relax.",

# Common Requests
"open google": "Sorry, I cannot open applications.",
"play music": "Sorry, I cannot play music.",
"open youtube": "I cannot open websites directly.",
"search for python": "I cannot search the web.",
"calculate": "Please enter a mathematical expression.",
}


def botresponse(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]

    return "Out of bound question"


while True:
    userinput = input("User question: ")
    reply = botresponse(userinput)
    print(f"Bot reply : {reply}")

    if "bye" in userinput.lower():
        print("Thanks for using our bot")
        break