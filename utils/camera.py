from Camera import Camera

CAMERA_INSTANCE = []


def get_camera(rstp_client_url: str) -> Camera:
    global CAMERA_INSTANCE
    for camera in CAMERA_INSTANCE:
        if camera.rtsp == rstp_client_url:
            return camera
    camera = Camera(rstp_client_url)
    CAMERA_INSTANCE.append(camera)
    return camera
