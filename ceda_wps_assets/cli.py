# -*- coding: utf-8 -*-

"""Console script for ceda_wps_assets."""

__author__ = """Ag Stephens"""
__contact__ = "ag.stephens@stfc.ac.uk"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
import sys
import click


from .flamingo import create_dset_configs, get_dset_info 


@click.command()
def main(args=None):
    """Console script for ceda_wps_assets."""
    
    click.echo("Running: flamingo script...")
    click.echo("Replace this message by putting your code into "
               "ceda_wps_assets.cli.main")
    return 0


if __name__ == "__main__":

    sys.exit(main())  # pragma: no cover
