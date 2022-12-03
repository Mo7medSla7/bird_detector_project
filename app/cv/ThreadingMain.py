from Reader  import VideoReader
from detector import BirdDetector
import threading
from queue import Queue
import cv2


def readAndDetect(path):
    lock = threading.Semaphore(0)
    SENTINEL = object()  #SENTINEL OBJECT
    SHARED_Q = Queue()
    res = dict()
    birdsCascade = cv2.CascadeClassifier("birds1.xml")
    cap = cv2.VideoCapture(path)

    reader = VideoReader(cap=cap , sentinel=SENTINEL ,queue=SHARED_Q)
    detector = BirdDetector( lock=lock, sentinel=SENTINEL, queue=SHARED_Q , res=res ,birdsCascade = birdsCascade)
    reader.start()
    data = detector.start()
    lock.acquire()
    return res['MaxBirds']

print(readAndDetect('vid.mp4'))

