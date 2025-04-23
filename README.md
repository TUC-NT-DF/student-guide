# Student Guide

[![build status](https://github.com/tuc-nt-df/student-guide/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/tuc-nt-df/student-guide/tree/main)

You can view the rendered version at [this website](https://tuc-nt-df.github.io/student-guide/).

## Contribution

Your help is very much appreciated. For more information, please see our [contribution guide](./CONTRIBUTING.md) and the [Collective Code Construction Contract](https://github.com/link-developers/rfcs/blob/master/docs/001.md) (C4).

## Local preview

You can preview the guide locally.

For this you need to install the following packages via Mamba/Conda:

```sh
conda create -n stu-guide -y mkdocs mkdocs-git-revision-date-localized-plugin mkdocs-material mkdocs-material-extensions
conda activate stu-guide
```

Then you can execute the following command in the root of the repository:

```
mkdocs serve
```

It will then start a small web server that hosts the rendered guide.
The URL for you to access the guide is shown in the terminal:

```
INFO    -  Serving on http://127.0.0.1:8000
```

## Linting on the command line

```console
$ # install prequisites
$ mamba install nodejs
$ npm install markdownlint-cli2 --global

$ # do the actual linting (must be done from repository root directory)
$ markdownlint-cli2 README.md "docs/**/*.md"
markdownlint-cli2 v0.6.0 (markdownlint v0.27.0)
Finding: docs/**/*.md
Linting: 22 file(s)
Summary: 0 error(s)
```

## Maintainers

- Matthias Gabriel (maintainer, original author)
