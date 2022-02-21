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

These tutorials are very much a work-in-progress.

## Roadmap

The following topics are planned in the order they are listed. No fixed date for these topics exists as of yet.

### AWS (🚧 In-Progress)
- [x] AWS Environment 
- [x] IAM
- [x] S3
- [ ] EC2 (🚧 In-Progress)
- [ ] VPC (🚧 In-Progress)
- [ ] Route53
- [ ] CloudWatch
- [ ] CloudTrail
- [ ] RDS
- [ ] Lambda
- [ ] SNS
- [ ] SQS
- [ ] Kinesis
- [ ] SES

### Docker (Not-Started)
- Content TBD

### Kubernetes (Not-Started)
- Content TBD

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
