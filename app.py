import os
from flask import Flask
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import json
from database import db, Todo
from flask import render_template

kernel = sk.Kernel()

#uncomment this in order to get it to work with OpenAI
#api_key="<get the key from https://platform.openai.com/api-keys>"
#org_id="<get the ord-id from https://platform.openai.com/account/organization>"

kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'todos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
app.debug = True

with app.app_context():
    db.create_all()


@app.route("/")

async def semantic_hello():
    
    todos = Todo.query.all()
    todo = None  # Initialize todo with None
    if todos:
        todo = todos[0]
    print(f"Todo: {todo}")
    if todo:
        try:
            todo.recommendations = json.loads(todo.recommendations)
        except Exception as e:
            print(f"Error loading recommendations: {e}")
        return render_template('app.html', recommendations=todo.recommendations)
    
    input_string = "Sign up kids for soccer" #modify this to get different recommendations
    
    prompt = f"Create array of 5 items with correct formated JSON syntax without newlines having title and link string properties with links that would be recommendations based on the input string: '{ input_string }'"
    response = kernel.create_semantic_function(prompt)

    data = await response.invoke()
    
    if data.error_occurred == True:
        print(data.last_error_description)
        return

    try:
        recommendations = data.result
    except Exception as e:
        print(f"Error dumping recommendations: {e}")
        return

    todo = Todo(recommendations=recommendations)

    try:
        db.session.add(todo)
        db.session.commit()
    except Exception as e:
        print(f"Error adding and committing todo: {e}")
        return
    
    try:
        recommendations = json.loads(todo.recommendations)
    except Exception as e:
        print(f"Error loading recommendations: {e}")
        return

    return render_template('app.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
