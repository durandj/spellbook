---
title: "Linked List"
weight: 2
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Linked List

## Summary

Linked lists are one of the simplest of the unordered collection data
structures. At it's core, a linked list is very similar to a chain.
When you wish to add something to the list you add a new link to the
chain. So with a list of length `10` you would have `10` links in the
chain.

{{<mermaid>}}
stateDiagram-v2
    direction LR

    [*] --> node1
    node1 --> node2
    node2 --> [*]
{{</mermaid>}}

### Operations

#### Insertion

This simple structure makes it really easy to do insertions anywhere
in the list by just adding a new item where needed and updating all
references that point to the previous or next element in the chain.

{{<mermaid>}}
stateDiagram-v2
    direction LR

    [*] --> node1
    node1 --> newNode

    state newNode {
        node1.5
    }

    newNode --> node2
    node2 --> [*]
{{</mermaid>}}

#### Deletion

Removing a node from the list is also relatively straightforward. You
search for the target node, and then update the links to that node so
that they point around the node instead.

{{<mermaid>}}
stateDiagram-v2
    direction LR

    [*] --> node1
    node1 --> node2

    node1.5

    node2 --> [*]
{{</mermaid>}}

Because of how this works, deletion is the same for any node in the
list.

#### Retrieval

Retrieving data from the linked list is where things get messy. You
can't just jump to an arbitrary element in the list anymore, you must
traverse the list one element at a time until you get to your desired
position.

So say you have a list of `5` elements and you wanted to get the value
at the `4th` position. You would start at the `1st` element and then
traverse across each of the linked nodes until you get to the `4th`
position.

The bigger the list is the more expensive this can be.

## Variations

Linked lists can be implemented in two different ways:

* Singly linked list
* Doubly linked list

### Singly linked list

We've touched briefly on how a linked list is like a chain and that
each link in the chain has a connection between it and the link that
came before it and the one that comes after it.

In a singly linked list, when you represent a each link in the chain
as an object it'll have some reference _only_ to the following node.
In other words, a singly linked list points only in a single
direction and you can only traverse forward in the list.

This reduces the memory footprint of the data structure since you're
storing less metadata per element but you must always traverse the
entire list if you wanted to get the last element. You could make a
small optimization by storing the last element and the first element
but that wouldn't help if you wanted the second to last element.

#### Implementations

{{<expand summary="Python">}}
{{% include-code file="/snippets/compsci/data-structures/linked-list/singly-linked-list.py" language="python" %}}
{{</expand>}}

{{<expand summary="Typescript">}}
{{% include-code file="/snippets/compsci/data-structures/linked-list/singly-linked-list.ts" language="typescript" %}}
{{</expand>}}

{{<expand summary="Golang">}}
{{% include-code file="/snippets/compsci/data-structures/linked-list/singly-linked-list.go" language="golang" %}}
{{</expand>}}

{{<expand summary="C++">}}
{{% include-code file="/snippets/compsci/data-structures/linked-list/singly-linked-list.hpp" language="c++" %}}
{{</expand>}}

{{<expand summary="C">}}
{{% include-code file="/snippets/compsci/data-structures/linked-list/singly-linked-list.h" language="c" %}}
{{</expand>}}

{{<expand summary="Java">}}
{{% include-code file="/snippets/compsci/data-structures/linked-list/singly-linked-list.java" language="java" %}}
{{</expand>}}

### Doubly linked list

Another, slightly more useful, version of the linked list is the
doubly linked list. It's basically the same as the singly linked list
except that each element in the list keeps track of the element just
before _and_ after it. This means you can traverse the list forwards
and backwards. This allows for some useful optimizations.

For example, when going to an index in the list, you can start at the
end _or_ the beginning of the list depending on what is closer to the
index you're interested in.

The downside to the doubly linked list is that there's some extra
overhead involved with maintaining the extra connections going back
up the list.

## Performance

## Related

Trees

{{< mermaid >}}
stateDiagram-v2
    direction TB

    [*] --> node1
    node1 --> node2
    node2 --> [*]
{{< /mermaid >}}

Queues
Stacks
