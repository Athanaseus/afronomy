#!/usr/bin/env python
import os
import sys
import click
from omegaconf import OmegaConf
from scabha.schema_utils import clickify_parameters

@click.command()
@click.argument('name')
@click.option('-o', '--outfile', default='hello.txt', help='Path to the output text file.')
def main(name, outfile):
    """CLI entry point."""
    click.echo(hello(name))
    write_greeting_to_file(name, outfile)

def hello(name: str) -> str:
    """Function that returns a greeting string."""
    return f"Hello {name}"

def write_greeting_to_file(name: str, file_path: str = "hello.txt") -> None:
    """
    Writes the greeting string to a specified text file.

    Args:
        name (str): The name to include in the greeting.
        file_path (str, optional): The path to the text file. Defaults to 'hello.txt'.

    Returns:
        None
    """
    greeting = hello(name)
    with open(file_path, 'w') as file:
        file.write(greeting)

schemas = OmegaConf.load(os.path.join(os.path.dirname(__file__), "../cabs/hello.yml"))

def clickify(name, schema_name=None):
    schema_name = schema_name or name
    return lambda func: \
        main.command(name, help=schemas.cabs.get(f'afronomy.{schema_name}').info,no_args_is_help=True)(
                clickify_parameters(schemas.cabs.get(f'afronomy.{schema_name}'))(func)
        )
