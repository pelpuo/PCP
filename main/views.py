from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=["GET","POST"])
def index():
    """Video streaming home page."""
    if request.method == "POST":
        camera = request.form.get("camera-select")
        print("Camera is {}".format(camera))
        if camera:
            return render_template("home.html", data={'video':camera, 'live':True})
    return render_template('home.html', data={})