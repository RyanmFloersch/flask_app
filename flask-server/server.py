from flask import Flask, render_template, Response
from camera import VideoCamera


# Create the flask endpoint
app = Flask(__name__)


# Default app route
@app.route('/')

# run index func on default route to render server html
def index():
    return render_template('index.html')


# Get the frames from the camera. 
# Loops over each frame and returns the displayed frame and the content type
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
# Video feed route
@app.route('/video_feed')

#   
def video_feed():
        # Return a Response returning the gen() func to display the frames,
        # with an http header to push the frames of the video to the web browser
        return Response(gen(VideoCamera()),
                         mimetype='multipart/x-mixed-replace; boundary=frame')



# Condition to run app
if __name__ == '__main__':
        # debug=true for development
        app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)


