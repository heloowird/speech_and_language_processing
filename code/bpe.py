#!/usr/bin/env python
#coding:utf-8
#reference:https://www.aclweb.org/anthology/P16-1162.pdf
#author:zhujianqi

from __future__ import print_function

import sys
import collections


def stat_pair(vocab):
    pair_cnt = collections.defaultdict(int)
    for char_seq, cnt in vocab.items():
        chars = char_seq.split(' ')
        for i in range(0, len(chars)-1):
            pair_cnt[(chars[i], chars[i+1])] += cnt
    return pair_cnt


def merge_pair(pair, v_in):
    v_out = {}
    for word in v_in:
        w_out = word.replace(' '.join(pair), ''.join(pair))
        v_out[w_out] = v_in[word]
    return v_out


def bpe(vocab, num_merges=10):
    pair_list = []
    for i in range(num_merges):
        pairs = stat_pair(vocab)
        best = max(pairs, key=pairs.get)
        pair_list.append(best)
        vocab = merge_pair(best, vocab)
    return pair_list, vocab


def test():
    vocab = {'l o w </w>' : 5, 'l o w e s t </w>' : 2, 'n e w e r </w>' : 6, 'w i d e r </w>' : 3, 'n e w </w>' : 2}
    num_merges = 8
    pair_list, vocab = bpe(vocab, 8)
    print(pair_list)
    print(vocab)

if __name__ == "__main__":
    test()

