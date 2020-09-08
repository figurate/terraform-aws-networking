from diagrams import Diagram, Cluster
from diagrams.aws.network import PrivateSubnet, RouteTable

with Diagram("AWS VPC Subnets", show=False, direction="TB"):

    route_table = RouteTable("route table")

    with Cluster("vpc"):

        route_table << [
            PrivateSubnet("subnet a"),
            PrivateSubnet("subnet b"),
            PrivateSubnet("subnet c")
        ]

