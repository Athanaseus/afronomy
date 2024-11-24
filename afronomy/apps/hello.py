#!/usr/bin/env python
import os
import click
from omegaconf import OmegaConf
from scabha.schema_utils import clickify_parameters

def hello(name: str) -> str:
    """Function that returns a greeting string."""
    return f"Hello {name}"

@click.command()
@click.option('--name', prompt='Please enter your name', help='The name to greet.')
def main(name):
    """CLI entry point."""
    click.echo(hello(name))

schemas = OmegaConf.load(os.path.join(os.path.dirname(__file__), "cabs/hello.yml"))
print(schemas)

if __name__ == '__main__':
    main()
