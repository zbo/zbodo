using System;
using System.Collections.Generic;
using System.Text;

namespace Code
{
    public class MergeSort
    {
        private readonly int[] buffer = { 5, 21, 6, 8, 9, 32, 13, 12, 41, 2, 3, 4, 1 };
        public void Run()
        {
            int range = 1;
            while (range < buffer.Length)
            {
                MergeSortRange(buffer, range);
                range = range * 2;
            }
            this.PrintAll();
        }

        private void MergeSortRange(int[] buffer, int range)
        {
            for (int startPos = 0; startPos < this.buffer.Length; startPos = startPos + range * 2)
            {
                int start1 = startPos;
                int start2 = startPos + range;
                if (start2 < buffer.Length)
                    MergeTwo(start1, start2, range);
            }
        }

        private void MergeTwo(int start1, int start2, int range)
        {
            int endofpart1 = start2 - 1;
            int endofpart2 = start2 + range - 1;
            if (endofpart2 >= buffer.Length)
                endofpart2 = buffer.Length - 1;
            while (start1 <= endofpart1)
            {
                if (buffer[start1] > buffer[start2])
                {
                    Swap(buffer, start1, start2);
                    AdjustPart2(buffer, start2, endofpart2);
                }
                start1++;
            }
        }

        private void AdjustPart2(int[] buffer, int start2, int endofpart2)
        {
            for (int i = start2; i < endofpart2; i++)
            {
                if (buffer[i] > buffer[i + 1])
                { Swap(buffer, i, i + 1); }
            }
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
