from flask import Flask
from parser import parseLines
app = Flask(__name__)

@app.route('/test/<username>')
def hello_world(username: str):
    text_file = open("simple.txt", "r")
    lines = text_file.readlines()
    print(parseLines(lines))
    return "tess"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')