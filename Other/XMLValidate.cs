using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;
using System.Xml.Schema;

namespace ACM
{
    public class XMLValidate
    {
        internal void validateXml()
        {
            // Create the XmlReader object.
            XmlReader reader = XmlReader.Create(@"C:\Documents and Settings\zbo\Desktop\Co3.xml");
            XmlValidatingReader validator = new XmlValidatingReader(reader);
            validator.ValidationType = ValidationType.Schema;
            validator.ValidationEventHandler += new ValidationEventHandler(validator_ValidationEventHandler);
            // Parse the file. 
            while (validator.Read()) ;
        }

        void validator_ValidationEventHandler(object sender, ValidationEventArgs e)
        {
            Console.WriteLine(e.Message);
        }
    }
}
