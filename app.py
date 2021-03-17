from flask import Flask
app = Flask(__name__)

@app.route('/test/<username>')
def hello_world(username: str):
    return 'Simple flask on Docker container!!!' + username

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')