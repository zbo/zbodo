using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using FoxDataDig.Rules;

namespace FoxDataDig
{
    public class Min5DataAccess
    {
        public Min5DataAccess(string datafolder)
        {
            this.SetDataFolder(datafolder);
        }

        private string drawLine =
            @"drawline(year={0} and month={1} and day={2} and hour={3}" +
            " and minute={4}, {5},year={6} and month={7} and day={8}" +
            " and hour={9} and minute={10},{11},0), COLORBULE,LINETHICK2;";

        private string datafoler = string.Empty;
        private string stockName = string.Empty;
        private List<CandleInstance> allData = new List<CandleInstance>();
        private List<CandleInstance> standardData = new List<CandleInstance>();
        private List<EndPointCandel> possibleEndPoint = new List<EndPointCandel>();

        private void SetDataFolder(string p)
        {
            this.datafoler = p;
        }

        public void OpenMin5Data(string p)
        {
            this.stockName = p + ".txt";
            var fileStream = File.Open(datafoler + '\\' + stockName, FileMode.Open);
            StreamReader reader = new StreamReader(fileStream);
            while (!reader.EndOfStream)
            {
                string line = reader.ReadLine();
                string[] array = line.Split(' ');
                DateTime date = BuildDateTime(array);
                CandleInstance instance = new CandleInstance(date, float.Parse(array[2]), float.Parse(array[3]),
                                                             float.Parse(array[4]), float.Parse(array[5]),
                                                             float.Parse(array[6]));
                allData.Add(instance);
            }
        }

        private DateTime BuildDateTime(string[] array)
        {
            string date = array[0];
            string time = array[1];
            string[] allDate = date.Split('/');
            string[] allTime = time.Split(':');
            return new DateTime(int.Parse(allDate[0]), int.Parse(allDate[1]),
                                int.Parse(allDate[2]), int.Parse(allTime[0]), int.Parse(allTime[1]), 0);
        }

        public void BuildStroke()
        {
            BuildRoughPoints();
            ReduceEndPoints();
        }

        private void ReduceEndPoints()
        {
            PeekValleyRepeatRule peekValleyRepeatRule = new PeekValleyRepeatRule();
            this.possibleEndPoint = peekValleyRepeatRule.Reduce(this.possibleEndPoint);
            CandleTooShortStrokeRule tooShortStrokeRule = new CandleTooShortStrokeRule();
            this.possibleEndPoint = tooShortStrokeRule.Reduce(this.possibleEndPoint);
            CandlePeekEqualValleyStrokeRule peekEqualValleyStrokeRule = new CandlePeekEqualValleyStrokeRule();
            this.possibleEndPoint = tooShortStrokeRule.Reduce(this.possibleEndPoint);
            
            //List<ACandleRelationRules> allRules=new List<ACandleRelationRules>();
            //allRules.Add(new PeekValleyRepeatRule());
            //allRules.Add(new CandleTooShortStrokeRule());
            //allRules.Add(new CandlePeekEqualValleyStrokeRule());
            //foreach(var rule in allRules)
            //{
            //    this.possibleEndPoint=rule.Reduce(this.possibleEndPoint);
            //}
        }

        private void BuildRoughPoints()
        {
            //找出所有可能的分型
            for (int i = 1; i < allData.Count; i++)
            {
                if (IsPeekOfTen(i))
                {
                    var tmp = new EndPointCandel();
                    tmp.instance = allData[i];
                    tmp.type = PointType.Peek;
                    this.possibleEndPoint.Add(tmp);
                }
                else if (IsValleyOfTen(i))
                {
                    var tmp = new EndPointCandel();
                    tmp.instance = allData[i];
                    tmp.type = PointType.Valley;
                    this.possibleEndPoint.Add(tmp);
                }
            }
        }

        private bool IsValleyOfTen(int i)
        {
            if (i < 5 || i > allData.Count - 5) return false;
            if (allData[i].Low <= allData[i - 1].Low && allData[i].Low <= allData[i - 2].Low &&
                allData[i].Low <= allData[i - 3].Low && allData[i].Low <= allData[i - 4].Low &&
                allData[i].Low <= allData[i + 1].Low && allData[i].Low <= allData[i + 2].Low &&
                allData[i].Low <= allData[i + 3].Low && allData[i].Low <= allData[i + 4].Low)
            {
                return true;
            }
            return false;
        }

        private bool IsPeekOfTen(int i)
        {
            if (i < 5 || i > allData.Count - 5) return false;
            if (allData[i].High >= allData[i - 1].High && allData[i].High >= allData[i - 2].High &&
                allData[i].High >= allData[i - 3].High && allData[i].High >= allData[i - 4].High &&
                allData[i].High >= allData[i + 1].High && allData[i].High >= allData[i + 2].High &&
                allData[i].High >= allData[i + 3].High && allData[i].High >= allData[i + 4].High)
            {
                return true;
            }
            return false;
        }

        public void GenerateOutput()
        {
            string line = string.Empty;
            string startPoint = string.Empty;
            string endPoint = string.Empty;
            foreach (var item in this.possibleEndPoint)
            {
                Console.WriteLine("Date:{0}  type:{1} ", item.instance.Datetime, item.type);
            }
            StringBuilder sbuilder = new StringBuilder();
            for (int i = 0; i < possibleEndPoint.Count - 1; i++)
            {
                if (possibleEndPoint[i].type == PointType.Peek)
                {
                    startPoint = "H";
                    endPoint = "L";
                }
                else
                {
                    startPoint = "L";
                    endPoint = "H";
                }
                line = string.Format(drawLine, possibleEndPoint[i].instance.Datetime.Year,
                                     possibleEndPoint[i].instance.Datetime.Month, possibleEndPoint[i].instance.Datetime.Day,
                                     possibleEndPoint[i].instance.Datetime.Hour, possibleEndPoint[i].instance.Datetime.Minute, startPoint,
                                     possibleEndPoint[i + 1].instance.Datetime.Year,
                                     possibleEndPoint[i + 1].instance.Datetime.Month, possibleEndPoint[i + 1].instance.Datetime.Day,
                                     possibleEndPoint[i + 1].instance.Datetime.Hour, possibleEndPoint[i + 1].instance.Datetime.Minute, endPoint);
                sbuilder.AppendLine(line);
            }
            TextWriter writer = new StreamWriter("out.txt", false, Encoding.ASCII);
            writer.Write(sbuilder.ToString());
            writer.Close();
        }

        public void BuildStandCandle()
        {
            var currentStay = allData[0];
            for (int i = 1; i < allData.Count; i++)
            {
                //if(allData[i].High<=currentStay.High && allData[i])
            }
        }
    }
}