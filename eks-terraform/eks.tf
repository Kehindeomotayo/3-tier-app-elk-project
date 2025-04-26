resource "aws_eks_cluster" "eks" {
  name     = var.cluster_name
<<<<<<< HEAD
  version = var.cluster_version
=======
>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = var.subnet_ids
  }
}
