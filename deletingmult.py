import boto3
from boto3.session import Session

session = Session(aws_access_key_id='your aws key id',
                 aws_secret_access_key='your aws secret key')

s3_resource = session.resource('s3')
my_bucket = s3_resource.Bucket("seconds3bucket-fb10d6d1-dfea-4cca-9dbd-43b131d5903b")

response = my_bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': "file2.txt"   # the_name of_your_file
            },
            {
                'Key': "file4.txt"
            },
            {
                'Key' : "file7.txt"
            }
        ]
    }
)
