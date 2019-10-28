import torch
import torch.nn as nn
import fairseq
from fairseq.modules.transformer_layer import TransformerDecoderLayer
from fairseq.models import register_model_architecture
import argparse
from fairseq.models import register_model

NUM_FEATUERS = 1068 
NUM_TC = 30
DECODER_EMBED_DIM = 1068 
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--decoder_embed_dim', default=DATASET, help='old foo help')
parser.add_argument('--decoder_attention_heads', default=4, help='old foo help')
parser.add_argument('--attention_dropout', default=0.0, help='old foo help')
parser.add_argument('--dropout',default=0.0)
parser.add_argument('--decoder_normalize_before',default=True)
args = parser.parse_args()

# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'transformer.wmt16.en-de', ... ]

# Load a transformer trained on WMT'16 En-De
en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt16.en-de', tokenizer='moses', bpe='subword_nmt')

new_output_layer = TransformerDecoderLayer(args)
@register_model('NeuroSeq')
class NeuroSeq(nn.Module):
    def __init__(self, args):

        self.pretrained = en2de
        self.output_layer =  new_output_layer
    def forward(x, **kwargs):
        x, _ = self.pretrained.forward(x)
        x, attn = self.output_layer(x)
        return x, attn
    @classmethod
    def build_model(cls, args, task):
        return PretrainedModel(args)

@register_model_architecture('NeuroSeq', 'run_neuroseq')
def run_neuroseq(args):
    # We use ``getattr()`` to prioritize arguments that are explicitly given
    # on the command-line, so that the defaults defined below are only used
    # when no other value has been specified.
