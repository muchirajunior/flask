from flask import  Flask,request
from werkzeug.utils import secure_filename
import os
from PIL import Image
import shortuuid
app=Flask(__name__)

@app.route("/")
def index():

    return {"state":"okey"}

@app.route("/file",methods=['POST'])
def fileupload():
    file=request.files['file']
    image=Image.open(file)
    image=image.resize((320,240))
    filename = secure_filename(file.filename)
    ext=filename.rsplit('.',1)[1]
    name=shortuuid.uuid()
    filename=name+'.'+ext

    image.save("files/"+filename)


    return {"state":"done"}

if __name__=="__main__":
    app.run(debug=True)