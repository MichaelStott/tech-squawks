<p align="center">
  <img alt="Tech Squawks" src="./images/logo.svg">
</p>

<p align="center">
Cloud computing tutorials in programming languages such as<br/>Python <img  height="16" alt="Tech Squawks" src="./images/pythonparrot.gif">, Go <img  height="16" alt="Tech Squawks" src="./images/partygopher.gif">, and Node <img   height="16" alt="Tech Squawks" src="./images/nodeparrot.gif">.
</p>

## About

The aim of this website is to present cloud-computing concepts using small, self-contained web apps. To achieve this, 
cloud infrastructure and services are manage through Pulumi. Pulumi allows users to express their cloud architecture 
using programming languages such as Python, Golang, Typescript, or Javascript. 

Flashcards are included at the end of each section to help reinforce concepts covered in the section.

## Roadmap

AWS (In-Progress)
- [x] Overview
- [ ] IAM
- [ ] S3
- [ ] EC2
- [ ] VPC
- [ ] Route53
- [ ] CloudWatch
- [ ] CloudTrail
- [ ] RDS
- [ ] Lambda
- [ ] SNS
- [ ] SQS
- [ ] Kinesis
- [ ] SES

Docker (Not-Started)

Kubernetes (Not-Started)

## Development

### Local

To launch the website locally, you will need to install `hugo`:

```
$ cd web
$ hugo server -D
```

### Deploy

```
$ pulumi stack select dev
$ pulumi up
```
