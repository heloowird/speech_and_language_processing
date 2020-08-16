#!/usr/bin/env python
#coding:utf-8
#author:heloowird

from __future__ import print_function
import sys


def forward_max_match(sentence, word_dict, token_list):
    if not sentence:
        return
    
    for i in range(len(sentence)): 
        prefix = sentence[0:len(sentence)-i]
        suffix = sentence[len(sentence)-i:]
        if prefix in word_dict: 
            token_list.append(prefix)
            forward_max_match(suffix, word_dict, token_list)
            return
    
    prefix = sentence[0:1]
    suffix = sentence[1:]
    token_list.append(prefix)
    forward_max_match(suffix, word_dict, token_list)

def test():
    word_dict = {"西湖", "杭州", "特别"}
    sentence = "杭州西湖人很多"
    token_list = []
    forward_max_match(sentence, word_dict, token_list)
    print(sentence)
    print(' | '.join(token_list))

if __name__ == "__main__":
    test()

