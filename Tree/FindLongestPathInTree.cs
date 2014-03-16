using System;
using System.Collections.Generic;
using System.Text;

namespace ACM
{
    public class FindLongestPathInTree
    {
        public void Run()
        {
            TreeNode root = InitialTree();
            int pathLength = FindMaxPath(root);
            Console.WriteLine(pathLength);
            Console.ReadLine();
        }

        private int FindMaxPath(TreeNode root)
        {
            if (root == null)
                return 0;
            if (root.Left == null && root.Right == null)
                return 0;
            int maxLeft = 0;
            int longestLeftNode = 0;
            int maxRight = 0;
            int longestRightNode = 0;
            if (root.Left != null)
            {
                maxLeft = FindMaxPath(root.Left);
                longestLeftNode = FindLongestNode(root.Left);
            }
            if (root.Right != null)
            {
                maxRight = FindMaxPath(root.Right);
                longestRightNode = FindLongestNode(root.Right);
            }
            return FindMax(maxLeft, maxRight, longestLeftNode + longestRightNode + 2);

        }

        private int FindMax(int maxLeft, int maxRight, int sum)
        {
            if (maxRight > sum && maxRight > maxLeft) return maxRight;
            else if (maxLeft > sum && maxLeft > maxRight) return maxLeft;
            else return sum;
        }

        private int FindLongestNode(TreeNode treeNode)
        {
            if (treeNode == null)
                return 0;
            if (treeNode.Left == null && treeNode.Right == null)
                return 0;
            int left = FindLongestNode(treeNode.Left);
            int right = FindLongestNode(treeNode.Right);
            if (left > right)
                return left+1;
            else
                return right+1;
        }

        private TreeNode InitialTree()
        {
            TreeNode root = new TreeNode(0);
            TreeNode node1 = new TreeNode(1);
            TreeNode node2 = new TreeNode(2);
            TreeNode node3 = new TreeNode(3);
            TreeNode node4 = new TreeNode(4);
            TreeNode node5 = new TreeNode(5);
            TreeNode node6 = new TreeNode(6);
            TreeNode node7 = new TreeNode(7);
            TreeNode node8 = new TreeNode(8);
            TreeNode node9 = new TreeNode(9);
            root.Left = node1;
            root.Right = node2;
            node1.Left = node3;
            node1.Right = node4;
            node3.Left = node6;
            node3.Right = node7;
            node2.Right = node5;
            node5.Left = node8;
            node5.Right = node9;
            return root;
        }
    }
    class TreeNode
    {
        public TreeNode(int value)
        {
            this.Value = value;
        }
        public TreeNode Left;
        public TreeNode Right;
        public int Value;
    }
}
