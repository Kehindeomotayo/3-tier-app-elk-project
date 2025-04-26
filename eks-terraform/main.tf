resource "aws_eks_node_group" "eks_nodes_1" {
  cluster_name    = aws_eks_cluster.eks.name
  node_group_name = "eks-node-group-1"
  node_role_arn   = aws_iam_role.eks_node_role.arn
  subnet_ids      = var.subnet_ids
<<<<<<< HEAD
  instance_types  = ["t2.micro"]

=======
  instance_types  = ["t3.medium"]
  
>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }
}

resource "aws_eks_node_group" "eks_nodes_2" {
  cluster_name    = aws_eks_cluster.eks.name
  node_group_name = "eks-node-group-2"
  node_role_arn   = aws_iam_role.eks_node_role.arn
  subnet_ids      = var.subnet_ids
<<<<<<< HEAD
  instance_types  = ["t2.micro"]

=======
  instance_types  = ["t3.small"]
  
>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }
}
