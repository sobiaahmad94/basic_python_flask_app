from app import app
# from the app.py file, import the variable app

@app.route('/')
def index():
    return "Troy and Abed in the morning! (Community TV show reference :P)"

# I need to use the flask run command in the terminal everytime I update the app, to view it on localhost:4999


