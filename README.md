<p align="center">
  <img alt="Tech Squawks" src="./images/logo.svg">
</p>
<p align="center">
  <a href="https://travis-ci.com/MichaelStott/KivMob"><img alt="Build Status" src="https://travis-ci.com/MichaelStott/KivMob.svg?branch=master"></a>
  <a href="https://badge.fury.io/py/kivmob"><img alt="pypi" src="https://badge.fury.io/py/kivmob.svg"></a>
  <a href="https://www.python.org/downloads/release/python-270/"><img alt="Python Version" src="https://img.shields.io/badge/python-3.0-green.svg"></a>
  <a href="https://pepy.tech/project/kivmob"><img alt="Code Climate" src="https://pepy.tech/badge/kivmob"></a>
  <a href="https://codeclimate.com/github/MichaelStott/KivMob/maintainability"><img alt="Code Climate" src="https://api.codeclimate.com/v1/badges/add8cd9bd9600d898b79/maintainability"></a>
  <a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="http://kivmob.com"><img alt="badges" src="https://img.shields.io/static/v1?label=badges&message=yes&color=blue"/></a>
</p>

<p align="center">
A website for learning cloud computing concepts using programming languages such as Python <img style="height: 1em" alt="Tech Squawks" src="./images/pythonparrot.gif">, Go <img  style="height: 1em" alt="Tech Squawks" src="./images/partygopher.gif">, and Node <img  style="height: 1em" alt="Tech Squawks" src="./images/nodeparrot.gif">.
</p>

## About

Originally, I had compiled study notes in a private repository while studying for the AWS Solutions Architect certification. The goal of 
this project is to rewrite, organize, and present those notes in a more digestible format to help reinforce those topics for the purpose 
of studying for the professional level certification and to aid newcomers to AWS and cloud engineering.

Rather than frontload sections with theory and detailed explanations followed by lengthy and convoluted examples switching between the AWS 
Console, downloading bulky files, etc. etc., the aim is have a more W3-esque style, with short explanations with small, self contained 
examples of cloud applications. To achieve this, cloud infrastructure and services are manage through Pulumi. Pulumi allows users to
express their cloud architecture using programming languages such as Python, Golang, Typescript, or Javascript. Time will tell how well 
the website achives this.

Flashcards are included at the end of each section to help reinforce concepts covered in the section.

## Local

To launch the website locally, you will need to install `hugo`:

```
$ cd web
$ hugo server -D
```

## Deploy

```
$ pulumi stack select dev
$ pulumi up
```
