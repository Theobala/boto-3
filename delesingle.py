import boto3

s3 = boto3.resource('s3')
s3.Object('firsts3bucket-0afca213-8e06-49e8-b2b3-168c118d961f', 'file.txt').delete()
