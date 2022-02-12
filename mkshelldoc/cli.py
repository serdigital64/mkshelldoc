import click
import mkshelldoc as mks

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def run():
    pass


@click.command()
@click.option("--source", help="Shell script to parse")
@click.option("--type", help="Shell script type", default=mks.MKSHELLDOC_TYPE_BASH)
@click.option("--format", help="Help style", default=mks.MKSHELLDOC_FORMAT_REST)
@click.option(
    "--output", help="Output format type", default=mks.MKSHELLDOC_OUTPUT_MARKDOWN
)
@click.option(
    "--destination", help="Filename of the document to create", default="api.md"
)
def create(
    source,
    type=mks.MKSHELLDOC_TYPE_BASH,
    format=mks.MKSHELLDOC_FORMAT_REST,
    destination="api.md",
    output=mks.MKSHELLDOC_OUTPUT_MARKDOWN,
):
    document = mks.MkShellDoc(source, type, format, destination, output)
    document.create()


run.add_command(create)
