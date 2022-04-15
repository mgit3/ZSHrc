import boto3
import pandas as pd

key_file = '/home/roberto/Documents/aws.csv'
df = pd.read_csv(key_file)
AWS_KEY_ID = df['Access key ID'][0]
AWS_SECRET = df['Secret access key'][0]

s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)



bucketName = 'roberto-server'
s3.create_bucket(Bucket= bucketName)
fileSrcHtml = './dataset_speedtest/graph.html'
keyName = 'graph.html';

# Upload the lines.html file to S3
s3.upload_file(Filename=fileSrcHtml, 
               # Set the bucket name
               Bucket=bucketName, Key= keyName,
               # Configure uploaded file
               ExtraArgs = {
                 # Set proper content type
                 'ContentType':'text/html',
                 # Set proper ACL
                 'ACL': 'public-read'})

# Print the S3 Public Object URL for the new file.
print("http://{}.s3.amazonaws.com/{}".format(bucketName, keyName))