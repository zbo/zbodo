
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
)

func main() {
	//fmt.Println(convert("PAYPALISHIRING",3))
	fmt.Println(convert("A",1))
}

func append(s string, a string) string {
	return s+a
}

func convert(s string, numRows int) string {
	if numRows == 1{
		return s
	}
	var result = ""
	fmt.Println(s)
	len := len([]rune(s))
	for i:=0; i < numRows; i++ {
		if i==0 || i==numRows-1{
			for j:=i; j<len; j=j+2*(numRows)-2{
				//fmt.Print(string(s[j]))
				result = append(result, string(s[j]))
			}
		}else {
			mark := -1
			gap := 2 * (numRows - i)
			k := i
			for k < len {
				//fmt.Print(string(s[k]))
				result = append(result, string(s[k]))

				if mark == 1 {
					gap = 2 * i
				} else {
					gap = 2 * (numRows -1 - i)
				}
				mark = mark * (-1)
				k = k + gap
			}
		}
	}
	return result
}
