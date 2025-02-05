from flask import Flask,json,jsonify,request
import os


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route("/makedir",methods=["POST"])
def makedir():
    data = request.get_json()
    name = data["name"]
    
    if name not in os.listdir(os.getcwd()+"/nodes"):
        print("Creating directory")
        os.mkdir(os.getcwd()+"//nodes//"+name)
        file = open("nodes/"+name+"/data.json","w")
        file.write("{}")
        file.close()
            
    return jsonify({"status":"success"})

@app.route("/updateLog",methods=['POST'])
def updateLog():
    data = request.get_json()
    stream = data['stream']
    time = data['time']
    name = data['name']
    app = data["window"]

    with open("nodes/"+name+"/data.json","r") as file:
        content = json.load(file)
            
    with open("nodes/"+name+"/data.json","w") as file:
        content[app+" at "+time]=stream
        # print(content)
        json.dump(content,file)
    
    return jsonify({"status":"success"})

if __name__ == '__main__':
    app.run(host="0.0.0.0")