import boto3


def start_ec2():
    ec2 = boto3.resource('ec2')

    ec2_instance = {"Name": "instance-type", "Values": ["g4dn.2xlarge"]}
    ec2_tag = {"Name": "tag:Name", "Values": ["hashcat_box"]}

    for instance in ec2.instances.filter(Filters=[ec2_tag]):
        instance.start()

def add_variables_to_ssm(to_be_added):
    ssm = boto3.client('ssm')
    ssm.put_parameter(
            Name=to_be_added,
            Description=to_be_added,
            Value=to_be_added,
            Type='String',
            Overwrite=True,
            Tier='Standard'
        )
    

def lambda_handler(event, context):
    # from form-data
    algo_of_hash = event['algo']
    hash_to_crack = event['hash']
    wordlist = event['wordlist']
    
    start_ec2()

    add_variables_to_ssm(algo_of_hash)
    add_variables_to_ssm(hash_to_crack)
    add_variables_to_ssm(wordlist) 
        
