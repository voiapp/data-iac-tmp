"""CLI entry point"""
import logging
from distutils.command.config import config
from pathlib import Path

import typer
from pulumi.automation import (
    ConfigValue,
    LocalWorkspaceOptions,
    ProjectBackend,
    ProjectRuntimeInfo,
    ProjectSettings,
    StackSettings,
    create_stack,
)

LOG = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def main() -> None:
    """Main group for iac cli"""
    print("hello")
    LOG.info("Iac cli")


@app.command()
def pulumi_wrapper(environment: str = "loadiissh") -> None:
    """Pulumi wrapper"""
    # import pdb; pdb.set_trace()
    LOG.info("Parsing and validating porter file {config_path}")
    create_stack(
        project_name="service-snowflake",
        work_dir="service-snowflake",
        stack_name=f"service-snowflake.{environment}",
        opts=LocalWorkspaceOptions(
            env_vars={"PULUMI_CONFIG_PASSPHRASE": ""},
            #secrets_provider="gcpkms://projects/voi-data-warehouse/locations/eu-zone-3",
            project_settings=ProjectSettings(
                name="project_name",
                runtime=ProjectRuntimeInfo(name="python", options={"virtualenv": "venv"}),
                description="A minimal Google Cloud Python Pulumi program",
s            ),
            stack_settings={
                f"service-snowflake.{environment}": StackSettings(
                    encryption_salt="abc", config={"gcp:project": "voi-data-warehouse"}
                )
            },
        ),
    )
    import pdb; pdb.set_trace()
    # stack.set_config("gcp:project", ConfigValue(value="voi-data-warehouse"))
    # stack.refresh(on_output=print)


def pulumi_wrapper(list_files, action, environment):
    set_of_parents = {parent for parent in list_files}
    for parent in set_of_parents:
        stack = create_stack("iac/parent")
        if environment == "dev":
            if action == "created":
                stack.init
            if action == "created-modified":
                stack.init
        if environment == "prod":
            if action == "created-modified":
                stack.up
            if action == "created-modified":
                stack.destroy


#            "opts": LocalWorkspaceOptions(
#                project_settings=self.project_settings,
#                env_vars=self.env_vars,
#                secrets_provider=secrets_provider,
#                stack_settings={stack_name: stack_settings},
#            )

if __name__ == "__main__":
    app()
