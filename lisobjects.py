import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Specify the bucket name without spaces or region identifiers
bucket_name = 'firsts3bucket-0cec8800-e7ac-4d98-93c7-e906b0eb6d06'

# Example operation: List objects in the bucket
response = s3.list_objects(Bucket=bucket_name)

# Process the response as needed
for obj in response['Contents']:
    print(obj['Key'])
