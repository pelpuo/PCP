from flask import Blueprint, render_template, request, Response, jsonify
import cv2
from .camera_feed import gen_frames, list_ports

stream = Blueprint('stream', __name__)

@stream.route('/video_feed')
@stream.route('/video_feed/<video>')
def video_feed(video=0):
    if len(video.split('.')) != 1:
        video = 'main/static/videos/' + video
    else:
        video = int(video)
        return Response(gen_frames(int(video)), mimetype='multipart/x-mixed-replace; boundary=frame')


@stream.route('/ports', methods=["GET", "POST"])
def ports():
    if request.method == "GET":
        ports = list_ports()
        return jsonify({'cameras':ports})
    else:
        return jsonify({'error':"Invalid method"})

@stream.route('/roi', methods=["POST"])
def roi():
    roi_value = request.json["roi"]
    print("New ROI Value is: {}".format(roi_value))
    return jsonify({"success":True})
    

@stream.route('/', methods=["GET","POST"])
def index():
    """Video streaming home page."""
    if request.method == "POST":
        camera = request.form.get("camera-select")
        print("Camera is {}".format(camera))
        if camera:
            return render_template("home.html", data={'video':camera, 'live':True})
    return render_template('index.html', data={})