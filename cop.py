# Using Client Method
# import boto3

# s3_client = boto3.client('s3')
# copy_source = {
     # 'Bucket': 'firsts3bucket-0afca213-8e06-49e8-b2b3-168c118d961f',
   # ' Key': 'file.txt'
# }
# s3_client.copy(copy_source, 'seconds3bucket-fb10d6d1-dfea-4cca-9dbd-43b131d5903b', 'file4.txt')


#  Using Resource  Method

import boto3

s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'firsts3bucket-0afca213-8e06-49e8-b2b3-168c118d961f',
    'Key': 'file.txt'
}
s3.Bucket('seconds3bucket-fb10d6d1-dfea-4cca-9dbd-43b131d5903b').copy(copy_source, 'file7.txt')
