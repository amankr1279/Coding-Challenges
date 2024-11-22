from flask import Flask, jsonify

app = Flask("server1")

@app.route("/ping", methods = ['GET'])
def ping():
    return jsonify(
        {
            "msg" : "Alive and healthy!"
        }
    )
    
@app.route("/", methods = ['GET'])
def home():
    return jsonify(
        {
            "msg" : "From backend Server 1"
        }
    )
    
app.run(debug=True, port = 8081)