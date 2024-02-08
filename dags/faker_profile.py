import awswrangler as wr
from utils.aws import aws_sesion
from utils.fakers_operations import profile_data_generator


def data_extract_to_s3():

    wr.s3.to_parquet(
                    df = profile_data_generator(200),
                    path = "s3://faker-raw-data/user_profile/",
                    boto3_session = aws_sesion(),
                    mode = "append",  
                    dataset=True
                    )
    return "Data successfully written to s3"





