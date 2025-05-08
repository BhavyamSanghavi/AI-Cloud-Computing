import gradio as gr
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download once if not already
# nltk.download('punkt')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Define intents and responses
intents = {
    "menu": ["menu", "items", "coffee", "tea", "drinks", "available"],
    "order": ["order", "want", "have", "get", "buy"],
    "hours": ["time", "open", "close", "hours", "timing"],
    "location": ["where", "location", "address", "place"],
    "greeting": ["hello", "hi", "hey"],
    "bye": ["bye", "goodbye", "see you"]
}

responses = {
    "menu": "Our menu includes espresso, cappuccino, latte, herbal teas, and fresh pastries.",
    "order": "Sure! Please tell me what you'd like to order.",
    "hours": "We're open from 8 AM to 8 PM, Monday to Saturday.",
    "location": "We're located at 123 Brew Street, Coffeetown.",
    "greeting": "Hello! Welcome to Café Bliss ☕. How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "default": "Sorry, I didn't get that. Could you please rephrase?"
}

# Preprocessing
def preprocess(text):
    tokens = word_tokenize(text.lower())
    lemma=[]
    for token in tokens:
        lemma.append(lemmatizer.lemmatize(token))
    return lemma

# Intent matching
def get_intent(user_input):
    lemmas = preprocess(user_input)
    for intent, keywords in intents.items():
        if any(word in lemmas for word in keywords):
            return intent
    return "default"

# Respond function
def respond(message, chat_history):
    intent = get_intent(message)
    bot_response = responses[intent]
    chat_history.append((message, bot_response))
    return "", chat_history

# Gradio Blocks UI
with gr.Blocks(title="☕ Brew Café Chatbot") as demo:
    gr.Markdown("## Welcome to ☕ Brew Café Chatbot\nAsk us about our menu, hours, location, or place an order!")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type your message and press Enter")
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
