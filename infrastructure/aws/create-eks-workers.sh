aws cloudformation create-stack \
    --stack-name kcluster-workers-stack \
    --template-body file://Eks-nodegroup.yml \
    --parameters ParameterKey=KeyName,ParameterValue=eks-key \
    ParameterKey=Subnets,ParameterValue=subnet-0166f9dad3402796f\\,subnet-07465738ab9615a72\\,subnet-07556cb1cd41dbd52\\,subnet-0cce83889a1da7939 \
    ParameterKey=VpcId,ParameterValue=vpc-0094328f898232c42 \
    ParameterKey=ClusterControlPlaneSecurityGroup,ParameterValue=sg-0983f83b477416be0 \
    --capabilities CAPABILITY_IAM
