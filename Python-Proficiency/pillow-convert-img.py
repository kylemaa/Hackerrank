#!/usr/bin/python3
from PIL import Image
import glob
import os
import sys
import shutil

for file in glob.glob("ic_*"):
    im = Image.open(file)
    im.convert("RGB").rotate(-90).resize((128,
                                          128)).save("$HOME/opt/icons" + file, "JPEG")
