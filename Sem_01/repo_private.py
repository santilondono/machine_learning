# Token for working on github (replace yours here given are placeholder)

import os

dir = '/content/drive/MyDrive/machine_learning/repo_keys'

print(os.path.dirname(os.path.realpath(dir)))
this_dir = os.path.dirname(os.path.realpath(dir))

GIT_KEY=""

with open(this_dir + "/repo_keys.txt") as f:
	for line in f:
		tups=line.strip().split("=")
		if tups[0] == "GIT_KEY":
			GIT_KEY=tups[1]
