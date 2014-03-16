using System;
using System.Collections.Generic;
using FoxDataDig;
using FoxDataDig.Rules;
using NUnit.Framework;

namespace FoxTests
{
    [TestFixture]
    public class RuleTests
    {
        

        public List<EndPointCandel> messList = new List<EndPointCandel>();

        [Test]
        public void ContainsRelationTestBasic()
        {
            ACandleRelationRules containRelation = new CandleTooShortStrokeRule();
            MockUpDataForContainsRule();
            var list = containRelation.Reduce(messList);
        }
        [Test]
        public void ContainsRelationTestKeepFirstMeaningful()
        {
            ACandleRelationRules containRelation = new CandleTooShortStrokeRule();
            MockUpDataForContainsRuleKeepFirst();
            var list = containRelation.Reduce(messList);
        }
        private void MockUpDataForContainsRule()
        {
            this.messList.Clear();
            var c1 = new EndPointCandel();
            c1.type = PointType.Valley;
            c1.instance = new CandleInstance(new DateTime(2012, 07, 02, 13, 05, 00), 0, 2, 1, 0, 0);
            messList.Add(c1);
            var c2 = new EndPointCandel();
            c2.type = PointType.Peek;
            c2.instance = new CandleInstance(new DateTime(2012, 07, 02, 13, 45, 00), 0, 6, 5, 0, 0);
            messList.Add(c2);
            var c3 = new EndPointCandel();
            c3.type = PointType.Valley;
            c3.instance = new CandleInstance(new DateTime(2012, 07, 02, 14, 00, 00), 0, 5, 4, 0, 0);
            messList.Add(c3);
            var c4 = new EndPointCandel();
            c4.type = PointType.Peek;
            c4.instance = new CandleInstance(new DateTime(2012, 07, 02, 15, 00, 00), 0, 9, 7, 0, 0);
            messList.Add(c4);
        }
        private void MockUpDataForContainsRuleKeepFirst()
        {
            this.messList.Clear();
            var c1 = new EndPointCandel();
            c1.type = PointType.Valley;
            c1.instance = new CandleInstance(new DateTime(2012, 07, 02, 13, 05, 00), 0, 2, 1, 0, 0);
            messList.Add(c1);
            var c2 = new EndPointCandel();
            c2.type = PointType.Peek;
            c2.instance = new CandleInstance(new DateTime(2012, 07, 02, 13, 45, 00), 0, 6, 5, 0, 0);
            messList.Add(c2);
            var c3 = new EndPointCandel();
            c3.type = PointType.Valley;
            c3.instance = new CandleInstance(new DateTime(2012, 07, 02, 14, 00, 00), 0, 4, 3, 0, 0);
            messList.Add(c3);
            var c4 = new EndPointCandel();
            c4.type = PointType.Peek;
            c4.instance = new CandleInstance(new DateTime(2012, 07, 02, 14, 10, 00), 0, 5, 4, 0, 0);
            messList.Add(c4);
            var c5 = new EndPointCandel();
            c5.type = PointType.Valley;
            c5.instance = new CandleInstance(new DateTime(2012, 07, 02, 15, 00, 00), 0, 2, 1, 0, 0);
            messList.Add(c5);


            var c6 = new EndPointCandel();
            c6.type = PointType.Peek;
            c6.instance = new CandleInstance(new DateTime(2012, 07, 02, 15, 10, 00), 0, 3, 2, 0, 0);
            messList.Add(c6);
            var c7 = new EndPointCandel();
            c7.type = PointType.Valley;
            c7.instance = new CandleInstance(new DateTime(2012, 07, 02, 15, 20, 00), 0, 2, 2, 0, 0);
            messList.Add(c7);
            var c8 = new EndPointCandel();
            c8.type = PointType.Valley;
            c8.instance = new CandleInstance(new DateTime(2012, 07, 02, 15, 50, 00), 0, 5, 5, 0, 0);
            messList.Add(c8);
        }
    }
}