from flask import Flask, render_template, request

import google.generativeai as genai

app = Flask(__name__)

# Configure the AI API key
api = "insert key"

if api is None:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=api)

@app.route('/', methods=['GET', 'POST'])
def index():
    winner = None
    user_input = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Call the AI model to get the winner
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Please, give a one word answer or a two word one if needed, Who was the winner of the premier league in {user_input}")
        winner = response.text

    return render_template('form.html', user_input=user_input, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)
