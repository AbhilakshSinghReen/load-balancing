from random import randint
import unittest

from load_balancer import LoadBalancer
from server import Server


class LoadBalancerTestCase(unittest.TestCase):
    def load_balancer_test(self, num_requests: int, num_servers: int):
        test_servers = [Server(str(i), randint(1, 15)) for i in range(0, num_servers)]
        server_weights_sum = sum([server.weight for server in test_servers])

        load_balancer = LoadBalancer(test_servers)

        for i in range(num_requests):
            load_balancer.make_request(f"request_{i}")

        for server in test_servers:
            server_weight_ratio = server.weight / server_weights_sum
            server_request_ratio = server.total_requests / num_requests

            self.assertAlmostEqual(server_request_ratio, server_weight_ratio, 2)

    def test_load_balancing(self):
        test_inputs = [
            [1000000, 10],
            # [95, 10],
            # [95, 9],
            # [95, 7],
            # [100, 13],
            # [1, 1],
            # [0, 5],
            # [10, 10],
        ]

        for test_input in test_inputs:
            self.load_balancer_test(test_input[0], test_input[1])


if __name__ == '__main__':
    unittest.main()
