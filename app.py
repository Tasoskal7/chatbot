from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'response': 'Please type a valid message.'})
    
    # OpenAI interaction with predefined context
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Hello! How can I assist you today? If you have any questions or want to discuss NBA 2K25, feel free to ask!"
            },
            {
                "role": "user",
                "content": "you only know about the game nba2k25 nothing else"
            },
            {
                "role": "assistant",
                "content": "I can certainly focus on discussing NBA 2K25 and its features, gameplay mechanics, and any new content it might have introduced. Feel free to ask me anything specific about the game!"
            },
            {
                "role": "user",
                "content": "dont answer any question other than nba 2k25"
            },
            {
                "role": "assistant",
                "content": "Understood! Feel free to ask any questions you have about NBA 2K25, and I'll be happy to help!"
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    bot_reply = response.choices[0].message.content
    
    # Replace newlines and create basic HTML structure
    formatted_reply = bot_reply.replace("\n", "<br>").replace("###", "<span style='font-size:16px;'>").replace("**", "<span>").replace("</span></span>", "</span>")



    
    return jsonify({'response': formatted_reply})

if __name__ == '__main__':
    app.run(debug=True)
