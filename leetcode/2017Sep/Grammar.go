package main
import  (
  "fmt"
  "container/list"
  "math"
)
var a = 1
func main() {
    //print ops
    fmt.Println("Hello World!")
    fmt.Println("a value is %d",a)
    fmt.Println(a)
    //list ops
    l := list.New()
    for i := 0; i < 5; i++ {
		      l.PushBack(i)
	  }
    for e := l.Front(); e != nil; e = e.Next() {
		      fmt.Println(e.Value) //输出list的值,01234
	  }
    fmt.Println("math.Ceil of 4.5 %d",math.Ceil(4.5))
    fmt.Println("math.Floor of 4.5 %d",math.Floor(4.5))
}
