from flask import Flask
app = Flask(__name__)
# Leave above lines in tack

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'


# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)