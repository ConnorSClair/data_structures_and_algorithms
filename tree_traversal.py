from enum import Enum
from typing import Dict, List

class Traversal_Type(Enum):
    IN_ORDER = 0,
    POST_ORDER = 1,
    PRE_ORDER = 2



def traverse(node: str,graph: Dict,type: Traversal_Type) -> None:
    print("TREE")
    if type == Traversal_Type.PRE_ORDER:
        pre_order(node,graph)
    elif type == Traversal_Type.POST_ORDER:
        post_order(node,graph)
    else:
        in_order(node,graph)
    print("\n")

def pre_order(node, graph):
    print(node)
    for c in graph[node]:
        pre_order(c,graph)

def post_order(node, graph):
    for c in graph[node]:
        post_order(c,graph)
    print(node)
    
def in_order(node, graph):
    if len(graph[node]) == 0:
        print(node)
        return
    in_order(graph[node][0],graph)
    print(node)
    if len(graph[node]) == 2:
        in_order(graph[node][1],graph)
        
    

