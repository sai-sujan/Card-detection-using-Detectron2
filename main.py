from ObjectDetector import Detector
from flask import Flask, render_template, request, Response, jsonify
import os
from flask_cors import CORS, cross_origin
from com_ineuron_utils.utils import decodeImage

app = Flask(__name__)

detector = Detector(filename="file.jpg")

RENDER_FACTOR = 35

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "file.jpg"
        # modelPath = 'research/ssd_mobilenet_v1_coco_2017_11_17'
        self.objectDetection = Detector(self.filename)


def run_inference(img_path='file.jpg'):
    # run inference using detectron2
    result_img = detector.inference(img_path)

    # clean up
    try:
        os.remove(img_path)
    except:
        pass

    return result_img


@app.route("/")
def home():
    # return "Landing Page"
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():

        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.objectDetection.inference('file.jpg')


        return jsonify(result)


# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    port = 8000
    app.run(host='127.0.0.1', port=port)
