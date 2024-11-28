#!/usr/bin/env python
import os
import sys
import click
from omegaconf import OmegaConf
from scabha.schema_utils import clickify_parameters

def hello(name: str) -> str:
    """Function that returns a greeting string."""
    return f"Hello {name}"

def write_greeting_to_file(name: str, outfile: str = "hello.txt") -> None:
    """
    Writes the greeting string to a specified text file.

    Args:
        name (str): The name to include in the greeting.
        outfile (str, optional): The path to the text file. Defaults to 'hello.txt'.

    Returns:
        None
    """
    click.echo(hello(name))
    if outfile:
        greeting = hello(name)
        with open(outfile, 'w') as file:
            file.write(greeting)

schemas = OmegaConf.load(os.path.join(os.path.dirname(__file__), "../cabs/hello.yml"))

@click.command('hello')
@clickify_parameters(schemas.cabs.get('hello'))
def main(**kwargs):
    """CLI entry point for hello app."""
    write_greeting_to_file(**kwargs)

