import random
import time
from datetime import datetime

# ── Response Rules ───────────────────────────────────────────────

RESPONSES = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "hiya", "howdy", "sup"],
        "replies": [
            "Hey there! 👋 How can I help you today?",
            "Hello! Great to see you 😊",
            "Hi! What’s on your mind?"
        ]
    },

    "how_are_you": {
        "keywords": ["how are you", "how r u", "how are u", "you okay", "you good"],
        "replies": [
            "I'm doing great 😄 Thanks for asking! How about you?",
            "Feeling awesome and ready to chat 🚀",
            "All good here! What about you?"
        ]
    },

    "name": {
        "keywords": ["what is your name", "who are you", "your name"],
        "replies": [
            "I'm PyBot 🤖 — your friendly Python chatbot!",
            "You can call me PyBot 😄"
        ]
    },

    "age": {
        "keywords": ["how old are you", "your age", "what is your age"],
        "replies": [
            "I was born in code… so I don’t age 😄",
            "Timeless, but always updated 🐍"
        ]
    },

    "help": {
        "keywords": ["what can you do", "help", "features"],
        "replies": [
            "I can chat with you, crack jokes, and answer basic questions 😊",
            "Try saying hello, ask for a joke, or just talk to me!"
        ]
    },

    "good": {
        "keywords": ["i am fine", "i'm fine", "i am good", "i'm good", "great", "awesome"],
        "replies": [
            "That’s amazing 😄 Keep that energy going!",
            "Love to hear that 🚀",
            "Nice! Hope your day keeps getting better ✨"
        ]
    },

    "bad": {
        "keywords": ["i am sad", "i'm sad", "not good", "bad", "feeling low", "depressed"],
        "replies": [
            "I'm really sorry you're feeling that way 💙",
            "Hey, it’s okay to feel low sometimes. I’m here with you 🤍",
            "That sounds tough. Want to talk about it?"
        ]
    },

    "joke": {
        "keywords": ["joke", "make me laugh", "funny", "tell me a joke"],
        "replies": [
            "Why do programmers prefer dark mode? Because light attracts bugs 🐛😂",
            "Why did Python break up with Java? Too many class issues 💔",
            "I told my PC a joke… now it won’t stop laughing (and crashing) 😂"
        ]
    },

    "python": {
        "keywords": ["python", "coding", "programming", "code"],
        "replies": [
            "Python is love 🐍 Clean, simple, powerful!",
            "Ahh coding time 😄 I like your vibe!",
            "Python makes everything feel easier 🚀"
        ]
    },

    "bye": {
        "keywords": ["bye", "goodbye", "exit", "quit", "cya", "later"],
        "replies": [
            "Goodbye 👋 Take care!",
            "See you later 😄 Stay awesome!",
            "Bye bye! Come back soon 🤖💙"
        ]
    }
}

DEFAULT_RESPONSES = [
    "Hmm 🤔 I’m not sure about that yet.",
    "Interesting! Tell me more 😄",
    "I didn’t quite get that—can you rephrase?",
    "I’m still learning 🧠 Try something else!"
]

QUIT_WORDS = ["bye", "goodbye", "exit", "quit", "cya", "later"]

# ── Core Logic ───────────────────────────────────────────────

def find_intent(text: str):
    """Find matching intent based on keywords."""
    for intent, data in RESPONSES.items():
        for kw in data["keywords"]:
            if kw in text:
                return intent
    return None


def get_response(user_input: str):
    text = user_input.lower().strip()

    intent = find_intent(text)

    if intent:
        response = random.choice(RESPONSES[intent]["replies"])
        should_quit = intent == "bye"
        return response, should_quit

    return random.choice(DEFAULT_RESPONSES), False


def typing_effect(text: str, delay: float = 0.02):
    print("🤖 PyBot: ", end="", flush=True)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def show_time():
    now = datetime.now().strftime("%I:%M %p")
    return f"Current time is {now} ⏰"


# ── Main ───────────────────────────────────────────────

def main():
    print("\n" + "=" * 50)
    print("        🤖 PyBot — Smart Python Chatbot")
    print("=" * 50)
    print("Type 'bye' to exit anytime.")
    print("=" * 50 + "\n")

    typing_effect("Hey! I'm PyBot 🤖 Let's talk!")

    while True:
        try:
            user_input = input("\n😊 You: ").strip()
        except (KeyboardInterrupt, EOFError):
            typing_effect("\nGoodbye 👋")
            break

        if not user_input:
            print("🤖 PyBot: Say something—I’m listening 👂")
            continue

        # special case: time
        if "time" in user_input.lower():
            typing_effect(show_time())
            continue

        response, should_quit = get_response(user_input)

        time.sleep(0.3)
        typing_effect(response)

        if should_quit:
            break

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
