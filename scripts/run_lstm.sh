mkdir -p checkpoints
CUDA_VISIBLE_DEVICES=0 fairseq-train /data/ds001980/comp-bin \
    --lr 0.0001 --clip-norm 0.1 --max-tokens 4000 \
    --arch lstm_wiseman_iwslt_de_en --no-epoch-checkpoints --save-dir lcheck
