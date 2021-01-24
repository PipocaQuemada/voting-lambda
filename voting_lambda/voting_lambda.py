from aws_cdk import (core,
                     aws_apigateway as apigateway,
                     aws_lambda as lambda_)

class VotingLambda(core.Construct):
    def __init__(self, scope: core.Construct, id: str):
        super().__init__(scope, id)

        handler = lambda_.Function(self, "Voting",
                    runtime=lambda_.Runtime.PYTHON_3_8,
                    code=lambda_.Code.from_asset("resources"),
                    handler="voting.handler",
                    environment=dict()
                    )

        api = apigateway.RestApi(self, "voting-api",
                  rest_api_name="Voting Service",
                  description="This service runs elections using STAR.")

        get_widgets_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_widgets_integration)   # GET /
