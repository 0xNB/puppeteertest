"""Parser for some startup arguments"""

import argparse
import os

from flathunter.config import Env


def parse():
    """Processes and return command-line arguments"""
    parser = argparse.ArgumentParser(
        description=("Scrapes real estate data from multiple real estate sources"
                     " and makes them available over a REST interface"),
        epilog="Designed by Niklas"
    )
    if Env.FLATHUNTER_TARGET_URLS is not None:
        default_config_path = None
    else:
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        default_config_path = f"{root_dir}/config.yaml"
    parser.add_argument('--config', '-c',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        default=default_config_path,
                        help=f'Config file to use. If not set, try to use "{default_config_path}"'
                        )
    parser.add_argument('--heartbeat', '-hb',
                        action='store',
                        default=None,
                        help=('Set the interval time to receive heartbeat messages to check'
                              'that the bot is alive. Accepted strings are "hour", "day", "week".'
                              'Defaults to None.')
                        )
    return parser.parse_known_args()[0]
