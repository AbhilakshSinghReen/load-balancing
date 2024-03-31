from time import sleep

from server import Server


class LoadBalancer:
    "Round-Robin Load Balancer with Redundancy"

    def __init__(self, servers: list[Server], max_num_retries=10) -> None:
        self.all_servers = servers
        self.available_lru_servers = self.all_servers
        self.unavailable_servers = []
        self.num_exceptions = 0
        self.num_requests = 0
        self.max_num_retries = max_num_retries
        self.failed_requests = []
        
    def update_server_availability(self):
        for server in self.unavailable_servers:
            if server.heartbeat():
                self.available_lru_servers.append(server)

    def wait_for_server_availability(self):
        while len(self.available_lru_servers) == 0:
            self.update_server_availability()

            # sleep(1)

    def make_request(self, request, retry_num=0):
        if retry_num > self.max_num_retries:
            self.failed_requests.append(request)
            return
        
        if len(self.available_lru_servers) == 0:
            # All servers are down - request is blocked until at least one server is back online
            self.wait_for_server_availability()
        
        target_server = self.available_lru_servers.pop(0)

        try:
            target_server.make_request(request)
            self.available_lru_servers.append(target_server)
        except:
            self.num_exceptions += 1
            self.unavailable_servers.append(target_server)
            self.make_request(request, retry_num + 1)
