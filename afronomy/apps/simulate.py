#!/usr/bin/env python
import os
import click
import numpy as np

from omegaconf import OmegaConf
from scabha.schema_utils import clickify_parameters

from afronomy.utils.utils import corrupt_vis, compute_res, correct_obs 


schemas = OmegaConf.load(os.path.join(os.path.dirname(__file__), "../cabs/simulate.yml"))

@click.command('simulate')
@clickify_parameters(schemas.cabs.get('simulate'))
def main(**kwargs):
    """
    CLI entry point for the simulate app.

    This app corrupts a measurement set (MS) visibilities column.

    Args:
        **kwargs: Command-line arguments including:
            msname (str): Path to the measurement set.
            column (str): Column name where the visibilities will be stored.

    Returns:
        None
    """
    corrupt_vis(**kwargs)
