#!/usr/bin/env python
# coding: utf-8

import typer
import os
import sys
import subprocess

neutu_path = os.environ['NEUTU_PATH']
if neutu_path is None:
    print('The path to neutu must be set in env var NEUTU_PATH!')
    sys.exit(1)

neutu_exe = os.path.join(neutu_path, 'neutu')

def skeletonize(idfile, server, uuid, instance: str):
    with open(idfile) as f:
        for line in f:
            bodyid = int(line)
            cmd = f'{neutu_exe} --command --skeletonize --bodyid {bodyid} "{server}?uuid={uuid}&segmentation={instance}"'
            subprocess.run(cmd.split())
            sys.exit(0)

if __name__ == '__main__':
    typer.run(skeletonize)