# coding=utf-8
# Copyright 2021 The I-BERT Authors (Sehoon Kim, Amir Gholami, Zhewei Yao, 
# Michael Mahoney, Kurt Keutzer - UC Berkeley) and The HuggingFace Inc. team.
# Copyright (c) 20121, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ...utils import logging
from ..roberta.tokenization_roberta import RobertaTokenizer


logger = logging.get_logger(__name__)


PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "kssteven/ibert-roberta-base": "https://huggingface.co/roberta-base/resolve/main/vocab.json",
        "kssteven/ibert-roberta-large": "https://huggingface.co/roberta-large/resolve/main/vocab.json",
        "kssteven/ibert-roberta-large-mnli": "https://huggingface.co/roberta-large-mnli/resolve/main/vocab.json",
    },
    "merges_file": {
        "kssteven/ibert-roberta-base": "https://huggingface.co/roberta-base/resolve/main/merges.txt",
        "kssteven/ibert-roberta-large": "https://huggingface.co/roberta-large/resolve/main/merges.txt",
        "kssteven/ibert-roberta-large-mnli": "https://huggingface.co/roberta-large-mnli/resolve/main/merges.txt",
    },
}

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    "kssteven/ibert-roberta-base": 512,
    "kssteven/ibert-roberta-large": 512,
    "kssteven/ibert-roberta-large-mnli": 512,
}

class IBertTokenizer(RobertaTokenizer):
    r"""
    Construct a I-BERT tokenizer.

    :class:`~transformers.IBertTokenizer` is identical to :class:`~transformers.RobertaTokenizer`. Refer to superclass
    :class:`~transformers.RobertaTokenizer` for usage examples and documentation concerning the initialization
    parameters and other methods.
    """
    # merges and vocab same as Roberta
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
