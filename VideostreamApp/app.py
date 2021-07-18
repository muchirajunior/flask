from flask import Flask,render_template,Response
import cv2
 
app=Flask(__name__)

camera=cv2.Videocapture(0)

def generateframe():
    while True:
        success,frame=camera.read()

        if not success:
            break
        else:
            value,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

    yield(b'--frame\r\n'+b'content-type:image/jpeg\r\n\r\n'+frame+b'\r\n')


@app.route('/')
def index():

    return render_template("index.html")

@app.route('/video')
def video():

    return Response(generateframe(),mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__=="__main__":
    app.run(debug=True)