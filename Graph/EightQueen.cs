using System;
using System.Collections.Generic;
using System.Text;

namespace ACM
{
    using System.Collections.Generic;

    using System.IO;




    class EightQueen
    {

        private List<GridCell> ArrangedList;

        public void printAllGridCells()
        {

            string s = string.Empty;

            foreach (GridCell c in ArrangedList)
            {

                s += "{" + c.xValue + "," + c.yValue + "}";

            }

            //MessageBox.Show(s);

            FileInfo t = new FileInfo(@"c:\result.txt");

            TextWriter Tex = t.AppendText();

            Tex.WriteLine(s);

            Tex.Close();

        }

        public void Run()
        {

            ClearBeforeResult();

            ArrangedList = new List<GridCell>();

            int row = 0;

            int col = 0;

            putCell(row, col);

        }



        private void ClearBeforeResult()
        {

            FileInfo t = new FileInfo(@"c:\result.txt");

            if (File.Exists(@"c:\result.txt"))
            {

                t.Delete();

            }

        }



        private void putCell(int row, int col)
        {

            while (row < 8)
            {

                GridCell cell = makeGridCell(row, col);

                if (ISLegal(cell))
                {

                    ArrangedList.Add(cell);

                    if (col < 7)
                    {

                        putCell(0, col + 1);

                    }

                    else
                    {

                        printAllGridCells();

                        this.RemovelastNode();

                    }

                }

                row++;

            }

            this.RemovelastNode();

            col--;

        }

        private void RemovelastNode()
        {

            if (ArrangedList.Count > 0)

                ArrangedList.RemoveAt(ArrangedList.Count - 1);

        }



        private bool ISLegal(GridCell cell)
        {

            bool result = true;

            foreach (GridCell gridCell in ArrangedList)
            {

                if (gridCell.xValue == cell.xValue) result = false;

                else if (gridCell.yValue == cell.yValue) result = false;

                else if (gridCell.yValue + gridCell.xValue == cell.yValue + cell.xValue) result = false;

                else if (gridCell.yValue - gridCell.xValue == cell.yValue - cell.xValue) result = false;

            }

            return result;

        }



        private GridCell makeGridCell(int row, int col)
        {

            GridCell cell = new GridCell();

            cell.xValue = row;

            cell.yValue = col;

            return cell;

        }



        class GridCell
        {

            public int xValue;

            public int yValue;

        }

    }


}
