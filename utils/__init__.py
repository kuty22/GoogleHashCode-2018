class Rides:

    def __init__(self, line):
        tmpLine = line.split(" ")
        self.__conf = dict({"startIntRow": tmpLine[0],
                            "startIntCol": tmpLine[1],
                            "endIntRow": tmpLine[2],
                            "endIntCol": tmpLine[3],
                            "earliest": tmpLine[4],
                            "latest": tmpLine[5]})

    def get_information(self):
        return self.__conf


class Care:

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.status = 0
        self.ride = 0
        self.__rideList = []

    def move(self, position):
        self.__x = position["x"]
        self.__y = position["y"]

    def get_position(self):
        return dict({"x": self.__x, "y": self.__y})

    def addRide(self, ride):
        self.__rideList.append(ride)


class parssFile:

    def __init__(self, filename):
        self.__summary = set()
        self.__rides = []
        self.__cars = []
        with open(filename) as f:
            read_data = f.read()
            for i, line in enumerate(read_data.split("\n")):
                if i == 0:
                    summary = line.split(" ")
                    self.__summary = dict({"row": int(summary[0]),
                                           "col": int(summary[1]),
                                           "car": int(summary[2]),
                                           "rides": int(summary[3]),
                                           "steps": int(summary[5])})

                    for i in range(self.__summary["car"]):
                        self.__cars.append(Care())
                else:
                    if line != "":
                        self.__rides.append(Rides(line))

    def get_summary(self):
        return self.__summary

    def get_cars(self):
        return self.__cars

    def get_ride_information(self):
        listn = []
        for r in self.__rides:
            listn.append(r.get_information())
        return listn

    def get_rides(self):
        return self.__rides
