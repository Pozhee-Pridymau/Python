import address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    @property
    def to_address(self):
        return self._to_address

    @to_address.setter
    def to_address(self, value):
        self._to_address = address.Address(value["index"], value["city"], value["street"], value["house"], value["apartment"])

    @property
    def from_address(self):
        return self._from_address

    @from_address.setter
    def from_address(self, value):
        self._from_address = address.Address(value["index"], value["city"], value["street"], value["house"], value["apartment"])

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = float(value)

    @property
    def track(self):
        return self._track

    @track.setter
    def track(self, value):
        self._track = str(value)

    def __repr__(self):
        return f"Mailing({self.to_address}, {self.from_address}, {self.cost}, {self.track})"