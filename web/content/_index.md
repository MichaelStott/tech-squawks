---
title: "Welcome!"
date: 2021-01-23T16:49:34-05:00
weight: 1
---

# Howdy!

Welcome to Tech Squawks, a website for learning [AWS](https://aws.amazon.com/) cloud development, using programming 
languages such as Typescript, Javascript, Python, Go, or Java. This site is a work in progress, so check back 
frequently for new tutorials and updates!

Learning cloud computing and AWS development can seem like a daunting task. At the time of writing, there are over 200 
cloud services offered by AWS. The goal of this website is to offer a more hands-on approach to understanding AWS 
development beyond the available documentation by providing code examples of cloud applications to demonstrate 
cloud computing concepts.

In an effort to make these tutorials accesible to those without AWS access and minimize costs, examples are designed 
to be compatible with [LocalStack](https://localstack.cloud/), a framework for running AWS cloud applications on the 
user's local machine, whenever possible. 

Flashcards are included at the end of each section for additional study and review, which may be useful for those wishing to pursue 
certification. These flaschards are publicly hosted on [Cram](https://www.cram.com/) and accesible through both the website and mobile app.

### Severless Webpage Demo

Below is a short example of deploying a small serverless web app. The deploy button will create the stack in the reader's Pulumi account, which can then be deployed using the Pulumi CLI tool.

{{< tabs groupId="code" >}}
{{< tab name="Typescript" >}}
{{% gist MichaelStott fb97da6768443ca12ca6c0c720fe2e89 "homepage_example.ts" %}}
{{% button href="https://github.com/MichaelStott/AWSExamples/tree/master/examples/homepage/ts" icon="fab fa-github" icon-position="left" %}}GitHub{{% /button %}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/AWSExamples/tree/master/examples/homepage/ts" icon="fas fa-cloud-upload-alt" icon-position="left" %}}Deploy{{% /button %}}
{{% button href="https://localstack.cloud/" icon="fas fa-laptop-code" icon-position="left" %}}LocalStack Compatible{{% /button %}}
{{< /tab >}}
{{< tab name="Javascript" >}}

{{% gist MichaelStott fb97da6768443ca12ca6c0c720fe2e89 "homepage_example.js" %}}
{{% button href="https://github.com/MichaelStott/AWSExamples/tree/master/examples/homepage/js" icon="fab fa-github" icon-position="left" %}}View Project{{% /button %}}
{{% button href="https://app.pulumi.com/new?template=https://github.com/MichaelStott/AWSExamples/tree/master/examples/homepage/js" icon="fas fa-cloud-upload-alt" icon-position="left" %}}Deploy{{% /button %}}

{{% button href="https://localstack.cloud/" icon="fas fa-laptop-code" icon-position="left" %}}LocalStack Compatible{{% /button %}}

{{< /tab >}}
{{< tab name="Python" >}}
{{< figure src="parrots/parrotnotfound.gif" title="Not yet available." >}}
{{< /tab >}}
{{< tab name="Go" >}}
{{< figure src="parrots/parrotnotfound.gif" title="Not yet available." >}}
{{< /tab >}}
{{< tab name="Java" >}}
{{< figure src="parrots/parrotnotfound.gif" title="Not yet available." >}}
{{< /tab >}}
{{< /tabs >}}

The exported URL will display the following image in your web browser: 

![squawk](https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif)

### Prerequisites

Before continuing, readers should be:

- Knowledgeable of at least one of the following programming languages: Typescript, Javascript, Python, or Go
- Comfortable with using their local terminal or shell
- Familiar with basic computer networking concepts

For setting up your development environment, see the  [Getting Started]({{< ref "getting_started" >}}) section.