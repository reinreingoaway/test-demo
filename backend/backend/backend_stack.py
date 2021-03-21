from aws_cdk import core, aws_dynamodb, aws_iam


class BackendStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.role = aws_iam.Role(
            self,
            id="something-role",
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'),
        )
        self.role.add_managed_policy(aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole'))

        self.table = aws_dynamodb.Table(
            self,
            id="SomethingTable",
            table_name=f"something-table",
            billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
            partition_key=aws_dynamodb.Attribute(
                name='something_id',
                type=aws_dynamodb.AttributeType.STRING
            ),
        )
        self.table.grant_full_access(self.role)
