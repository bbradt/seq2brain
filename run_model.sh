mkdir -p checkpoints
CUDA_VISIBLE_DEVICES=0 fairseq-train /data/ds001980/comp-bin \
    --lr 0.25 --clip-norm 0.1 --max-tokens 4000 \
    --arch fe --save-dir checkpoints