import uiautomator2 as u2
import os
import sys
import time
import yaml
import json
import argparse

from subroutines import *
from info import BusinessInfo
from dataclasses import asdict

from rich.console import Console
console = Console()

#####################################################
# read config (device info, etc.)
with open('config.yaml') as f:
    config = yaml.safe_load(f)

d = u2.connect(config['usbserial'])
d.implicitly_wait(config['timeout'])  # 全局隐式等待 config['timeout'] seconds


#####################################################
# read arguments
parser = argparse.ArgumentParser(description='Mark maps')
parser.add_argument('--map', type=str, default='amap',
                    help='Mark on which map? default: amap; optional: amap (高德地图), bmap (百度地图), tmap (腾讯地图)')
parser.add_argument('--info', type=str, default='store-231118-2',
                    help='Identifier of the business info for locating file name and album name (e.g. store-231118-2).')
args = parser.parse_args()

#####################################################
# set business info
with open('../data/{}.json'.format(args.info)) as f:
    info = BusinessInfo(**json.load(f))

console.print('Marking business info:')
console.print(asdict(info))


#####################################################
# execute marking routine
if args.map == 'amap':
    console.print('Marking on Amap (高德地图) ...')
    mark_amap(d, info)
elif args.map == 'bmap':
    console.print('Marking on Bmap (百度地图) ...')
    mark_bmap(d, info)
elif args.map == 'tmap':
    console.print('Marking on Tmap (腾讯地图) ...')
    mark_tmap(d, info)
else:
    raise ValueError(f'[red]Error:[/red] unknown map: {args.map}')
