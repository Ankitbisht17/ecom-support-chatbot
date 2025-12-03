\# 🤖 AI E-Commerce Support Chatbot



An intelligent customer support chatbot for e-commerce websites, built using \*\*Machine Learning, NLP and Flask\*\*.  

The bot can answer customer queries about \*\*order tracking, refunds, shipping and payment methods\*\* using an intent-classification model and rule-based logic.



---



\## 🌟 Features



\- Intent classification using \*\*TF-IDF + Logistic Regression\*\*

\- Handles multiple intents:

&nbsp; - `greet`, `goodbye`

&nbsp; - `order\_status`

&nbsp; - `refund`

&nbsp; - `shipping`

&nbsp; - `payment`

&nbsp; - (extensible via `intents.csv`)

\- Fake order database (`orders\_db.py`) for demo order tracking

\- Beautiful \*\*chat UI\*\* with:

&nbsp; - Typing indicator

&nbsp; - Message bubbles

&nbsp; - Quick-reply chips

\- Flask backend API (`/chat`) for easy integration with any front-end

\- (Optional) SQLite models prepared in `database.py` for login/order history



---



\## 🛠 Tech Stack



\- \*\*Backend:\*\* Python, Flask

\- \*\*ML / NLP:\*\* scikit-learn, TF-IDF, Logistic Regression

\- \*\*Frontend:\*\* HTML, CSS, Vanilla JS

\- \*\*Data:\*\* Custom intent dataset (`intents.csv`)

\- \*\*Version Control:\*\* Git \& GitHub



---



\## 📂 Project Structure



```bash

ecom-support-chatbot/

├── app.py                 # Flask app (routes + API)

├── chatbot\_core.py        # Intent detection + response logic

├── train\_intent\_model.py  # Trains Logistic Regression intent model

├── intents.csv            # Training data for intents

├── orders\_db.py           # Demo order data + helper

├── database.py            # (Optional) SQLAlchemy models

├── templates/

│   └── index.html         # Chat UI page

└── .gitignore



💬 Example Queries

Hi



What is your refund policy?



Track my order ORD12345



How long does delivery take?



What payment methods do you accept?



Future Enhancements

Real database integration with user login and real orders



Add more intents and larger training dataset



Deploy to cloud (Render / Railway / Heroku-like platforms)



WhatsApp / Telegram / website widget integration



Use transformer-based models for better intent detection



This project is built for academic / learning purposes and can be extended into a full-scale industrial chatbot.





Author

Ankit Bisht

GitHub: @Ankitbisht17





