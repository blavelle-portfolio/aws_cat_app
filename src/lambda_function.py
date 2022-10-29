import json
import boto3

def start_ec2():
    ec2 = boto3.resource('ec2')

    tag_key = "gpu"
    tag_val = "yes"
    instances = ec2.describe_instances(Filters=[{'Name': 'tag:'+tag_key, 'Values': [tag_val]}])

    try:
        response = ec2.start_instances(InstanceIds=[instances], DryRun=False)
        return response
    except ClientError as e:
        return e

def add_variables_to_ssm(to_be_added):
    ssm = boto3.client('ssm')
    
    try:
        resposne = ssm.put_parameter(
            Name=to_be_added
            Description='added from lambda',
            Value=to_be_added,
            Type='String',
            Overwrite=True,
            Tier='Standard',
            DataType='string')
        return response
    except CLientError as e:
        return e
    

def lambda_handler(event, context):
    # from form-data
    algo_of_hash = json.loads["Metadata"]["algo"]
    hash_to_crack = json.loads["Metadata"]["hash"]
    wordlist = json.loads["Metadata"]{"wordlist"}

    try: 
        start_ec2()
        add_variables_to_ssm(algo_of_hash)
        add_variables_to_ssm(hash_to_crack)
        add_variables_to_ssm(wordlist) 
        
        return {"statusCode": 200, "body": json.dumps("Hash uploaded successfully! Please check your email for the output")}
    
    except CLientError as e:
        return e

