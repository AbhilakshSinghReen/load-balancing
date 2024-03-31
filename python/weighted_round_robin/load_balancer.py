from random import uniform

from server import Server


class LoadBalancer:
    "Simple Round-Robin Load Balancer"

    def __init__(self, servers: list[Server]) -> None:
        self.all_servers = servers
        self.server_weights_sum = sum([server.weight for server in servers])
        self.probability_ranges = self.compute_probability_ranges(servers)
    
    def compute_probability_ranges(self, servers):
        probability_ranges = []
        
        last_range_end = 0
        for server in servers:
            probability_ranges.append({
                "serverId": server.id,
                "rangeStart": last_range_end,
                "rangeEnd": last_range_end + server.weight,
            })

            last_range_end += server.weight
        
        return probability_ranges

    def get_target_server(self):
        range_specifier = uniform(0, self.server_weights_sum)

        target_server_id = ""
        for prob_range in self.probability_ranges:
            if range_specifier >= prob_range["rangeStart"] and range_specifier < prob_range["rangeEnd"]:
                target_server_id = prob_range["serverId"]
                break
        if target_server_id == "":
            target_server_id = self.probability_ranges[-1]["serverId"]

        for server in self.all_servers:
            if server.id == target_server_id:
                return server
        
        return False
    
    def make_request(self, request):
        target_server = self.get_target_server()

        target_server.make_request(request)
