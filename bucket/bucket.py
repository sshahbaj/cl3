import boto3

s3 = boto3.resource('s3')

def bucket_create():
    bucket_name = input('Name of the bucket(unique): ')
    location = input('Enter Location: ')
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
    'LocationConstraint': location})

def store_data():
    bucket_name = input('Name of the bucket(unique): ')
    data = input('Enter the name of the file to be uploaded: ')
    s3.Object(bucket_name, data).put(Body=open(data, 'rb'))

def get_s3_keys():
    bucket_name = input('Name of the bucket(unique): ')
    conn = boto3.client('s3')
    for key in conn.list_objects(Bucket=bucket_name)['Contents']:
        print(key['Key'])

def list_bucket():
    for bucket in s3.buckets.all():
        print(bucket.name)

def remove_bucket():
    bucket_name = input('Name of the bucket(unique): ')
    bucket = s3.Bucket(bucket_name)
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()


bucket_create()
store_data()
get_s3_keys()
list_bucket()
remove_bucket()
