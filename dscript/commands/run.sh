#!/bin/bash

SBATCH_OPTS="\
--mem=128GB
--mail-type=END --mail-user=Kapil.Devkota@tufts.edu \
--time=0-20:00:00 \
"

source activate dscript
sbatch $SBATCH_OPTS -o ./output_first.log ./train.py --train=human_train-500.tsv --val=human_test-500.tsv --embedding=human.h5 --num-epochs=2
