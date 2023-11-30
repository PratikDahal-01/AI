#!pip install nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name 7",
        ["My name is RSCOE and I'm a chatbot?",]
    ],
    [
        r"how are you ’2",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want 7",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ‘2",
        ["Nagesh created me using Python's NLTK library", "top secret ;)",]
    ],
    [
        r"(.*) (locationlcity) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ]
]

def BOT():
    print("Hi, I'm ChattyBOT and I chat a lot ;)\nPlease type lowercase English language to start a conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    BOT()
