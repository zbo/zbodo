using System;
using System.Collections.Generic;

namespace FoxDataDig.Rules
{
    public class ACandleRelationRules
    {
        public virtual List<EndPointCandel> Reduce(List<EndPointCandel> messList)
        {
            throw new NotImplementedException();
        }

        public List<EndPointCandel> RemoveMeanLess(List<EndPointCandel> messList)
        {
            var result = new List<EndPointCandel>();
            foreach (EndPointCandel item in messList)
            {
                if (item.type != PointType.MeanLess)
                {
                    result.Add(item);
                }
            }
            return result;
        }
    }

    public class CandleTooShortStrokeRule : ACandleRelationRules
    {
        public class MeanLessPair
        {
            public  EndPointCandel PointOne;
            public EndPointCandel pointTwo;
            public int PointOneIndex;
            public int PointTwoIndex;

            public MeanLessPair(EndPointCandel pointOne, EndPointCandel pointTwo,int pointOneIndex,int pointTwoIndex)
            {
                PointOne = pointOne;
                this.pointTwo = pointTwo;
                this.PointOneIndex = pointOneIndex;
                this.PointTwoIndex = pointTwoIndex;
            }
        }
        List<MeanLessPair> MeanLessList=new List<MeanLessPair>();
        public override List<EndPointCandel> Reduce(List<EndPointCandel> messList)
        {
            var FourCandels = new TimeSpan(0, 0, 20, 0);
            var TooShortCollections = new List<EndPointCandel>();
            for (int i = 1; i < messList.Count; i++)
            {
                TimeSpan timeGap = messList[i].instance.Datetime - messList[i - 1].instance.Datetime;
                if (timeGap < FourCandels)
                {
                    MeanLessPair pair=new MeanLessPair(messList[i-1],messList[i],i-1,i);
                    this.MeanLessList.Add(pair);
                }
            }
            MarkMeanLessPoints();
            return RemoveMeanLess(messList);
        }

        private void MarkMeanLessPoints()
        {
            List<List<MeanLessPair>> GroupedMeanLessList = GroupThemByBreak();
            var a = 0;
        }

        private List<List<MeanLessPair>> GroupThemByBreak()
        {
            List<List<MeanLessPair>> group = new List<List<MeanLessPair>>();
            var tmp = new List<MeanLessPair>();
            foreach (var meanLessPair in MeanLessList)
            {
                if (tmp.Count==0) {tmp.Add(meanLessPair);continue;}//空的
                if (tmp[tmp.Count - 1].PointTwoIndex == meanLessPair.PointOneIndex) { tmp.Add(meanLessPair); continue; } //连续的
                if (tmp[tmp.Count - 1].PointTwoIndex < meanLessPair.PointOneIndex)
                {
                   group.Add(tmp);
                   tmp=new List<MeanLessPair>();
                   tmp.Add(meanLessPair); continue;
                }
            }
            if(tmp.Count>0)
            group.Add(tmp);
            return group;
        }
    }

    public class PeekValleyRepeatRule : ACandleRelationRules
    {
        public override List<EndPointCandel> Reduce(List<EndPointCandel> messList)
        {
            EndPointCandel lastMeanFulPoint = messList[0];
            for (int i = 1; i < messList.Count; i++)
            {
                if (messList[i].type == lastMeanFulPoint.type)
                {
                    if (lastMeanFulPoint.type == PointType.Peek) //后面的高点更高
                    {
                        if (messList[i].instance.High > lastMeanFulPoint.instance.High)
                        {
                            lastMeanFulPoint.type = PointType.MeanLess;
                            lastMeanFulPoint = messList[i];
                        }
                        else //后面高点不够高
                            messList[i].type = PointType.MeanLess;
                    }
                    else if (lastMeanFulPoint.type == PointType.Valley)
                    {
                        if (messList[i].instance.Low < lastMeanFulPoint.instance.Low) //后面的低点更低
                        {
                            lastMeanFulPoint.type = PointType.MeanLess;
                            lastMeanFulPoint = messList[i];
                        }
                        else
                            messList[i].type = PointType.MeanLess;
                    }
                }
                else
                {
                    lastMeanFulPoint = messList[i];
                }
            }
            return RemoveMeanLess(messList);
        }
    }

    public class CandlePeekEqualValleyStrokeRule : ACandleRelationRules
    {
        public override List<EndPointCandel> Reduce(List<EndPointCandel> messList)
        {
            for (int i = 1; i < messList.Count; i++)
            {
                float firstValue = GenValue(messList[i - 1]);
                float secondValue = GenValue(messList[i]);
                if (firstValue == firstValue)
                {
                    messList[i].type = PointType.MeanLess;
                    messList[i - 1].type = PointType.MeanLess;
                }
            }
            return RemoveMeanLess(messList);
        }

        private float GenValue(EndPointCandel endPointCandel)
        {
            if (endPointCandel.type == PointType.Peek)
                return endPointCandel.instance.High;
            else
                return endPointCandel.instance.Low;
        }
    }
}