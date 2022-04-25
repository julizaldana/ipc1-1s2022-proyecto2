from flask import Flask
from flask_cors import CORS
from libro.routes.libro_Route import libro
#from prestamista.routes.prestamista_Route import prestamista


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return {"msg" : "This api works!"}

app.register_blueprint(libro)
##app.register_blueprint(prestamista)
##app.register_blueprint()

if __name__ == '__main__':
    app.run(debug = True)