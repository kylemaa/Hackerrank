#!/usr/bin/env python3

import os
import glob
from PIL import Image

size = 128, 128

for file in glob.glob("ic_*"):
    im = Image.open(file).convert('RGB')
    im.rotate(270).resize((size)).save("/opt/icons/" + file, "JPEG")
