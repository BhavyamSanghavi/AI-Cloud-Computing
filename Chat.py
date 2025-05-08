import gradio as gr
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

user_prompts = {
    "greeting": ["hello", "hi", "hey", "good morning"],
    "menu": ["what's on the menu", "show me the drinks", "what do you serve"],
    "order": ["i want to order", "can i get a coffee", "i'd like to have a tea", "get me a cake", "i want cake"],
    "hours": ["when do you open", "what are your hours", "closing time"],
    "goodbye": ["bye", "goodbye", "see you later"],
    "thanks": ["thank you", "thanks a lot", "thanks"],
    "reservation": ["book a table", "i need a reservation", "reserve for two"],
    "location": ["where are you located", "what's your address", "location of the cafe"],
    "wifi": ["do you have wifi", "internet available", "wifi password"],
    "delivery": ["do you deliver", "home delivery", "can i order from home"],
    "negative": ["i don't want cake", "no coffee", "not interested in tea", "i do not want anything sweet"],
}

chat_responses = {
    "greeting": "Welcome to Brew Café! What can I get for you today?",
    "menu": "Here's our menu:\n☕ Coffee\n🍵 Tea\n🥐 Croissant\n🍰 Cake",
    "order": "Sure! What would you like to order?",
    "hours": "We're open from 8 AM to 8 PM every day!",
    "goodbye": "Thanks for visiting Brew Café. Have a great day!",
    "thanks": "You're welcome! 😊",
    "reservation": "Sure! We can reserve a table for you. For how many people?",
    "location": "We're located at 123 Coffee Street, Brewtown ☕📍",
    "wifi": "Yes! Free Wi-Fi is available. The password is brewcoffee123.",
    "delivery": "Yes, we offer home delivery within 5 km. 🍽",
    "negative": "No problem! How about trying something else from our menu? ☕🍰🍵",
}

menu_items = {
    "cake": "🍰 We have:\n- Chocolate Cake 🍫: ₹150\n- Red Velvet ❤: ₹180\n- Cheesecake 🍰: ₹200\n(Available in egg & eggless options)",
    "coffee": "☕ Coffee options:\n- Espresso: ₹100\n- Cappuccino: ₹120\n- Latte: ₹130",
    "tea": "🍵 Tea options:\n- Green Tea: ₹80\n- Masala Chai: ₹70\n- Lemon Tea: ₹75",
    "croissant": "🥐 Croissants:\n- Butter: ₹90\n- Almond: ₹110\n- Chocolate: ₹120",
}

all_inputs = []
all_intents = []
for intent, inputs in user_prompts.items():
    all_inputs.extend(inputs)
    all_intents.extend([intent] * len(inputs))

vectorizer = TfidfVectorizer()
vectorized_given_inputs = vectorizer.fit_transform(all_inputs)

def respond(message, chat_history):
    if message.lower() == "exit":
        chat_history.append((message, "Thank you for visiting our cafe!"))
        return "", chat_history
    else:
        user_input_vectorized = vectorizer.transform([message])
        similarity = cosine_similarity(user_input_vectorized, vectorized_given_inputs)

        best_match_index = np.argmax(similarity)
        best_match_intent = all_intents[best_match_index]
        best_score = similarity[0][best_match_index]

        response = chat_responses.get(best_match_intent, "I'm sorry, I don't understand that. Could you rephrase?")

        if best_match_intent == "order":
            for item_key, item_response in menu_items.items():
                if item_key in message.lower() and "don't" not in message.lower() and "do not" not in message.lower():
                    response += f"\n\n{item_response}"
                    break
            else:
                response = chat_responses["order"] # If a specific item isn't mentioned after "order"

        elif best_match_intent in menu_items and best_match_intent != "order": # For direct menu queries
            response = menu_items[best_match_intent]

        chat_history.append((message, response))
        return "", chat_history

with gr.Blocks(title="☕ Brew Café Chatbot") as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
