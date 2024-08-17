import click

from python_click_demo.commands.command_a import hello_a
from python_click_demo.commands.command_b import hello_b

@click.group()
def cli():
    pass

cli.add_command(hello_a)
cli.add_command(hello_b)

if __name__ == "__main__":
    cli()