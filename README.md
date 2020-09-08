# ![AWS](aws-logo.png) VPC Subnets

Purpose: Blueprint for provisioning subnets.

![AWS VPC Subnets](aws\_vpc\_subnets.png)

## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| aws | n/a |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| cidr\_prefix | The CIDR block | `any` | n/a | yes |
| is\_public | Indicates whether the subnets should be publicly routable (via Internet) | `bool` | `false` | no |
| newbits | The bits added to the cidr block to define the extent of subnets. Note this cannot exceed (24 - cidr\_range)<br><br>Example:<br><br> * CIDR = 10.0.0.1/16<br> * 0 < Newbits <= 8 | `any` | n/a | yes |
| route\_table | Route table to associate with subnets | `any` | n/a | yes |
| vpc\_default | Boolean value to indicate whether the matched VPC should be default for the region | `string` | `"true"` | no |
| vpc\_tags | A map of tags to match on the VPC lookup | `map(any)` | `{}` | no |

## Outputs

No output.

