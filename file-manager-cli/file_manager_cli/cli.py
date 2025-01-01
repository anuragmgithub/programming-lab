import click
from .file_operations import search_files, move_file, delete_file, compress_directory, display_file_stats

@click.group()
@click.option("--root", default=".", help="Root directory for file operations.")
@click.pass_context
def file_manager(ctx, root):
    """File Manager CLI Tool"""
    ctx.ensure_object(dict)
    ctx.obj["ROOT"] = root

@file_manager.command()
@click.argument("pattern")
@click.pass_context
def search(ctx, pattern):
    """Search for files matching a pattern."""
    search_files(ctx.obj["ROOT"], pattern)

@file_manager.command()
@click.argument("source")
@click.argument("destination")
@click.option("--copy", is_flag=True, help="Copy instead of move.")
@click.pass_context
def move(ctx, source, destination, copy):
    """Move or copy a file."""
    move_file(ctx.obj["ROOT"], source, destination, copy)

@file_manager.command()
@click.argument("path")
@click.pass_context
def delete(ctx, path):
    """Delete a file."""
    delete_file(ctx.obj["ROOT"], path)

@file_manager.command()
@click.argument("directory")
@click.argument("output")
@click.pass_context
def compress(ctx, directory, output):
    """Compress a directory into a zip file."""
    compress_directory(ctx.obj["ROOT"], directory, output)

@file_manager.command()
@click.argument("path")
@click.pass_context
def stats(ctx, path):
    """Display statistics of a file."""
    display_file_stats(ctx.obj["ROOT"], path)

if __name__ == "__main__":
    file_manager()
