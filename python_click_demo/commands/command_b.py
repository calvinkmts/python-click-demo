import click

@click.command()
@click.argument("name")
def hello_b(name: str):
    click.echo(f"Hello {name} from function B")