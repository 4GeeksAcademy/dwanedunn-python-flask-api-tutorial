from flask import Flask, jsonify, request
app = Flask(__name__)
# Leave above lines in tact


# The request body is already JSON decoded, and it comes in the request.json variable
# print(request.json)

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

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json()
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)