#!/bin/sh
# Copyright 2023 - 2023, Niels Moseley and the pyrigremote contributors
# SPDX-License-Identifier: GPL-3.0-only

./compile_resources.sh
./update_version.py
rm -rf dist
python3 -m build
