import boto3

# IAM
iam = boto3.client('iam')

user_name = 'ManasiDemoUser'

try:
    iam.create_user(UserName=user_name)
    print(f"IAM User Created: {user_name}")
except Exception as e:
    print("IAM Error:", e)

# S3
s3 = boto3.client('s3')

bucket_name = 'manasi-demo-bucket-2026-unique123'

try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )
    print(f"S3 Bucket Created: {bucket_name}")
except Exception as e:
    print("S3 Error:", e)

# EC2
ec2 = boto3.resource('ec2')

try:
    instance = ec2.create_instances(
        ImageId='ami-0d682f26195e9ec0f',
        MinCount=1,
        MaxCount=1,
        InstanceType='t3.micro'
    )

    print("EC2 Instance Created")
    print("Instance ID:", instance[0].id)

except Exception as e:
    print("EC2 Error:", e)