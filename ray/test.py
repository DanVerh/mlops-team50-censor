from collections import Counter
import socket
import time

import ray

@ray.remote
class Actor:
    def __init__(self):
        pass

    def get_cluster_resources(self):
        return '''This cluster consists of
            {} nodes in total
            {} CPU resources in total
        '''.format(len(ray.nodes()), ray.cluster_resources())

    def task_def(self):
        time.sleep(0.001)
        # Return IP address.
        return socket.gethostbyname(socket.gethostname())

ray.init()

# Create actors with different resource demands
actor1 = Actor.options(num_cpus=2).remote()
actor2 = Actor.options(num_cpus=2).remote()

print(ray.get(actor1.get_cluster_resources.remote()))
print(ray.get(actor2.get_cluster_resources.remote()))
