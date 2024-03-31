from random import random


class Server:
    def __init__(self, id) -> None:
        self.id = id
        self.total_requests = 0

    def make_request(self, request: str):
        self.total_requests += 1
        return True
    
    def get_total_requests(self):
        return self.total_requests
