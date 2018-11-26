"""Akash Gajjar - 201501212@daiict.ac.in"""

from utils import *
from node import Node


def merkle_proof(tx, merkle_tree):
    proof = []
    node = merkle_tree._root
    i = merkle_tree.leaves.index(tx)
    low = 0
    high = len(merkle_tree.leaves)
    while high - low > 1:
        mid = (low + high) // 2
        if i < mid:
            proof.append(Node("r", node._right.data if type(node._right) != str else node._right))
            node = node._left
            high =  mid
        else:
            proof.append(Node("l", node._left.data if type(node._left) != str else node._left))
            node = node._right
            low = mid
    return proof

def verify_proof(tx, merkle_proof):
    proof = [tx] + merkle_proof[::-1]
    while len(proof) > 1:
        if proof[1].direction == 'l':
            proof.insert(0, hash_data(proof.pop(1).tx + proof.pop(0)))
        else:
            proof.insert(0, hash_data(proof.pop(0) + proof.pop(0).tx))
    return proof[0]