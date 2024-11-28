import sys
import click
from . import hello, predict, simulate

@click.group()
def driver():
    """Top-level CLI for Afronomy."""
    pass

# Add CLI as a subcommands to main driver
driver.add_command(hello.main, "hello")
driver.add_command(predict.main, "predict")
driver.add_command(simulate.main, "simulate")

if __name__ == "__main__":
    sys.exit(driver())
