import cv2
import time
import datetime


# Configuración
DETECTION_THRESHOLD = 1
SECONDS_TO_RECORD_AFTER_DETECTION = 5
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
VIDEO_FOURCC = cv2.VideoWriter_fourcc(*"mp4v")

# Clasificadores
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")


def get_video_capture():
    return cv2.VideoCapture(0)


def detect_faces_and_bodies(gray_frame):
    return face_cascade.detectMultiScale(gray_frame, 1.3, 5), body_cascade.detectMultiScale(gray_frame, 1.3, 5)


def start_recording(current_time):
    global out
    out = cv2.VideoWriter(f"{current_time}.mp4", VIDEO_FOURCC, 20, (FRAME_WIDTH, FRAME_HEIGHT))
    print("¡Grabación iniciada!")


def stop_recording():
    global out
    out.release()
    print("¡Grabación detenida!")


def write_frame_to_video(frame):
    if out is not None:
        out.write(frame)


def display_frame(frame):
    cv2.imshow("Cámara", frame)


def main():
    global out

    cap = get_video_capture()

    detection = False
    detection_stopped_time = None
    timer_started = False

    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces, bodies = detect_faces_and_bodies(gray)

        detections = len(faces) + len(bodies)

        if detections >= DETECTION_THRESHOLD:
            if not detection:
                detection = True
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                start_recording(current_time)
        elif detection:
            if timer_started:
                if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                    detection = False
                    timer_started = False
                    stop_recording()
            else:
                timer_started = True
                detection_stopped_time = time.time()

        write_frame_to_video(frame)
        display_frame(frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
