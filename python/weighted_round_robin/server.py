class Server:
    def __init__(self, id, weight) -> None:
        self.id = id
        self.weight = weight
        self.total_requests = 0

    def make_request(self, request: str):
        self.total_requests += 1
        return True
