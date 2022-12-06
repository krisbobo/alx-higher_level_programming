#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ''):
        tuple_res = (len(sentence), None)
    else:
        tuple_res = (len(sentence), sentence[0])
    return (tuple_res)
