"""
Console script for whisk. The structure is based on `Click complex example app <https://github.com/pallets/click/blob/master/examples/complex/>`_.
"""
import sys
import click
import whisk
from whisk.cli.whisk_multi_command import WhiskMultiCommand
from whisk.log import configure_logger
import cookiecutter.log
import logging
import platform

@click.command(cls=WhiskMultiCommand)
@click.option('--debug/--no-debug', default=False, help="Enable verbose logging.")
@click.option('--log-file', default=None, help="Log output to a file.")
@click.pass_context
def cli(ctx, debug, log_file):
    """Entry point for the whisk cli."""
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug
    ctx.obj['LOG_FILE'] = log_file
    configure_logger(stream_level='DEBUG' if debug else 'INFO', log_file=log_file)
    cookiecutter.log.configure_logger(stream_level='DEBUG' if debug else 'INFO', debug_file=log_file)
    logger = logging.getLogger(__name__)
    logger.debug("whisk version=%s",whisk.__version__)
    logger.debug("whisk module location=%s",whisk)
    logger.debug("Platform: %s", platform.platform())
    logger.debug("Python Version: %s", platform.python_version())
    logger.debug("Python executable: %s", sys.executable)

if __name__ == "__main__":
    cli()
