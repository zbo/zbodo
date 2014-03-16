using System;
using System.Collections.Generic;
using System.Text;

namespace ACM
{
    public class HanoiTower
    {
        private int count = 0;
        public void Run()
        {
            Console.WriteLine("Begin");
            HanNoi(5, 'A', 'B', 'C');
            Console.WriteLine("total steps are: {0}",count);
            Console.ReadLine();
        }

        private void HanNoi(int n, char from, char mid, char to)
        {
            if (n == 1)
            {
                Move(from, to);
            }
            else
            {
                HanNoi(n - 1, from, to, mid);
                Move(from, to);
                HanNoi(n - 1, mid, from, to);
            }
        }

        private void Move(char from, char to)
        {
            count++;
            Console.WriteLine(from + " -> " + to);
        }
    }
}
