from PIL import Image
import glob
import shutil
import os

source = "/Users/student-00-740cdfece5d3/images"
destination = "/Users/student-00-740cdfece5d3/opt/icons"

for file in glob.glob("ic_*"):
    f = os.path.join(source, destination)
    print(f)
    im = Image.open(file)
    im_rbg = im.convert('RGB')
    im_rotate = im.rotate(270)
    im_size = im.resize(128, 128)
    im_name = file + ".jpg"
    new_file = "opt/icons" + file
    im.save(new_file, 'JPEG', quality=80)
