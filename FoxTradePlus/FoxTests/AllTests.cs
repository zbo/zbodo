using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using FoxDataDig;
using NUnit.Framework;

namespace FoxTests
{
    [TestFixture]
    public class Test
    {
        [Test]
        public void MyTest()
        {
            var access = new Min5DataAccess(@"C:\TXTMIN5");
            access.OpenMin5Data("SH600051");
            access.BuildStandCandle();
            access.BuildStroke();
            access.GenerateOutput();

        }
    }
}
