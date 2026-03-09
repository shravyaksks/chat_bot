from flask import Flask, render_template, request, redirect, url_for
import os, json

app = Flask(__name__)

DATA_FILE = "data/chat_history.json"
os.makedirs("data", exist_ok=True)

def load_history():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(DATA_FILE, "w") as f:
        json.dump(history, f, indent=4)

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there!"
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I don't understand that yet."

@app.route("/", methods=["GET", "POST"])
def chat():
    history = load_history()
    response = None
    if request.method == "POST":
        user_message = request.form["message"]
        bot_message = chatbot_response(user_message)

        history.append({"user": user_message, "bot": bot_message})
        save_history(history)

        response = bot_message
    return render_template("chat_index.html", history=history, response=response)

@app.route("/clear")
def clear():
    save_history([])
    return redirect(url_for("chat"))

if __name__ == "__main__":
    app.run(debug=True)
