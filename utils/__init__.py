class Rides:

    def __init__(self, line):
        tmpLine = line.split(" ")
        print(tmpLine)
        self.__conf = dict({"startIntRow": tmpLine[0],
                            "startIntCol": tmpLine[1],
                            "endIntRow": tmpLine[2],
                            "endIntCol": tmpLine[3],
                            "earliest": tmpLine[4],
                            "latest": tmpLine[5]})

    def get_information(self):
        return self.__conf


class parssFile:

    def __init__(self, filename):
        self.__summary = set()
        self.__rides = []
        with open(filename) as f:
            read_data = f.read()
            for i, line in enumerate(read_data.split("\n")):
                if i == 0:
                    summary = line.split(" ")
                    print(summary)
                    self.__summary = dict({"row": int(summary[0]),
                                           "col": int(summary[1]),
                                           "car": int(summary[2]),
                                           "rides": int(summary[3]),
                                           "steps": int(summary[5])})

                else:
                    if line != "":
                        self.__rides.append(Rides(line))

    def get_summary(self):
        return self.__summary

    def get_rides(self):
        return self.__rides
