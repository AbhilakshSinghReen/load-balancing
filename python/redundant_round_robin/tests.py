import unittest

from load_balancer import LoadBalancer
from server import Server


class LoadBalancerTestCase(unittest.TestCase):
    def load_balancer_test(self, num_requests: int, num_servers: int):
        test_servers = [Server(str(i), 0.2) for i in range(0, num_servers)]

        load_balancer = LoadBalancer(test_servers)

        for i in range(num_requests):
            load_balancer.make_request(f"request_{i}")

        server_processed_requests = [server.get_processed_requests() for server in test_servers]
        server_total_requests = [server.get_total_requests() for server in test_servers]

        print(sum(server_processed_requests))
        print(len(load_balancer.failed_requests))
        print(num_requests)
        print(sum(server_total_requests))

        # Processed requests Sum should be equal to num_requests
        self.assertEqual(sum(server_processed_requests) + len(load_balancer.failed_requests), num_requests)

        

        # Total requests sum should be equal to num_requests + num_exceptions
        # self.assertEqual(sum(server_total_requests), num_requests + load_balancer.num_exceptions)
    
    def test_load_balancing(self):
        test_inputs = [
            [100, 10],
            [95, 10],
            [95, 9],
            [95, 7],
            [100, 13],
            [1, 1],
            [0, 5],
            [10, 10],
        ]

        for test_input in test_inputs:
            self.load_balancer_test(test_input[0], test_input[1])


if __name__ == '__main__':
    unittest.main()
