```markdown
# 💬 Simple Chat Bot (Flask)

A simple web-based **Chat Bot** built with Flask. This app allows users to interact with a basic rule-based chatbot and stores conversation history in a JSON file.

---

## 📂 Project Structure
```
chat_bot/
│
├── chat_app.py              # Main Flask application
├── data/
│   └── chat_history.json    # Stores chat history
├── static/
│   └── style.css            # Styling for the app
├── templates/
│   └── chat_index.html      # Chat interface
```

---

## 🚀 Features
- Rule-based chatbot with simple responses:
  - "hello" → "Hi there!"
  - "how are you" → "I'm just code, but I'm doing great!"
  - "bye" → "Goodbye!"
- Stores chat history in JSON file
- Option to clear chat and start fresh
- Clean UI with styled chat window

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/shravyaksks/chat_bot.git
   cd chat_bot
   ```

2. **Create a virtual environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the application**
   ```bash
   python chat_app.py
   ```

5. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

---

## 📸 Screenshots
- **Chat Page**: Type messages and see bot responses.
- **History**: View past conversation stored in JSON.

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS (Jinja2 templates)
- **Data Storage**: JSON file

---

## 🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss.

---

## 📜 License
This project is licensed under the MIT License.
```

---

### 🔹 Step 4: Commit and push README
```bash
git add README.md
git commit -m "Add README.md with project details"
git push
```
