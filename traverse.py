import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('firsts3bucket-0afca213-8e06-49e8-b2b3-168c118d961f')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
