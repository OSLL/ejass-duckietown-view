import cv2


class Camera:
    def __init__(self, rstp):
        self.rtsp = rstp
        self.camera = cv2.VideoCapture(self.rtsp)

    def gen_frames(self):
        while True:
            # Capture frame-by-frame
            success, frame = self.camera.read()  # read the camera frame
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
