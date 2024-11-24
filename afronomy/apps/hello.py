#!/usr/bin/env python
import click

def hello(name: str) -> str:
    """Function that returns a greeting string."""
    return f"Hello {name}"

@click.command()
@click.option('--name', prompt='Please enter your name', help='The name to greet.')
def main(name):
    """CLI entry point."""
    click.echo(hello(name))

if __name__ == '__main__':
    main()
