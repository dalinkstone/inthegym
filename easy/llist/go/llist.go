package main

import (
	"fmt"
)

type ListNode struct {
	val int
	next *ListNode
}

func CreateList() *ListNode {
	head := &ListNode{val: 0}
	current := head

	for i := 1; i <= 3; i++ {
		current.next = &ListNode{val : i}
		current = current.next
	}

	return head
}

func ReverseList(head *ListNode) []*ListNode {

	var prev *ListNode
	current := head

	for current != nil {
		temp := current.next
		current.next = prev
		prev = current
		current = temp
	}

	var result []*ListNode
	iterator := prev

	for iterator != nil {
		result = append(result, iterator)
		iterator = iterator.next
	}

	return result

}

func main() {

	listNode := CreateList()

	result := ReverseList(listNode)

	fmt.Println("This is the reverse a singly linked list, the list is [0, 1, 2, 3]")
	fmt.Println("This should return [3, 2, 1, 0]")

	fmt.Print("Actual Result: [")

	for i, node := range result {
		fmt.Print(node.val)
		if i < len(result)-1 {
			fmt.Print("")
		}
	}

	fmt.Println("]")

}
