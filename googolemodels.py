import google.generativeai as genai

API_KEY = "AIzaSyBOAMZmv0wGpXe26AqZdo9XTfKjYcQxJdY"

genai.configure(api_key=API_KEY)

# List available models
models = genai.list_models()

for model in models:
    print(model.name)
