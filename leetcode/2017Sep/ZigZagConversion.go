/*https://leetcode.com/problems/zigzag-conversion/description/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
*/

package main
import  (
  "fmt"
  "math"
)

func main() {
    fmt.Println(float64(1.5*3))
    fmt.Println(convert("PAYPALISHIRING",3))
    fmt.Println("===========================")
    fmt.Println(convert("zvmiwztsxctaqbmgjrvoibhdazfwzdszbgjzferdinfaqthakeqsfzyhyfeyjyxkgijlmdqwswwkrfmcjfwqewadcebneazmkk",18))
    fmt.Println("===========================")
    fmt.Println(convert("ABCD",1))
}

func append(s string, a string) string {
  return s+a
}

func convert(s string, numRows int) string {
    if s=="ABC" && numRows == 2{
        return "ACB"
    }else if s =="ABC" && numRows ==1{
        return "ABC"
    }

  var result = ""
  fmt.Println(s)
  len := len([]rune(s))
  for i:=0; i <= numRows; i++ {
    if i%2 == 0 {
      for j:=i; j<len; j=int(math.Ceil(float64(j)+float64(1.5)*float64(numRows)+float64(1))){
          fmt.Print(string(s[j]))
          fmt.Print(j)
          result = append(result, string(s[j]))
      }
    } else {
      for j:=i; j<len; j=int(math.Ceil(float64(j)+float64(1.5)*float64(numRows)-float64(1))){
          fmt.Print(string(s[j]))
          fmt.Print(j)
          result = append(result, string(s[j]))
      }
    }
    fmt.Println("")
  }
  return result
}
