class Signal:
    def __init__(self, name: str, start: object, end: object):
        print("Created Signal: ", name)
        self.start = start
        self.end = end
