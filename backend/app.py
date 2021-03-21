#!/usr/bin/env python3

from aws_cdk import core

from backend.backend_stack import BackendStack


app = core.App()
BackendStack(app, "backend", env={'region': 'eu-central-1'})

app.synth()
