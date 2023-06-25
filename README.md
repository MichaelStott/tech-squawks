<p align="center">
  <img alt="Tech Squawks" src="./images/logo.svg">
</p>

<p align="center">
Cloud computing tutorials in programming languages such as Node (Typescript/Javascript)<img   height="16" alt="Tech Squawks" src="./images/nodeparrot.gif">,<br/>Python <img  height="16" alt="Tech Squawks" src="./images/pythonparrot.gif">, and Go <img  height="16" alt="Tech .Squawks" src="./images/partygopher.gif">.
</p>

## About

The aim of this website is to present cloud-computing concepts using small, self-contained code examples. To achieve this, 
cloud infrastructure and services are managed with Pulumi, which allows cloud resources to be defined using programming languages such as Typescript, Javascript, Python, and Go 

Flashcards will be included at the end of each section (once content is finalized) to help reinforce key concepts.

These tutorials are very much a work-in-progress. As a result, the site structure and URLs may be subject to change. 

## Development

### Website

To launch the website locally, you will need to install `hugo`:

```
$ cd web
$ hugo server
```

To build the website with drafts included, run `hugo server -D`

To sync any code examples referenced in the webpage markdown, run `npm run sync`

### Code Examples

All code examples can be found under the `code` directory. All should be 
deployable via:

```
$ pulumi up
```

The CI/CD pipeline should automatically detect new or modified projects and
ensure that `pulumi preview` runs successfully.

## Deployment

```
$ pulumi stack select dev
$ pulumi up
```
