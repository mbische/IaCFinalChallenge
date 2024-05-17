from constructs import Construct
from aws_cdk import (
    Stage
)
from iacfinalexam_stack import IacfinalexamStack

class IacfinalexamStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = IacfinalexamStack(self, 'JaveProject')