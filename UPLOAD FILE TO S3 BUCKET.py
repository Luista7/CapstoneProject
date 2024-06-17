import boto3


def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """Upload a file to an S3 bucket."""
    if object_name is None:
        object_name = file_name

    # Create an S3 client
    s3_client = boto3.client('s3')

    # Upload the file
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        return False
    else:
        print(f"File uploaded successfully to\
              S3: s3://{bucket_name}/{object_name}")
        return True


# Replace 'your-local-file.csv' with the path to your local CSV file
local_file_name = 'C:\\Users\\lucas\\Downloads\\employeeSheet2.csv'
local_file_name2 = 'C:\\Users\\lucas\\Downloads\\STEELBRAZERDATA.csv'
local_file_name3 = 'C:\\Users\\lucas\\Downloads\\qualitysheet2.csv'
local_file_name4 = 'C:\\Users\\lucas\\Downloads\\scrap_issue_list2.csv'
local_file_name5 = 'C:\\Users\\lucas\\Downloads\\tempsheet2.csv'
# Replace 'your-s3-bucket-name' with the name of your S3 bucket
s3_bucket_name = 'chukwuemeka-capstone-project'


# Replace 'your-s3-object-name.csv'
# with the desired object key/name in the S3 bucket
s3_object_name = 'employeeSheet2.csv'
s3_object_name2 = 'STEELBRAZERDATA.csv'
s3_object_name3 = 'qualitysheet2.csv'
s3_object_name4 = 'scrap_issue_list2.csv'
s3_object_name5 = 'tempsheet2.csv'
# Upload the file to S3
upload_file_to_s3(local_file_name, s3_bucket_name, s3_object_name)
# upload_file_to_s3(local_file_name3, s3_bucket_name, s3_object_name3)
# upload_file_to_s3(local_file_name5, s3_bucket_name, s3_object_name5)
