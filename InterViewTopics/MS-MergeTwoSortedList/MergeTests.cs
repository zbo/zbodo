using System;
using NUnit.Framework;

namespace Merge
{
    [TestFixture]
    internal class MergeTests
    {
        private void PrintList(Node head)
        {
            if (head == null)
                Console.WriteLine("the list is null");
            else
            {
                while (head != null)
                {
                    Console.WriteLine(head.data);
                    head = head.next;
                }
            }
        }

        private Node BuildList(int[] array)
        {
            if (array == null)
                return null;
            if (array.Length == 0)
                return null;
            Node head = new Node();
            head.data = array[0];
            int currentIndex = 1;
            Node currentNode = head;
            while (currentIndex < array.Length)
            {
                Node nextNode = new Node();
                nextNode.data = array[currentIndex];
                currentNode.next = nextNode;
                currentNode = nextNode;
                currentIndex++;
            }
            return head;
        }

        [Test]
        public void MergeTwoListsTest()
        {
            int[] array1 = {5, 6, 7, 8, 9, 32, 130, 132, 132, 134, 300};
            int[] array2 = {-5, -1, 6, 7, 10, 33, 130, 130, 132, 133, 301,340};
            Node head1 = BuildList(array1);
            Node head2 = BuildList(array2);
            MergeClass instance = new MergeClass();
            Node result = instance.Merge(head1, head2);
            PrintList(result);
        }
        [Test]
        public void MergeTwoListsWithNullTest()
        {
            int[] array1 = {1, 2, 3, 4, 5, 6};
            int[] array2 = null;
            Node head1 = BuildList(array1);
            Node head2 = BuildList(array2);
            MergeClass instance = new MergeClass();
            Node result = instance.Merge(head1, head2);
            PrintList(result);
        }

    }
}