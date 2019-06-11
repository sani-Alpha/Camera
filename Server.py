from flask import Flask, render_template, Response, jsonify, request
from Capture import Camera

app = Flask(__name__)

cap_camera = None
cap_frame = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture_status', methods=['POST'])
def capture_status():
    global cap_camera
    if cap_camera == None:
        cap_camera = Camera()

    json = request.get_json()

    status = json['status']

    if status == "true":
        cap_camera.camera()
        return jsonify(result="started")
    else:
        cap_camera.stop()
        return jsonify(result="stopped")

def camera_stream():
    global cap_camera
    global cap_frame

    if cap_camera == None:
        cap_camera = Camera()

    while True:
        frame = cap_camera.filters()

        if frame != None:
            cap_frame = frame
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + cap_frame + b'\r\n\r\n')

@app.route('/image_viewer')
def image_viewer():
    return Response(camera_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
