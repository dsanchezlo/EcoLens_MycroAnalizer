from flask import Flask, Response, request
import cv2
from cvzone.ClassificationModule import Classifier
import os
from flask_cors import CORS

os.environ['TF_ENABLE_ONEDNN_OPTS']='0'

app = Flask(__name__)
CORS(app)

def generate_frames(model:str):
    cap = cv2.VideoCapture(0)

    model_path = f"./model_server/models/{model}/model.h5"
    label_path = f"./model_server/models/{model}/label.txt"

    classifier_model = Classifier(model_path,label_path)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            predictions, index = classifier_model.getPrediction(frame)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return 'Model server for image classification'
    
@app.route('/model/<model>', methods=['GET'])
def video_feed(model):
    # ip = request.remote_addr
    # print(ip)
    return Response(generate_frames(model=model), mimetype='multipart/x-mixed-replace; boundary=frame')

class model():
    def __init__(self):
        if __name__ == '__main__':
            app.run(debug=True)
            print('Model is running')

model()