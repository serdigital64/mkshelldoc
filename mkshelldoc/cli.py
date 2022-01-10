"""Console script for mkshelldoc."""
import sys
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--source', help='Shell script to parse')
@click.option('--type', help='Shell script type', default="bash")
def main(source,type):
    """Console script for mkshelldoc."""
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
