import boto3

def delete_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    
    # Check if the bucket exists
    if not bucket.creation_date:
        print(f"Bucket {bucket_name} does not exist.")
        return
    
    # Delete all objects in the bucket
    bucket.objects.all().delete()
    
    # Check if versioning is enabled and delete all versions if so
    versioning = s3.BucketVersioning(bucket_name)
    if versioning.status == 'Enabled':
        bucket.object_versions.delete()
    
    # Delete the bucket
    bucket.delete()
    print(f"Bucket {bucket_name} has been deleted.")

# Example usage
bucket_name = 'seconds3bucket-fb10d6d1-dfea-4cca-9dbd-43b131d5903b'
delete_bucket(bucket_name)
