#include <iostream>
using namespace std;

class Node {
public:
	int data;
	Node* next;
};

class LinkedList {
public:
	Node* head;
	Node* tail;
	int theSize;
	LinkedList() {
		head = NULL;
		tail = NULL;
		theSize = 0;
	}
	void add_node(int x) {
		Node* temp = new Node;
		temp->data = x;
		temp->next = NULL;
		if (head == NULL) {
			head = temp;
			tail = temp;
		}
		else {
			tail->next = temp;
			tail = tail->next;
		}
		theSize++;
	}
	void printList()
	{
		Node* temp = head;

		if (head == NULL) {
			cout << "List empty" << endl;
			return;
		}

		while (temp != NULL) {
			cout << temp->data << " ";
			temp = temp->next;
		}
	}
};

LinkedList mergeTwoLists(LinkedList l1, LinkedList l2) {
	LinkedList l3;
	Node* c1 = l1.head;
	Node* c2 = l2.head;
	while(){
		l3.add_node(min(c1->data,c2->data));
		l3.add_node(max(c1->data, c2->data));
		c1 = c1->next;
		c2 = c2->next;
	}
	return l3;
}
void main() {
	LinkedList l1, l2;
	l1.add_node(0);
	l1.add_node(2);
	l1.add_node(3);
	l2.add_node(1);
	l2.add_node(3);
	l2.add_node(4);
	int x = l1.theSize;
	int y = l2.theSize;
	//cout << x << " " << y;
	LinkedList l3 = mergeTwoLists(l1, l2);
	l3.printList();
}