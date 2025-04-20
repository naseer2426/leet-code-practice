package main
import (
    "fmt"
    "strconv"
)

func isPalindrome(x int) bool {
    s := strconv.Itoa(x)
    r := reverseStr(s)
    fmt.Println(r)
    return s == r
}

func reverseStr(s string) string {
    r := ""
    for i := len(s)-1; i>=0; i-- {
        r+=string(s[i])
    }
    return r
}

func main() {
    fmt.Println(isPalindrome(123))
}
