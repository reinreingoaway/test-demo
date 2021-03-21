import json
import pytest

from aws_cdk import core
from backend.backend_stack import BackendStack


def get_template():
    app = core.App()
    BackendStack(app, "backend")
    return json.dumps(app.synth().get_stack("backend").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
