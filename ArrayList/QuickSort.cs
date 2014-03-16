using System;
using System.Collections.Generic;
using System.Text;

namespace ACM
{
    public class QuickSort
    {
        private readonly int[] buffer = { 5, 21, 6, 8, 9, 32, 13, 12, 41, 2, 3, 4 };
        public void Run()
        {
            QS(buffer, 0, buffer.Length - 1);
            this.PrintAll();
        }
        private void QS(int[] numbers, int left, int right)
        {
            if (left < right)
            {
                int middle = (left + right) / 2;
                int leftSentry = left;
                int rightSentry = right;
                while (leftSentry < middle || rightSentry > middle)
                {
                    leftSentry = left;
                    rightSentry = right;
                    leftSentry = FindBigNumberFromLeft(leftSentry, middle);
                    rightSentry = FindSmallNumberFromRight(rightSentry, middle);
                    if(leftSentry!=rightSentry)
                        Swap(buffer, leftSentry, rightSentry);
                }
                QS(buffer,left, middle);
                QS(buffer, middle+1, right);

            }
        }

        private int FindSmallNumberFromRight(int rightSentry, int middle)
        {
            while (rightSentry > middle)
            {
                if (buffer[rightSentry] < buffer[middle])
                    break;
                rightSentry--;
            }
            return rightSentry;
        }

        private int FindBigNumberFromLeft(int leftSentry,int middle)
        {
            while (leftSentry < middle)
            {
                if (buffer[leftSentry] > buffer[middle])
                    break;
                leftSentry++;
            }
            return leftSentry;
        }
        private void PrintAll()
        {
            for (int i = 0; i < buffer.Length; i++)
            {
                Console.Write(buffer[i] + ", ");
            }
        }
        private static void Swap(int[] numbers, int i, int j)
        {
            int number = numbers[i];
            numbers[i] = numbers[j];
            numbers[j] = number;
        }
    }
}
