using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Code
{
    public class CellphoneKeyboard
    {
        private readonly char[][] CharArray=new char[10][];
        private readonly string NumberString = "453";
        public void Run()
        {
            InitialArray();
            var NumberStringArray = this.NumberString.ToCharArray();
            List<string> possibleOutPut = new List<string>();
            possibleOutPut.Add("");
            List<string> allPossibleOutPut = GetPossibleOutPut(possibleOutPut, NumberStringArray);
            PrintAllPossibleOutPut(allPossibleOutPut);
            Console.WriteLine("got tooal possibles {0}",allPossibleOutPut.Count);
            
        }

        private void PrintAllPossibleOutPut(List<string> allPossibleOutPut)
        {
            foreach (var str in allPossibleOutPut)
            {
                Console.WriteLine(str);
            }

        }

        private List<string> GetPossibleOutPut(List<string> tillNowAllPossibleOutPut, char[] LeftNumbers)
        {
            if (LeftNumbers.Length > 0)
            {
                List<string> allPossibleOutPut = new List<string>();
                char nextChar = LeftNumbers[0];
                int nextInt = int.Parse(nextChar.ToString());
                var allchars = this.CharArray[nextInt].ToArray();
                foreach (var str in tillNowAllPossibleOutPut)
                {
                    foreach (char ch in allchars)
                    {
                        allPossibleOutPut.Add(str + ch);
                    }
                }
                LeftNumbers = new string(LeftNumbers).Substring(1).ToCharArray();
                return GetPossibleOutPut(allPossibleOutPut, LeftNumbers);
            }
            else
            {
                return tillNowAllPossibleOutPut;
            }
        }

        private void InitialArray()
        {
            this.CharArray[0] = "".ToCharArray();
            this.CharArray[1] = "".ToCharArray();
            this.CharArray[2] = "ABC".ToCharArray();
            this.CharArray[3] = "DEF".ToCharArray();
            this.CharArray[4] = "GHI".ToCharArray();
            this.CharArray[5] = "JKL".ToCharArray();
            this.CharArray[6] = "MNO".ToCharArray();
            this.CharArray[7] = "PQRS".ToCharArray(); 
            this.CharArray[8] = "TUV".ToCharArray();
            this.CharArray[9] = "WXYZ".ToCharArray();
        }
    }
}
