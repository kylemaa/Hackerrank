First Part
 #!/bin/bash

> oldFiles.txt

files=$(grep " jane " ~/data/list.txt | cut -d' ' -f3 | cut -d'/' -f3)

for i in $files; do
	if test -e ~/data/$i; then
		echo $HOME/data/$i >> oldFiles.txt
	fi
done

Second Part

#!/usr/bin/env python3

import sys
import subprocess

#open version

f = open(sys.argv[1],"r")
for line in f.readlines():
  old_name = line.strip()
  new_name = old_name.replace("jane","jdoe")
  subprocess.run(["mv",old_name,new_name])
f.close()

#with version
with open(sys.argv[1],"r") as files:
    for line in files.readlines():
        old_name = line.strip()
        new_name = old_name.replace("jane","jode")
        subprocess.run(["mv",old_name,new_name])  
    files.close()


