import click

@click.command()
@click.option('--name', prompt='Please enter your name', help='The name to greet.')
def hello(name):
    """Prints 'Hello name' to the terminal from input."""
    click.echo(f"Hello {name}")

if __name__ == '__main__':
    hello()
