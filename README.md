[![Python application test with Github Actions](https://github.com/HimaBindhuG/devops-2022/actions/workflows/main.yml/badge.svg)](https://github.com/HimaBindhuG/devops-2022/actions/workflows/main.yml)



# devops-2022
repo for devops

## process for prototyping 

1. try idea out in ipython
2. make a function
3. build a  command-line tool.



# how to use boto3 and aws to translate


[boto 3 translate docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#client)

[Api Languages](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html)

"""
response = client.create_parallel_data(
    Name='string',
    Description='string',
    ParallelDataConfig={
        'S3Uri': 'string',
        'Format': 'TSV'|'CSV'|'TMX'
    },
    EncryptionKey={
        'Type': 'KMS',
        'Id': 'string'
    },
    ClientToken='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)
"""

example of text:

"""python
text = "AWS Lambda is a compute service that lets you run code with out provisioning or managing servers."
"""
