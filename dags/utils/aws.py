import awswrangler as wr
import boto3
import pandas as pd
from airflow.models import Variable
from faker import Faker


def aws_sesion():
    
    session = boto3.Session(
        aws_access_key_id = Variable.get("access_key"),
        aws_secret_access_key = Variable.get("secret_access_key"),
        region_name = "eu-central-1"
    )
    return session


