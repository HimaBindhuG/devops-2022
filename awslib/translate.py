import boto3
#import client
import requests
import os


    

"""
os.environ['AWS_PROFILE'] = "Profile1"
os.environ['AWS_DEFAULT_REGION'] = "us-west-2"

s3 = boto3.client('s3', region_name='us-west-2')
print("[INFO:] Connecting to cloud")

# Retrieves all regions/endpoints that work with S3

response = s3.list_buckets()
print('Regions:', response)

text = "AWS Lambda is a compute service that lets you run code with out provisioning or managing servers."
"""
def translator(text,source='en',target='es'):
    """this uses aws translate to translate text
    valid values: de|en|es|fr|it|ja|ko|pt|zh|zh-TW"""

    print(f"passed in source language: {source}")
    print(f"passed in target language: {target}")

    client = boto3.client('translate')
    response = client.translate_text(
        Text='text',
        SourceLanguageCode='source',
        TargetLanguageCode='target', 
    )
    return response['TranslatedText']