# main.py - VectorShift Backend

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PipelinePayload(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]


def is_dag(nodes: list, edges: list) -> bool:
    """
    Check if the graph formed by nodes and edges is a Directed Acyclic Graph.
    Uses DFS-based cycle detection (topological sort approach).
    """
    node_ids = {node["id"] for node in nodes}

    # Build adjacency list
    adj: Dict[str, List[str]] = {nid: [] for nid in node_ids}
    for edge in edges:
        src = edge.get("source")
        tgt = edge.get("target")
        if src in adj and tgt in adj:
            adj[src].append(tgt)

    # DFS cycle detection
    # States: 0 = unvisited, 1 = in current path, 2 = done
    state = {nid: 0 for nid in node_ids}

    def has_cycle(node: str) -> bool:
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1
        for neighbor in adj.get(node, []):
            if has_cycle(neighbor):
                return True
        state[node] = 2
        return False

    for nid in node_ids:
        if state[nid] == 0:
            if has_cycle(nid):
                return False  # Has a cycle → not a DAG

    return True


@app.get("/")
def read_root():
    return {"message": "VectorShift Pipeline API"}


@app.post("/pipelines/parse")
def parse_pipeline(payload: PipelinePayload):
    num_nodes = len(payload.nodes)
    num_edges = len(payload.edges)
    dag = is_dag(payload.nodes, payload.edges)

    return {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "is_dag": dag,
    }
