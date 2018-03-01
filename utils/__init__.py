class parssFile:

    def __init__(self, filename):
        with open(filename) as f:
            read_data = f.read()
            lines = read_data.split("\n")
            summary = lines[0].split(" ")
            print(summary)
            self.__summary = dict({"row": int(summary[0]),
                                   "col": int(summary[1]),
                                   "car": int(summary[2]),
                                   "rides": int(summary[3]),
                                   "steps": int(summary[5])})

            print(self.__summary)

    def get_summary(self):
        return self.__summary
