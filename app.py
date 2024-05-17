#!/usr/bin/env python3
import os

import aws_cdk as cdk

from iacfinalexam.iacfinalexam_stack import IacfinalexamStack


app = cdk.App()
IacfinalexamStack(app, "IacfinalexamStack",


    env=cdk.Environment(account="529089064156", region="us-east-1")
)

app.synth()





