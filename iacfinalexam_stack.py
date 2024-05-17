from aws_cdk import (
    # Duration,
    aws_codebuild as codebuild,
    aws_codecommit as codecommit,
    pipelines as pipelines,
    aws_iam as iam,
    Stack,
    Stage,
    # aws_sqs as sqs,
)

import aws_cdk.aws_codepipeline as codepipeline
import aws_cdk.aws_s3 as s3

import aws_cdk.aws_codecommit as codecommit
from aws_cdk import cloudformation_include as cfn_inc

from iacfinalexam_stage import IacfinalexamStage

from constructs import Construct

class IacfinalexamStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repo_template = cfn_inc.CfnInclude(self, "Template",
            template_files="app-codebuild-template.json"
        )

        
        repo = codecommit.Repository(self, "repository", repository_name="iacfinalexam_repo")
        
        repo_template = repo
        
        pipeline = codepipeline.CodePipeline(self, "Pipeline",
            synth=repo.ShellStep(
                "Synth",
                input=repo.CodePipelineSource.code_commit(repo, "main"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "npx cdk synth",
                ]
            ),
        )

        deploy = IacfinalexamStage(self, "Deploy")
        deploy_stage = pipeline.add_stage(deploy)
        
        codebuild.Project(self, "PlaceToStoreFiles",
        source=codebuild.Source.code_commit(repository=repo)
        )
        
        bucket = s3.Bucket(self, "iacfinalexambucket")

        codebuild.Project(self, "MyProject",
        source=codebuild.Source.s3(
        bucket=bucket,
        path="java-project.zip"
        )
        )

