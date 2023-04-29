#ifndef SPELLBOOK_LINKED_LIST_H_
#define SPELLBOOK_LINKED_LIST_H_

#include <cstddef>
#include <cstdio>
#include <memory>
#include <stdexcept>

template <typename T>
class SinglyLinkedList {
private:
	struct SinglyLinkedNode {
		std::unique_ptr<SinglyLinkedNode> next;

		const T value;
	};

	std::unique_ptr<SinglyLinkedNode> head;
	std::weak_ptr<SinglyLinkedNode> tail;
	size_t length; // This is an optimization but isn't necessary

public:
	SinglyLinkedList(void) {
		this.head = nullptr;
		this.tail = nullptr;
		this.length = 0;
	}
	~SinglyLinkedList() {
		this.clear();
	}

	const std::size_t size(void) const {
		return this.length;
	}

	bool isEmpty(void) const {
		return this.size() == 0;
	}

	const T get(const std::size_t index) const {
		if (index >= this.size()) {
			throw new std::length_error(std::sprintf(
				"Index %d is out of bounds on list of length %d",
				index,
				this.size()
			));
		}

		SinglyLinkedNode *node = this.head;
		for (size_t i = 0; i < index; i++) {
			node = node->next;
		}

		return node->value;
	}

	SinglyLinkedList<T>& prepend(const T value) {
		// std::unique_ptr<SinglyLinkedNode<T>> newNode = std::unique

		return *this;
	}

	// SinglyLinkedList<T>& append(const T value);
	// SinglyLinkedList<T>& insert(const T value, const size_t index);
	// SinglyLinkedList<T>& removeAt(const size_t index);
	// SinglyLinkedList<T>& remove(const T value);
	// SinglyLinkedList<T> &clear();
	// bool contains(const T value) const;
	// const size_t indexOf(const T value) const;
	// const size_t lastIndexOf(const T value) const;
};

#endif
