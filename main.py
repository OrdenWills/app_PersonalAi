import markdown
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = os.environ.get("APP_PASSWORD")

def init_model():
    # Set the API key
    Googleapi_key = os.environ.get('GOOGLE_API_KEY')
    genai.configure(api_key=Googleapi_key)

        # initialize the model
    model = genai.GenerativeModel('gemini-pro')
    conversations = model.start_chat(history=[])
    return conversations

conversations_history = []

conversations = init_model()

# print(response.text)
def to_mark(text):
    return markdown.markdown(text)

@app.route("/home", methods=["POST","GET"])
def home():
    
    
    # Get the user's prompt from the request body
    if request.method == 'POST':
        user_input = request.form['user_input']
        chat = conversations.send_message(user_input)

        conversations_history.append({'role': 'user','text': user_input})
        conversations_history.append({'role': 'model','text': to_mark(chat.text)})
        print(to_mark(chat.text))

        # formated model reponse
        # model_reponse_markdown = markdown.markdown(conversations.text)
        
        # history = conversations_history.extend(
        #     [
        #         {'role':'user','text':user_input},
        #         {'role': 'model','text':model_reponse_markdown}
        #     ])
        
    return render_template('home.html',conversations=conversations_history)

# @app.route("/process_input", methods=["POST"])
# def conversation():
#     # Get the user's message from the request body
#     message = request.json["message"]

#     # Generate a response using the GPT model
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=f"You: {message}\nBot: ",
#         max_tokens=1024,
#         temperature=0.7,
#     )

#     # Return the response to the user
#     return jsonify({
#         "response": response["choices"][0]["text"]
#     })

if __name__ == "__main__":
    app.run()

