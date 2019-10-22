aws cloudformation create-stack \
    --stack-name kcluster-workers-stack \
    --template-body file://Eks-nodegroup.yml \
    --parameters ParameterKey=KeyName,ParameterValue=eks-key \
    ParameterKey=Subnets,ParameterValue=subnet-024662537fc31609a\\,subnet-0667bffb74feecc8f\\,subnet-09a1a571d3f28d117\\,subnet-0de049550a6c2ae72 \
    ParameterKey=VpcId,ParameterValue=vpc-01afa29aa4ff90aa9 \
    ParameterKey=ClusterControlPlaneSecurityGroup,ParameterValue=sg-0b1cdd3a6df6b0052 \
    --capabilities CAPABILITY_IAM
