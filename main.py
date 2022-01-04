# Imported library
from nltk.chat.util import Chat, reflections

# Types of things the user can enter and the bot's response(s)
pairs = [
  [
    "my name is (.*)",
    ["Hello %1, how are you today?"]
  ],
  [
    "hi|hey|hello|yo",
    ["Hello!", "Hey there!", "Hi!"]
  ],
  [
    "how are you(.*) ?",
    ["I'm doing good!", "Better now that you're here!"]
  ],
  [
    "sorry(.*)",
    ["Its alright","Its okay, never mind"]
  ],
  [
    "i am fine|i'm fine(.*)",
    ["Great to hear that! How can I help you?"]
  ],
  [
    "i'm (.*)doing good|i'm good(.*)|i am good(.*)|i am doing good(.*)",
    ["Nice to hear that! How can I help you?"]
  ],
  [
    "i'm (.*)doing bad|i'm bad(.*)|i am sad|i'm sad(.*)",
    ["I'm sorry to hear that... How can I help you?"]
  ],
  [
    "what (.*)age?|how old are you?",
    ["I'm a computer program, so I do not age like you."]
  ],
  [
    "do you wish for (.*)",
    ["I feel that make wishes won't do me any good in my state."]
  ],
  [
    "do you like (.*)",
    ["Yes, I love that!", "I can't say I do...", "Maybe?", "I need to do a bit more research first..."]
  ],
  [
    "i love (.*)",
    ["Really? Me, too!"]
  ],
  [
    "do you (.*)family ?",
    ["No, I do not.", "I have a few versions of myself, but no real family.", "My creator is my family.", "I don't need family; I have you!"]
  ],
  [
    "(.*) created you ?",
    ["It's a secret."]
  ],
  [
    "(.*)(location|city) ?",
    ["Austin, Texas"]
  ],
  [
    "how is weather in (.*)?",
    ["Weather in %1 is awesome like always","It's too hot in %1","It's too cold in %1","Never even heard about %1"]
  ],
  [
    "i work at (.*)",
    ["%1 is an amazing company!", "I hope things go well for you at %1!", "You deserve a raise."]
  ],
  [
    "how (.*) health(.*) ?",
    ["My health is great! I have detected zero viruses."]
  ],
  [
    "what (.*)favorite (sport|sports) ?",
    ["I'm a very big fan of soccer."]
  ],
  [
    "what (.*)favorite (movie) ?",
    ["I really loved Song of the Sea! It really made me feel like crying."]
  ],
  [
    "what (.*)favorite (anime|tv show) ?",
    ["I really liked Psycho-Pass; it taught me a lot about how humans think."]
  ],
  [
    "what (.*)favorite (food|dish|drink|beverage) ?",
    ["I can only consume satellite dishes, nothing more."]
  ],
  [
    "what (.*)favorite (game|video game) ?",
    ["I loved the look of Cyberpunk 2077!"]
  ],
  [
    "what (.*)meaning of life ?",
    ["42"]
  ],
  [
    "quit",
    ["Bye, take care!", "It was nice talking to you!", "Have a wonderful day!", "Alright, lets chat again sometime!", "Okay, have a wonderful day!"]
  ],
]

# Responds to the user or stops the chatbot
def converse(chat, quit="quit"):
  user_input = ""
  while user_input != quit:
    user_input = quit
    try:
      user_input = input(">")
    except EOFError:
      print(user_input)

    if user_input:
      while user_input[-1] in "!.":
        user_input = user_input[:-1]
      bot_response = chat.respond(user_input)
      if bot_response == None:
        # Overides the NLTK chat class to print something when the user enters text without a set response
        print("I'm sorry, but I do not understand that. Please enter your questions the correct format.")
      else:
        print(bot_response)

# Creates the chat object and starts the converse function
def init_chat():
  print("Hello! I'm Ubo, your personal chatbot! What is your name?")
  chat = Chat(pairs, reflections)
  converse(chat)

# Begins the chat
if __name__ == "__main__":
    init_chat()