package main

import "fmt"

func merge(l1, l2 []int) []int {
	var newArray []int

	for (len(l1) > 0) && (len(l2) > 0) {
		if l1[0] > l2[0] {
			newArray = append(newArray, l2[0])
			l2 = l2[1:]
		} else {
			newArray = append(newArray, l1[0])
			l1 = l1[1:]
		}
	}

	for len(l1) > 0 {
		newArray = append(newArray, l1[0])
		l1 = l1[1:]
	}

	for len(l2) > 0 {
		newArray = append(newArray, l2[0])
		l2 = l2[1:]
	}

	return newArray
}

func mergeSort(array []int) []int {
	length := len(array)
	if length == 1 {
		return array
	}
	l1 := array[0 : length/2]
	l2 := array[length/2:]

	l1 = mergeSort(l1)
	l2 = mergeSort(l2)

	return merge(l1, l2)
}

func main() {
	a := []int{2, 6, 4, 7, 3, 1, 5}
	x := mergeSort(a[0:])
	fmt.Printf("Final Answer: %v", x)
}
