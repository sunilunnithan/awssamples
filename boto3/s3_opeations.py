import boto3
import json

# Use aws cli to configure your environment
# aws configure

BUCKET_NAME = "sunilu-awesome-bucket1"
def s3_client():
    client = boto3.client("s3")
    """ :type : pyboto3.s3 """
    return client

# You can list the bucket using aws cli
# aws s3 ls

def create_bucket(bucket_name):
    return s3_client().create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
        "LocationConstraint" : "us-east-2"
    })

def create_bucket_policy():
    policy = {
        "Version" : "2012-10-17",
        "Statement" : [
            {
                "Sid" : "AddPerm",
                "Effect": "Allow",
                "Principal" : "*",
                "Action": ["s3:*"],
                "Resource": ["arn:aws:s3:::sunilu-awesome-bucket1/*"]
            }
        ]
    }

    policy_string = json.dumps(policy)
    return s3_client().put_bucket_policy(
        Bucket= BUCKET_NAME,
        Policy= policy_string
    )

def list_buckets():
    return s3_client().list_buckets()

def get_bucket_policy():
    return s3_client().get_bucket_policy(Bucket=BUCKET_NAME)

def get_bucket_encryption():
    return s3_client().get_bucket_encryption(Bucket=BUCKET_NAME)

def server_side_encrypt_bucket():
    return s3_client().put_bucket_encryption(
        Bucket= BUCKET_NAME,
        ServerSideEncryptionConfiguration= {
            "Rules" : [
                {
                    "ApplyServerSideEncryptionByDefault" : {
                        "SSEAlgorithm" : "AES256"
                    }
                }
            ]

        }
    )

def delete_bucket(bucket_name):
    return s3_client().delete_bucket(bucket_name)


def upload_small_files_to_s3(filename, bucket_name):
    import os
    filepath = os.path.dirname(__file__) + "/" + filename
    return s3_client().upload_file(filepath,Bucket=bucket_name,Key= filename)

### Create a venv and pip install boto3

if __name__ == '__main__':
    # print(create_bucket(BUCKET_NAME))
    # print(create_bucket_policy())
     print(list_buckets())
    # print(get_bucket_policy())
    # print(get_bucket_encryption())
    # print(server_side_encrypt_bucket())
    #print(upload_small_files_to_s3("readme.txt", BUCKET_NAME))
