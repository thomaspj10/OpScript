package main

import "fmt"

func pop(alist *[]int) int {
	f := len(*alist)
	rv := (*alist)[f-1]
	*alist = (*alist)[:f-1]
	return rv
}

func main() {
	stack := []int{}
	_ = stack
	a := 0
	_ = a
	b := 0
	_ = b

	//[generated_code]
}

func _() {
	fmt.Println()
}
