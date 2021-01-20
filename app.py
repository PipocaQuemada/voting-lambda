#!/usr/bin/env python3

from aws_cdk import core

from voting_lambda.voting_lambda_stack import VotingLambdaStack


app = core.App()
VotingLambdaStack(app, "voting-lambda")

app.synth()
