class RideSharingSystem:

    def __init__(self):
        self.rider_queue = deque()
        self.driver_queue = deque()
        self.valid_rider = {}
        
    def addRider(self, riderId: int) -> None:
        self.rider_queue.append(riderId)
        self.valid_rider[riderId] = True

    def addDriver(self, driverId: int) -> None:
        self.driver_queue.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if len(self.rider_queue) == 0 or len(self.driver_queue) == 0:
            return [-1, -1]

        res = [self.driver_queue.popleft(), self.rider_queue.popleft()]

        while self.rider_queue and self.valid_rider[self.rider_queue[0]] == False:
            self.rider_queue.popleft()

        return res

    def cancelRider(self, riderId: int) -> None:
        self.valid_rider[riderId] = False

        while self.rider_queue and self.valid_rider[self.rider_queue[0]] == False:
            self.rider_queue.popleft()

        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)