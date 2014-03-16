using System;
using System.Collections.Generic;
using System.Text;

namespace ACM
{
    public class HeapSort3
    {
        private readonly int[] buffer = { 5, 21, 6, 8, 9, 32, 13, 12, 41, 2, 3, 4, 1 };
        public void Run()
        {
            HeapSort();
            this.PrintAll();
        }

        private void HeapSort()
        {
            int start = 0;
            int end = buffer.Length - 1;
            InitialHeap(buffer, start, end);
            while (start < end)
            {
                Swap(buffer, start, end);//make the array from start to end as big root heap
                end--;
                AdjustHeap(buffer, start, end);
                //InitialHeap(buffer, start, end);
            }
        }

        private void AdjustHeap(int[] buffer, int start, int end)
        {
            int currentPos = start;
            int switchPos = GetSwitchPos(currentPos, end);
            while (switchPos != currentPos)
            {
                Swap(buffer, currentPos, switchPos);
                currentPos = switchPos;
                switchPos = GetSwitchPos(currentPos, end);
            }
        }

        private int GetSwitchPos(int currentPos, int end)
        {
            int leftPos = currentPos * 2 + 1;
            int rightPos = currentPos * 2 + 2;
            if (rightPos <= end)
            {
                if (buffer[rightPos] <= buffer[currentPos] && buffer[leftPos] <= buffer[currentPos])
                    return currentPos;
                else if (buffer[leftPos] > buffer[rightPos])
                    return leftPos;
                else
                    return rightPos;
            }
            else if (leftPos <= end)
            {
                if (buffer[leftPos] > buffer[currentPos])
                    return leftPos;
                else
                    return currentPos;
            }
            else
            {
                return currentPos;
            }
        }
        private void InitialHeap(int[] buffer, int start, int end)
        {
            int currentPos;
            int parantPos;
            bool lastTime;
            for (int i = start; i <= end; i++)
            {
                currentPos = i;
                parantPos = (currentPos - 1) / 2;
                lastTime = false;
                while (parantPos >= start)
                {
                    if (buffer[currentPos] > buffer[parantPos])
                        Swap(buffer, currentPos, parantPos);
                    currentPos = parantPos;
                    parantPos = (currentPos - 1) / 2;
                    if (lastTime == true)
                        break;
                    if (parantPos == start)
                    { lastTime = true; }
                } 
            }
        }

        private void InitialHeap2(int[] buffer, int start, int end)
        {
            int currentPos = end;
            int parantPos = (currentPos - 1) / 2;
            while (parantPos >= start)
            {
                if (buffer[currentPos] > buffer[parantPos])
                    AdjustHeap(buffer, parantPos, end);
                currentPos--;
                parantPos = (currentPos - 1) / 2;
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
