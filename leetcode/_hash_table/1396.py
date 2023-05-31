class UndergroundSystem:

    def __init__(self):
        self.hash_map = {}
        self.total_time = {}
        self.total_people = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hash_map[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, time = self.hash_map.pop(id)
        self.total_time[(station, stationName)] = self.total_time.get((station, stationName), 0) + t - time
        self.total_people[(station, stationName)] = self.total_people.get((station, stationName), 0) + 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total_time[(startStation, endStation)] / self.total_people[(startStation, endStation)]

