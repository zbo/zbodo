using System;
using System.Collections.Generic;
using System.Text;

namespace Code
{
    public class MazeFindWay
    {
        private char[][] Maze = new char[5][];
        private int RowNumber = 5;
        private int ColumnNumber = 4;

        public MazeFindWay()
        {
            Maze[0] = "0X00".ToCharArray();
            Maze[1] = "0000".ToCharArray();
            Maze[2] = "0XX0".ToCharArray();
            Maze[3] = "0XX0".ToCharArray();
            Maze[4] = "0000".ToCharArray();
        }
        public void Run()
        {
            this.printMaze();
            Node start = new Node(0, 0);
            Node end = new Node(4, 3);
            List<Node> ArrangedList = new List<Node>();
            GetPossiblePath(start, end, ArrangedList);
            this.printMaze();
            Console.ReadLine();
            
        }

        private void GetPossiblePath(Node start, Node end, List<Node> ArrangedList)
        {
            ArrangedList.Add(start);
            List<Node> possibleNext = GetPossibleNext(start, ArrangedList);
            foreach (Node node in possibleNext)
            {
                if (node.row == end.row && node.column == end.column)
                {
                    PrintArrangement(ArrangedList);
                    Console.WriteLine("==============================");
                }
                else
                {
                    GetPossiblePath(node, end, ArrangedList);
                }
            }
            ArrangedList.Remove(start);
        }

        private void PrintArrangement(List<Node> ArrangedList)
        {
            foreach (Node node in ArrangedList)
            {
                Console.WriteLine("({0},{1})->", node.row, node.column);
            }
        }

        private List<Node> GetPossibleNext(Node start, List<Node> ArrangedList)
        {
            List<Node> possibleNext = new List<Node>();
            if (start.row > 0)
                possibleNext.Add(new Node(start.row - 1, start.column));
            if (start.row < RowNumber - 1)
                possibleNext.Add(new Node(start.row + 1, start.column));
            if (start.column > 0)
                possibleNext.Add(new Node(start.row, start.column - 1));
            if (start.column < ColumnNumber - 1)
                possibleNext.Add(new Node(start.row, start.column + 1));
            for (int i = possibleNext.Count - 1; i >= 0; i--)
            {
                if (Maze[possibleNext[i].row][possibleNext[i].column] == 'X')
                    possibleNext.RemoveAt(i);
                //else if (AlreadyExist(possibleNext[i], ArrangedList))
                else if (ArrangedList.Find(n=>n.row==possibleNext[i].row&&n.column==possibleNext[i].column)!=null)
                    possibleNext.RemoveAt(i);
            }
            return possibleNext;
        }

        private bool AlreadyExist(Node node, List<Node> ArrangedList)
        {
            foreach (Node n in ArrangedList)
            {
                if (n.row == node.row && n.column == node.column)
                    return true;
            }
            return false;
        }
        private void printMaze()
        {
            for (int i = 0; i < RowNumber; i++)
            {
                for (int j = 0; j < ColumnNumber; j++)
                    Console.Write(" " + Maze[i][j] + " ");
                Console.WriteLine();
            }
        }
        class Node
        {
            public Node(int row, int column)
            { this.row = row; this.column = column; }
            public int row;
            public int column;
        }
    }
}
