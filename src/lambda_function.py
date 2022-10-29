import json
import boto3
from botocore import exceptions

def start_ec2():

    desc = boto3.client('ec2')
    ec2 = boto3.resource('ec2')

    tag_key = 'gpu'
    tag_val = 'yes'
        
    instances = desc.describe_instances(Filters=[{'Name': 'tag:'+tag_key, 'Values': [tag_val]}])
   
    ec2.start_instances(InstanceIds=[instances], DryRun=False)

def add_variables_to_ssm(to_be_added):
    ssm = boto3.client('ssm')
    ssm.put_parameter(
            Name=to_be_added,
            Description=to_be_added,
            Value=to_be_added,
            Type='String',
            KeyId='string',
            Overwrite=True,
            AllowedPattern='string',
            Tags=[
                {
                    'Key': 'gpu',
                    'Value': 'yes'
                },
            ],
            Tier='Standard',
            Policies='string',
            DataType='string'
        )
    

def lambda_handler(event, context):
    # from form-data
    algo_of_hash = event['algo']
    hash_to_crack = event['hash']
    wordlist = event = ['wordlist']
    
    start_ec2()

    add_variables_to_ssm(algo_of_hash)
    add_variables_to_ssm(hash_to_crack)
    add_variables_to_ssm(wordlist) 
        
