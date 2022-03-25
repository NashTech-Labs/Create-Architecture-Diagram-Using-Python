from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3

with Diagram("First Architecture", show=False):
    lb = ELB("lb")
    dns = Route53("dns")
    app = EC2("app")
    database = RDS("database")
    bucket = S3("bucket")

    dns >> lb >> app
    app >> database
    app >> bucket