using System;
using System.Reflection;
using System.Threading;
using System.Runtime.Remoting;


class Program
{
    static void Main(string[] args)
    {
        // Get a reference to the AppDomain that the calling thread is executing in
        AppDomain adCallingThreadDomain = Thread.GetDomain();
        // Every AppDomain is assigned a friendly string name, which is helpful
        // for debugging. Get this AppDomain's friendly name and display it
        String callingDomainName = adCallingThreadDomain.FriendlyName;
        Console.WriteLine("Default AppDomain's friendly name={0}", callingDomainName);
        // Get & display the assembly in our AppDomain that contains the 'Main' method
        String exeAssembly = Assembly.GetEntryAssembly().FullName;
        Console.WriteLine("Main assembly={0}", exeAssembly);
        // Define a local variable that can refer to an AppDomain
        AppDomain ad2 = null;
        // DEMO 1: Cross-AppDomain communication using Marshal-by-Reference
        Console.WriteLine("{0}Demo #1: Marshal-by-Reference", Environment.NewLine);
        // Create a new AppDomain (security & configuration match current AppDomain)
        ad2 = AppDomain.CreateDomain("AD #2", null, null);
        // Load our assembly into the new AppDomain, construct an object, marshal
        //it back to our AD (we really get a reference to a proxy)
        MarshalByRefType mbrt = (MarshalByRefType)ad2.CreateInstanceAndUnwrap(exeAssembly, "MarshalByRefType");
        Type t = mbrt.GetType();
        // Prove that we got a reference to a proxy object
        Console.WriteLine("Is proxy={0}", RemotingServices.IsTransparentProxy(mbrt));
        // This looks as if we're calling a method on a MarshalByRefType instance, but
        // we're not. We're calling a method on an instance of a proxy type.
        // The proxy transitions the thread to the AppDomain owning the object and
        // calls this method on the real object
        mbrt.SomeMethod(callingDomainName);
        // Unload the new AppDomain
        AppDomain.Unload(ad2);
        // mbrt refers to a valid
        // mbrt refers to a valid proxy object;
        // this proxy refers to an invalid AppDomain now
        try
        {
            // We're calling a method on the proxy type object.
            // The AD is invalid, an exception is thrown
            mbrt.SomeMethod(callingDomainName);
            Console.WriteLine("Successful call.");
        }
        catch (AppDomainUnloadedException)
        {
            Console.WriteLine("Failed call.");
        }

        // DEMO 2: Cross-AppDomain Communication using Marshal-by-Value
        Console.WriteLine("{0}Demo #2: Marshal-by-Value", Environment.NewLine);
        // Create a new AppDomain (security & configuration match current AppDomain)
        ad2 = AppDomain.CreateDomain("AD #2", null, null);
        // Load our assembly into the new AppDomain, construct an object, marshal
        // it back to our AD (we really get a copy of the object with the same state)
        MarshalByValType mbvt = (MarshalByValType)ad2.CreateInstanceAndUnwrap(exeAssembly, "MarshalByValType");
        // Prove that we did NOT get a reference to a proxy object
        Console.WriteLine("Is proxy={0}", RemotingServices.IsTransparentProxy(mbvt));
        // This looks as if we're calling a method on a MarshalByValType object, and we are
        mbvt.SomeMethod(callingDomainName);
        // Unload the new AppDomain
        AppDomain.Unload(ad2);
        // mbvt refers to valid object; unloading the AppDomain has no impact.
        try
        {
            // We're calling a method on an object; no exception is thrown
            mbvt.SomeMethod(callingDomainName);
            Console.WriteLine("Successful call.");
        }
        catch (AppDomainUnloadedException)
        {
            Console.WriteLine("Failed call.");
        }

        // DEMO 3: Cross-AppDomain Communication using non-marshalable type
        Console.WriteLine("{0}Demo #3: Non-Marshalable Type", Environment.NewLine);
        // Create a new AppDomain (security & configuration match current AppDomain)
        ad2 = AppDomain.CreateDomain("AD #2", null, null);
        // Load our assembly into the new AppDomain, construct an object, try
        // to marshal it back to our AD (exception is thrown)
        NotMarshalableType nmt = (NotMarshalableType)ad2.CreateInstanceAndUnwrap(exeAssembly, "NotMarshalableType");
        // We won't get here...






        Console.ReadLine();
    }
}
public class MarshalByRefType : MarshalByRefObject
{
    DateTime creation = DateTime.Now;
    public MarshalByRefType()
    {
        Console.WriteLine("{0} ctor running in {1}",
        this.GetType().ToString(), Thread.GetDomain().FriendlyName);
    }
    public void SomeMethod(String callingDomainName)
    {
        Console.WriteLine("Calling from '{0}' to '{1}'.",
        callingDomainName, Thread.GetDomain().FriendlyName);
    }
}
// Instances can be marshaled by value across AppDomain boundaries
[Serializable]
public class MarshalByValType : Object
{
    DateTime creation = DateTime.Now;
    public MarshalByValType()
    {
        Console.WriteLine("{0} ctor running in {1}",
        this.GetType().ToString(), Thread.GetDomain().FriendlyName);
    }
    public void SomeMethod(String callingDomainName)
    {
        Console.WriteLine("Calling from '{0}' to '{1}'.",
        callingDomainName, Thread.GetDomain().FriendlyName);
    }
}
// Instances cannot be marshaled across AppDomain boundaries
//[Serializable]
public class NotMarshalableType : Object
{
    DateTime creation = DateTime.Now;
    public NotMarshalableType()
    {
        Console.WriteLine("{0} ctor running in {1}",
        this.GetType().ToString(), Thread.GetDomain().FriendlyName);
    }
    public void SomeMethod(String callingDomainName)
    {
        Console.WriteLine("Calling from '{0}' to '{1}'.",
        callingDomainName, Thread.GetDomain().FriendlyName);
    }
}