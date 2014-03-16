using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace FoxDataDig
{
     public enum PointType
    {Peek,Valley,MeanLess}
    public class EndPointCandel
    {
        public CandleInstance instance { get; set; }
        public PointType type { get; set; }
    
    }

    public class CandleInstance
    {
        public CandleInstance(DateTime date, float open, float high, float low, float close, float volumn)
        {
            this.Datetime = date;
            High = high;
            Low = low;
            Close = close;
            Open = open;
            Volumn = volumn;
        }

        public CandleInstance(float high, float low)
        {
            High = high;
            Low = low;
        }

        public DateTime Datetime { get; set; }
        public float Open
        { get; set; }
        public float High
        { get; set; }
        public float Low
        { get; set; }
        public float Close
        { get; set; }
        
        public float Volumn
        { get; set; }
    }
}
