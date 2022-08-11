from urllib import request
from flask import Flask , render_template , request
app = Flask(__name__)
#conexion de MySQL

@app.route('/')
def index():
    return render_template('index0.html')

if __name__ == '__main__':
    app.run(debug=True,port=3306)