import click

# Define a command group
@click.group()
def task_manager():
    """Task Manager CLI - Add, List, and Remove tasks."""
    pass

# Command 1: Add a new task
@click.command()
@click.argument('task')
def add(task):
    """Add a new task."""
    click.echo(f"Task added: {task}")

# Command 2: List all tasks
@click.command()
def list_tasks():
    """List all tasks."""
    click.echo("Listing all tasks...")

# Command 3: Remove a task
@click.command()
@click.argument('task_id', type=int)
def remove(task_id):
    """Remove a task by its ID."""
    click.echo(f"Task {task_id} removed.")

# Register the commands under the task_manager group
task_manager.add_command(add)
task_manager.add_command(list_tasks)
task_manager.add_command(remove)

# Run the CLI
if __name__ == '__main__':
    task_manager()
