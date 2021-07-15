import argparse

parser = argparse.ArgumentParser()
parser.add_argument("k", type = int)
args   = parser.parse_args()
nodes       = {}
train_edges = []
test_edges  = []
with open("human_train.tsv", "r") as ht:
    for line in ht:
        p, q, w = line.strip().split()
        for m in [p, q]:
            if m not in nodes:
                nodes[m] = 0
            nodes[m]    += 1
        train_edges.append((p, q, w))

nodelist = [(key, nodes[key]) for key in nodes]
nodelist = sorted(nodelist, key = lambda x:x[1], reverse = True)[: args.k]
nodelist = [k for k,v in nodelist]

with open(f"human_list_{args.k}.nd", "w") as ls:
    for nd in nodelist:
        ls.write(f"{nd}\n")

nodeset = set(nodelist)
with open("human_test.tsv", "r") as ht:
    for line in ht:
        p, q, w = line.strip().split()
        test_edges.append((p, q, w))

train_edges = [(p, q, w) for (p, q, w)
               in train_edges if
               (p in nodeset and q in nodeset)]

test_edges  = [(p, q, w) for (p, q, w)
               in test_edges if
               (p in nodeset and q in nodeset)]

with open(f"human_train-{args.k}.tsv", "w") as htk:
    for p, q, w in train_edges:
        htk.write(f"{p}\t{q}\t{w}\n")

with open(f"human_test-{args.k}.tsv", "w") as htk:
    for p, q, w in test_edges:
        htk.write(f"{p}\t{q}\t{w}\n")
