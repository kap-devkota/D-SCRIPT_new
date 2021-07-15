nodes = set()
with open("human_500.fasta", "r") as ifl:
    for line in ifl:
        if line.startswith(">"):
            nodes.add(line[1:].strip())

train_samples = []
test_samples = []
with open("human_train.tsv", "r") as of:
    for line in of:
        p, q, w = line.strip().split()
        if p in nodes and q in nodes:
            train_samples.append((p, q, w))
with open("human_test.tsv", "r") as of:
    for line in of:
        p, q, w = line.strip().split()
        if p in nodes and q in nodes:
            test_samples.append((p, q, w))
          
            
t_str  = ""
with open("human_500_train.tsv", "w") as of:
    for p, q, w in train_samples:
        t_str += f"{p}\t{q}\t{w}\n"
    of.write(t_str)


t_str  = ""
with open("human_500_test.tsv", "w") as of:
    for p, q, w in test_samples:
        t_str += f"{p}\t{q}\t{w}\n"
    of.write(t_str)
