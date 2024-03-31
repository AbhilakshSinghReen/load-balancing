from random import random


class Server:
    def __init__(self, id, fail_probability=0) -> None:
        self.id = id
        self.fail_probability = fail_probability
        self.processed_requests = 0
        self.failed_requests = 0
        self.total_requests = 0

    def heartbeat(self):
        return self.fail_probability < random()

    def make_request(self, request: str):
        self.total_requests += 1

        if self.fail_probability > random():
            self.failed_requests += 1
            raise Exception(f"Server with id {self.id} could not process the request: {request}.")
        
        self.processed_requests += 1
        return True
    
    def get_total_requests(self):
        return self.total_requests
    
    def get_processed_requests(self):
        return self.processed_requests
