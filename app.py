from flask import Flask
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import json
from flask import render_template

kernel = sk.Kernel()

api_key = "sk-"
org_id = "org-"
#api_key="<get the key from https://platform.openai.com/api-keys>"
#org_id="<get the ord-id from https://platform.openai.com/account/organization>"

kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

app = Flask(__name__)

@app.route("/")
async def semantic_hello():
    prompt = f"Create array of 5 items with correct formated JSON syntax without newlines having title and link string properties with links that would be recommendations based on the input string: 'Sign up kids for soccer'"
    response = kernel.create_semantic_function(prompt)

    data = await response.invoke()
    
    if data.error_occurred == True:
        print(data.last_error_description)

    recommendations = json.loads(data.result)

    dumpsrecommend = json.dumps(recommendations)

    print(dumpsrecommend)

    recommendations = json.loads(dumpsrecommend)


    return render_template('app.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
