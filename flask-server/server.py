from flask import Flask, render_template, Response
import cv2

# Initialize the Flask app
app = Flask(__name__)

# *** Video Setup ***

# Sets up the video capture. Allowing access to your camera.  
video = cv2.VideoCapture(0)

# Function loops over frames from the video and returns the frames as 
# response chunkswith content type image/jpeg. 
def gen_frames():
        while True:
                success, frame = video.read() # read camera frame
                if not success:
                        break
                else:
                        ret, buffer = cv2.imencode('.jpg', frame) 
                        frame = buffer.tobytes()
                        #concat frame one by one and show the result
                        yield (b'--frame\r\n'
                                b'Content-Type: image/jpeg\r\n\r\n')


# *** Route setup ***
# Default app route
@app.route('/')
# run index func on default route
def index():
        return render_template('../client/index.js')

# Video feed route
@app.route('/video_feed')
# run video feed func at video_feed
# 
def video_feed():
        return Response(gen_frames(), mimetype='multipart/x-mixed-replaced; boundary=frame')


# Members API Route
@app.route("/members")
# Create
def members():
        # Returning a json of members array
        return {"members": ["Members1", "Members2","Members3","Members4"]}

# Condition to run app
if __name__ == "__main__":
        # debug=true for development
        app.run(debug=True)