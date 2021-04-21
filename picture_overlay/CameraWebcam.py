import cv2 as cv


class CameraWebcam:

    def __init__(self):
        self.window_name = "window1"
        self.window_size = cv.WINDOW_AUTOSIZE

    def take_picture(self):
        cap = cv.VideoCapture(0)

        while (True):
            # Capture frame by frame
            ret, frame = cap.read()

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            cv.imshow(self.window_name, gray)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    camera_webcam = CameraWebcam()
    camera_webcam.take_picture()