from server import Server


class LoadBalancer:
    "Simple Round-Robin Load Balancer"

    def __init__(self, servers: list[Server]) -> None:
        self.all_servers = servers
        self.lru_servers = self.all_servers

    def make_request(self, request):
        target_server = self.lru_servers.pop(0) # Least Recently Used server is our target

        target_server.make_request(request) # Make the request

        self.lru_servers.append(target_server) # The requested server is not the most recently used
