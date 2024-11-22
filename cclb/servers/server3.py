from flask import Flask, jsonify, Response

app = Flask("server3")

@app.route("/ping", methods = ['GET'])
def ping():
    return Response(
        "Server is not alive",
        status=400
    )
    
@app.route("/", methods = ['GET'])
def home():
    return jsonify(
        {
            "msg" : "From backend Server 3"
        }
    )
    
app.run(debug=True, port = 8083)