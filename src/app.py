from flask import Flask, jsonify
app = Flask(__name__)
# Leave above lines in tact

#Global Variables
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/todos', methods=['GET'])
def hello_todo():
    # json_data = jsonify(todos)
    return jsonify(todos)


# @app.route('/todos', methods=['GET'])
# def hello():
#     return "<h1>Hello!</h1>"

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)