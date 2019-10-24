### Create Cluster
aws cloudformation create-stack --stack-name kcluster-stack \
    --template-body file://Eks-on-public-private-subnets.yml

### Create Kubeconfig for local access
./kubeconfig-for-remote-cluster.sh

### Check the remote access
kubectl get nodes
kubectl cluster-info

### Create Worker nodes
Replace the subnet IDs, VpcID and SecurityGroupID below with the ones generated in the first step "Create Cluster", and execute the following command:

aws cloudformation create-stack \
    --stack-name kcluster-workers-stack \
    --template-body file://Eks-nodegroup.yml \
    --capabilities CAPABILITY_IAM

### Authorize the worker nodes to join the cluster
Replace the ARN of the NodeInstanceRole in the auth-config-map.yml with the one  generated in the above step, and execute the following command:

kubectl apply -f auth-config-map.yml

### Check if the nodes joined the cluster
kubectl get nodes
