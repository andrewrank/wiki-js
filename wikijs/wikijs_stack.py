from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

with open(r'wikijs\scripts\install.sh') as f:
    user_data = f.read()

class WikijsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        myVpc = ec2.Vpc(self, 'WikiJsVpc',
            ip_addresses=ec2.IpAddresses.cidr('10.11.0.0/24')
            )

        mySg = ec2.SecurityGroup(self, "mySg",
            vpc = myVpc,
            allow_all_outbound=True)
        mySg.connections.allow_from_any_ipv4(
            port_range=ec2.Port.tcp(22)
        )

        myEc2A = ec2.Instance(self, "MyEc2InstanceA",
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3,ec2.InstanceSize.LARGE),
            vpc=myVpc,
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            security_group=mySg,
            user_data=ec2.UserData.custom(user_data)
        )


    
