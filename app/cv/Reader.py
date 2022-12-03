from threading import Thread

class VideoReader(Thread):
    def __init__(self, cap, queue, sentinel):
        super().__init__()
        self.queue = queue
        self.cap = cap
        self.sentinel = sentinel
    def run(self):
        cap = self.cap
        ret, frame = cap.read()
        while ret:
            self.queue.put(frame)
            ret, frame = cap.read()
        self.queue.put(self.sentinel)
        self.cap.release()
