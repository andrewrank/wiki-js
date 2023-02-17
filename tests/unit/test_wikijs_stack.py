import aws_cdk as core
import aws_cdk.assertions as assertions

from wikijs.wikijs_stack import WikijsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in wikijs/wikijs_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WikijsStack(app, "wikijs")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
