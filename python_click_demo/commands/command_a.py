import click

@click.command()
def hello_a():
    click.echo("Hello World from function A")