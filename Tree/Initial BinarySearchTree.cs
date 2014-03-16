/*
在初始化查找二叉树的时候不能用数组结构代替。
因为数组只能用于表示一个完全二叉树（complete binary tree），
例如“堆”，就是一种完全二叉树。
所以堆排序可以利用数组的前几个未排列的位子作为堆结构。
*/
using System;
using System.Collections.Generic;
using System.Text;

namespace ACM
{
    public class BinerySearchTree
    {
        private readonly int[] buffer = { 5, 21, 6, 8, 9, 32, 13, 12, 41, 2, 3, 4, 1 };
        public void Run()
        {
            TreeNode root= InitialBinerySearchTree();
        }

        private TreeNode InitialBinerySearchTree()
        {
            TreeNode root = new TreeNode(buffer[0]);
            root.Value = buffer[0];
            for (int i = 1; i < buffer.Length; i++)
            {
               Arrange(i,root); 
            }
            return root;
        }

        private void Arrange(int current, TreeNode root)
        {
            if (root.Value > buffer[current])//put to left tree
            {
                if (root.Left == null)
                { TreeNode left = new TreeNode(buffer[current]); root.Left = left; }
                else
                {
                    Arrange(current, root.Left);
                }
            }
            else 
            {
                if (root.Right == null)
                { TreeNode right = new TreeNode(buffer[current]); root.Right = right; }
                else
                {
                    Arrange(current, root.Right);
                }
            }
        }
    }
    
}
