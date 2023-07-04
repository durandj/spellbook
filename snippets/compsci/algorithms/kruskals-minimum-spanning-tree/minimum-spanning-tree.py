Node = int
EdgeWeight = int | float
Edge = tuple[Node, Node, EdgeWeight]
ConnectedGraphEdgeList = list[Edge]
MinimumSpanningTreeEdgeList = list[Edge]

def find_minimum_spanning_tree(
        graph: ConnectedGraphEdgeList,
) -> MinimumSpanningTreeEdgeList:
    mst: MinimumSpanningTreeEdgeList = []

    sorted_edge_list = sorted(graph, key=lambda edge: edge[2])
    node_parents: dict[Node, Node] = {
        node: node
        for node in set(edge[0] for edge in sorted_edge_list) | set(edge[1] for edge in sorted_edge_list)
    }
    for edge in sorted_edge_list:
        (start, end, _weight) = edge

        start_parent = _get_root_node(node_parents, start)
        end_parent = _get_root_node(node_parents, end)

        # if nodes share a parent then there would be a cycle
        if start_parent == end_parent:
            continue

        mst.append(edge)

        node_parents[end_parent] = start_parent

    return mst


def _get_root_node(
        node_parents: dict[Node, Node],
        node: Node,
) -> Node:
    parent = node_parents[node]
    if parent == node:
        return parent

    return _get_root_node(node_parents, parent)


if __name__ == "__main__":
    graph: ConnectedGraphEdgeList = [
        (0, 1, 7),
        (1, 2, 8),
        (0, 3, 5),
        (1, 3, 9),
        (1, 4, 7),
        (2, 4, 5),
        (3, 4, 15),
        (3, 5, 6),
        (4, 5, 8),
        (4, 6, 9),
        (5, 6, 11),
    ]

    mst = find_minimum_spanning_tree(graph)
    expected_mst = [(0, 3, 5), (2, 4, 5), (3, 5, 6), (0, 1, 7), (1, 4, 7), (4, 6, 9)]

    sorted_mst = sorted(mst)
    sorted_expected_mst = sorted(expected_mst)

    print(f"Got:      {mst}")
    print(f"Expected: {expected_mst}")

    assert len(sorted_mst) == len(sorted_expected_mst), "MST did not have correct number of edges"
    for i in range(len(sorted_expected_mst)):
        expected = sorted_expected_mst[i]
        actual = sorted_mst[i]

        assert expected == actual, f"Expected {expected} at index {i} but got {actual}"
