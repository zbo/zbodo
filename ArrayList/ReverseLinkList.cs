using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Code
{
    public class ReverseLinkList
    {
        private readonly int[] buffer = { 5, 21, 6, 8, 9, 32, 13, 12, 41, 2, 3, 4, 1 };  
        public void Run()
        {
            Console.WriteLine("Begin");
            LinkedListNode root = InitialLinkedList();
            PrintLinkedList(root);
            LinkedListNode newRoot= ReverseLinkListByOnceLoop(root);
            Console.WriteLine();
            PrintLinkedList(newRoot);
            Console.ReadLine();
        }

        private LinkedListNode ReverseLinkListByOnceLoop(LinkedListNode root)
        {
            LinkedListNode currentNode = root;
            LinkedListNode next1 = currentNode.Next;
            LinkedListNode next2 = next1.Next;
            root.Next = null;
            while (next2!= null)
            {
                next1.Next = currentNode;
                currentNode = next1;
                next1 = next2;
                next2 = next2.Next;
            }
            next1.Next = currentNode;
            return next1;
        }

        private void PrintLinkedList(LinkedListNode root)
        {
            LinkedListNode currentNode=root;
            do
            {
                Console.Write(currentNode.Value+" ");
                currentNode = currentNode.Next;
            }
            while (currentNode != null);
        }

        private LinkedListNode InitialLinkedList()
        {
            LinkedListNode root = new LinkedListNode();
            root.Value = buffer[0];
            int index = 1;
            LinkedListNode currentNode = root;
            while (index < buffer.Length)
            {
                LinkedListNode node = new LinkedListNode();
                node.Value = buffer[index];
                currentNode.Next = node;
                currentNode = node;
                index++;
            }
            return root;
        }
    }
    public class LinkedListNode
    {
        public int Value { get; set; }
        public LinkedListNode Next{get;set;}
    }
}
