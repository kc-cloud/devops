aws eks --region us-east-1 create-cluster --name kCluster --kubernetes-version 1.14 \
--role-arn arn:aws:iam::612474429126:role/EKSServiceRole \
--resources-vpc-config subnetIds=subnet-58cff23f,subnet-a3566d8d,securityGroupIds=sg-c060d890
