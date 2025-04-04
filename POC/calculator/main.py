import click
from calculator import operations

def two_int_args(fn):
    fn = click.argument("a", type=int)(fn)
    fn = click.argument("b", type=int)(fn)
    return fn


@click.group()
def cli():
    """A simple calculator CLI."""
    pass

@cli.command()
@two_int_args
def add(a,b):
    """Add two numbers."""
    result = operations.add(a, b)
    click.echo(f"The result of {a} + {b} is: {result}")

@cli.command()
@two_int_args
def subtract(a,b):
    """Subtract two numbers."""
    result = operations.subtract(a, b)
    click.echo(f"The result of {a} - {b} is: {result}")

@cli.command()
@two_int_args
def multiply(a,b):
    """Multiply two numbers."""
    result = operations.multiply(a, b)
    click.echo(f"The result of {a} * {b} is: {result}")

@cli.command()
@two_int_args
def divide(a,b):
    """Divide two numbers."""
    try:
        result = operations.divide(a, b)
        click.echo(f"The result of {a} / {b} is: {result}")
    except ValueError as e:
        click.echo(e)

@cli.command()
@two_int_args
def power(a,b):
    """Raise a number to the power of another."""
    result = operations.power(a, b)
    click.echo(f"The result of {a} ** {b} is: {result}")

if __name__ == '__main__':
    cli()
