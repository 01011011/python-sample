# Python Flask Application

This is a Python Flask application that uses the Semantic Kernel and OpenAI to generate recommendations based on a given input string.

## Prerequisites

- Python 3.6 or higher: You can download it from the official Python website [here](https://www.python.org/downloads/). After installation, you can verify the installation by running `python --version` in your terminal.

- Flask: After installing Python, you can install Flask using pip, which is a package manager for Python. Run the following command in your terminal: `pip install flask`

- Semantic Kernel: 
    `python -m pip install --upgrade semantic-kernel`
- OpenAI account: You can create an account on the OpenAI platform [here](https://platform.openai.com/signup). After creating an account, you will be able to generate API keys for using OpenAI services.

## Setup

1. Clone the repository to your local machine.

2. Install the required Python packages. You can do this by running `pip install -r requirements.txt` in the root directory of the project.

3. You need to have an OpenAI account. Get the API key and organization ID from your OpenAI account at https://platform.openai.com/api-keys and https://platform.openai.com/account/organization respectively.

4. Uncomment the lines in `app.py` where the `api_key` and `org_id` variables are defined and replace `<get the key from https://platform.openai.com/api-keys>` and `<get the ord-id from https://platform.openai.com/account/organization>` with your actual API key and organization ID.

## Running the Application

1. Navigate to the root directory of the project in your terminal.

2. Run the command `python app.py` to start the application.

3. Open your web browser and navigate to `http://localhost:5000` to see the application in action.

## How it Works

The application uses the Semantic Kernel and OpenAI to generate recommendations based on a given input string. The input string is "Sign up kids for soccer", and the application generates an array of 5 items with title and link properties that would be recommendations based on this input string.

The recommendations are stored in a SQLite database and displayed on the web page.

## Troubleshooting

If you encounter any errors, check the console output for error messages. These messages should give you an idea of what went wrong and how to fix it.