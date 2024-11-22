from flask import Flask, jsonify

app = Flask("server2")

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
            "msg" : "From backend Server 2"
        }
    )
    
app.run(debug=True, port = 8082)