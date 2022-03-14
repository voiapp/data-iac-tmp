# data-iac
This project contains the Infrastructure As Code



# Infrastructure as Code

Our first experiments with Pulumi. For now, **not** automated yet for CI runs.

Folder structure inspired
by [Terraform WoW v2](https://voidev.atlassian.net/wiki/spaces/VOIENGP/pages/79318384740/Terraform+Way+of+Working+v2).

## Setting up

1. Install Pulumi: `brew install pulumi`
2. Authenticate against our GCS backend: `pulumi login gs://voi-data-pulumi-state`

## Creating a new project

```shell
$ mkdir service-tableau
$ cd service-tableau
$ pulumi new gcp-python --generate-only
```

As a stack, use `<project-name>.<environment>` (example: `service-tableau.prod`). We need to namespace the environment
because of a Pulumi limitation when using self-hosted backends. https://github.com/pulumi/pulumi/issues/2522

## Running

On each project (folder):

```shell
$ pulumi up
```

If you get an error related to passphrase, do:

```shell
$ export PULUMI_CONFIG_PASSPHRASE=""
```
