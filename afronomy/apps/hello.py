#!/usr/bin/env python
import os
import sys
import click
from omegaconf import OmegaConf
from scabha.schema_utils import clickify_parameters

def hello(name: str) -> str:
    """Function that returns a greeting string."""
    return f"Hello {name}"

@click.group()
@click.option('--name', prompt='Please enter your name', help='The name to greet.')
def main(name):
    """CLI entry point."""
    click.echo(hello(name))

schemas = OmegaConf.load(os.path.join(os.path.dirname(__file__), "../cabs/hello.yml"))

def clickify(name, schema_name=None):
    schema_name = schema_name or name
    return lambda func: \
        main.command(name, help=schemas.cabs.get(f'afronomy.{schema_name}').info,no_args_is_help=True)(
                clickify_parameters(schemas.cabs.get(f'afronomy.{schema_name}'))(func)
        )

if __name__ == '__main__':
    sys.exit(main())
