<p align="center">
  <img alt="Tech Squawks" src="./images/logo.svg">
</p>

<p align="center">
Cloud computing tutorials in programming languages such as Node (Typescript/Javascript)<img   height="16" alt="Tech Squawks" src="./images/nodeparrot.gif">,<br/>Python <img  height="16" alt="Tech Squawks" src="./images/pythonparrot.gif">, and Go <img  height="16" alt="Tech .Squawks" src="./images/partygopher.gif">.
</p>


## About

The aim of this website is to present cloud-computing concepts using small, self-contained web apps. To achieve this, 
cloud infrastructure and services are managed with Pulumi. Pulumi allows users to easilty define their cloud resources 
using programming languages such as Python, Golang, Typescript, or Javascript. 

Flashcards are included at the end of each section to help reinforce concepts covered in the section.

These tutorials are very much a work-in-progress. As a result, the site structure and URLs may be subject to change. 

## Roadmap

The following topics are planned in the order they are listed. No fixed date for these topics exists as of yet.

### AWS (🚧 In-Progress)
- [x] AWS Environment 
- [x] IAM
- [x] S3
- [ ] EC2 (🚧 In-Progress)
- [ ] ELB (🚧 In-Progress)
- [ ] VPC (🚧 In-Progress)
- [ ] KMS
- [ ] Route53
- [ ] CloudWatch
- [ ] CloudTrail
- [ ] Lambda
- [ ] Step Functions
- [ ] SNS
- [ ] SQS
- [ ] Kinesis
- [ ] SES
- [ ] RDS
- [ ] DynamoDB
- [ ] Secrets Manager
- [ ] STS
- [ ] Config

### Docker (Not-Started)
- [ ] Introduction
- Content TBD
(Need to outline)

### Kubernetes (Not-Started)
- [ ] Introduction
- Content TBD

## Development

### Local

To launch the website locally, you will need to install `hugo`:

```
$ cd web
$ hugo server
```

To build the website with drafts included, run `hugo server -D`

### Deploy

```
$ pulumi stack select dev
$ pulumi up
```
