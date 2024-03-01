
class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


def file_log():
    with File("log.txt", "r") as file:
        for f in file:
            if "LINK12" in f:
                yield f


if __name__ == '__main__':
    for i in file_log():
        print(i)

