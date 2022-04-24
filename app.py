from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return {"msg" : "This api works!"}

##app.register_blueprint()
##app.register_blueprint()
##app.register_blueprint()

if __name__ == '__main__':
    app.run(debug = True)