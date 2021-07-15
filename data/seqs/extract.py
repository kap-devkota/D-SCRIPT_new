import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")
args   = parser.parse_args()

nodes  = set()
with open(args.file, "r") as of:
    for line in of:
        nodes.add(line.strip())

NAME   = True
ADD    = False
seqmap = {}
with open("human.fasta", "r") as ifl:
    for line in ifl:
        if NAME == True:
            name = line.strip()[1: ]
            if name in nodes:
                ADD = True
            else:
                ADD = False
            NAME = False
        else:
            NAME = True
            if ADD:
                seqmap[name] = line.strip()

with open("human_500.fasta", "w") as of:
    for key in seqmap:
        of.write(f">{key}\n")
        of.write(f"{seqmap[key]}\n")
