# devops-2022
repo for devops

# how to use boto3 and aws to translate


[boto 3 translate docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/translate.html#client)

```
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
```