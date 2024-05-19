from address import Address

class Mailing:
    def __init__(self, from_address: Address, to_address:Address, cost: int, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
