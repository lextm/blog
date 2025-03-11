---
layout: post
title: "LordGate Notes: Multithreading Performance"
description: This post is about how to analyze the performance of multithreading scenarios.
tags: SNMP
permalink: /lordgate-notes-multithreading-performance-2a816da2af6d
excerpt_separator: <!--more-->
---
A few performance testing scenarios have been executed recently and the results are quite surprising. Before locating the culprits, this post only shows what the testing reveals.
<!--more-->

## Sample Code

``` csharp
[Test]
[Category("Default")]
public void TestResponses()
{
    var start = 16102;
    var end = start + 40; // change this to 4, 40, and 80.
    var engine = CreateEngine();
    engine.Listener.ClearBindings();
    for (var index = start; index < end; index++)
    {
        engine.Listener.AddBinding(new IPEndPoint(IPAddress.Loopback, index));
    }

    var time = DateTime.Now;
    engine.Start();
    Console.WriteLine(DateTime.Now - time);

    const int timeout = 100000;
    for (int index = start; index < end; index++) // in sync
    //Parallel.For(start, end, index => // async
    {
        GetRequestMessage message = new GetRequestMessage(index, VersionCode.V2, new OctetString("public"), new List<Variable> { new Variable(new ObjectIdentifier("1.3.6.1.2.1.1.1.0")) });
        Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

        Stopwatch watch = new Stopwatch();
        watch.Start();
        var response = message.GetResponse(timeout, new IPEndPoint(IPAddress.Loopback, index), socket);
        watch.Stop();
        Console.WriteLine("manager {0}: {1}", index, watch.Elapsed);
        Assert.AreEqual(index, response.RequestId());
    }
    // );

    engine.Stop();
}
```

## Four Requests in Sync

``` text
manager 16102: 00:00:01.7603102
agent 16102: 00:00:00.0477945
agent 16103: 00:00:00.0008415
manager 16103: 00:00:00.0012003
agent 16104: 00:00:00.0001305
manager 16104: 00:00:00.0004236
agent 16105: 00:00:00.0001108
manager 16105: 00:00:00.0003382
```

Interesting that the very first request takes much longer than all other requests following.

## 40 Requests in Sync

``` text
manager 16102: 00:00:37.6857179
agent 16102: 00:00:00.0814214
agent 16103: 00:00:00.0006769
manager 16103: 00:00:00.0009836
agent 16104: 00:00:00.0001633
manager 16104: 00:00:00.0004758
agent 16105: 00:00:00.0002015
manager 16105: 00:00:00.0005755
agent 16106: 00:00:00.0001284
manager 16106: 00:00:00.0004942
agent 16107: 00:00:00.0001268
manager 16107: 00:00:00.0004138
agent 16108: 00:00:00.0001802
manager 16108: 00:00:00.0022517
agent 16109: 00:00:00.0001494
manager 16109: 00:00:00.0004971
agent 16110: 00:00:00.0001457
manager 16110: 00:00:00.0004478
agent 16111: 00:00:00.0001227
manager 16111: 00:00:00.0004068
agent 16112: 00:00:00.0001227
manager 16112: 00:00:00.0003924
agent 16113: 00:00:00.0001424
manager 16113: 00:00:00.0005012
agent 16114: 00:00:00.0000952
manager 16114: 00:00:00.0003797
agent 16115: 00:00:00.0001108
manager 16115: 00:00:00.0003641
agent 16116: 00:00:00.0000882
manager 16116: 00:00:00.0003510
agent 16117: 00:00:00.0001202
manager 16117: 00:00:00.0003817
agent 16118: 00:00:00.0001014
manager 16118: 00:00:00.0003801
agent 16119: 00:00:00.0001404
manager 16119: 00:00:00.0004593
agent 16120: 00:00:00.0001087
manager 16120: 00:00:00.0004031
agent 16121: 00:00:00.0001194
manager 16121: 00:00:00.0003822
agent 16122: 00:00:00.0001092
manager 16122: 00:00:00.0003715
agent 16123: 00:00:00.0001067
manager 16123: 00:00:00.0003534
agent 16124: 00:00:00.0000981
manager 16124: 00:00:00.0003312
agent 16125: 00:00:00.0000952
manager 16125: 00:00:00.0003571
agent 16126: 00:00:00.0000981
manager 16126: 00:00:00.0003210
agent 16127: 00:00:00.0001005
manager 16127: 00:00:00.0003382
agent 16128: 00:00:00.0000845
manager 16128: 00:00:00.0003255
agent 16129: 00:00:00.0000903
manager 16129: 00:00:00.0003066
agent 16130: 00:00:00.0002237
manager 16130: 00:00:00.0056928
agent 16131: 00:00:00.0001083
manager 16131: 00:00:00.0003842
agent 16132: 00:00:00.0000993
manager 16132: 00:00:00.0003370
agent 16133: 00:00:00.0000981
manager 16133: 00:00:00.0003304
agent 16134: 00:00:00.0001042
manager 16134: 00:00:00.0003493
agent 16135: 00:00:00.0001350
manager 16135: 00:00:00.0004010
agent 16136: 00:00:00.0001026
manager 16136: 00:00:00.0003546
agent 16137: 00:00:00.0001075
manager 16137: 00:00:00.0003374
agent 16138: 00:00:00.0001773
manager 16138: 00:00:00.0028954
agent 16139: 00:00:00.0001030
manager 16139: 00:00:00.0003374
agent 16140: 00:00:00.0000890
manager 16140: 00:00:00.0002890
agent 16141: 00:00:00.0000853
manager 16141: 00:00:00.0002836
```

When testing with 40 requests, the initial delay is much more significant.

## 40 Requests Async

``` text
manager 16102: 00:00:36.2356932
agent 16102: 00:00:00.0481501
agent 16132: 00:00:00.0022435
manager 16132: 00:00:00.9079101
agent 16103: 00:00:00.0003645
manager 16103: 00:00:01.8997028
agent 16133: 00:00:00.0002212
manager 16133: 00:00:01.9948014
manager 16104: 00:00:00.9910570
agent 16104: 00:00:00.0001720
agent 16122: 00:00:00.0001289
manager 16122: 00:00:03.5007052
agent 16134: 00:00:00.0001215
manager 16134: 00:00:00.0012196
manager 16105: 00:00:01.9983143
agent 16105: 00:00:00.0001490
agent 16106: 00:00:00.0001863
manager 16106: 00:00:00.9992511
manager 16123: 00:00:00.9987298
agent 16123: 00:00:00.0014532
agent 16107: 00:00:00.0001859
manager 16107: 00:00:00.0015604
agent 16135: 00:00:00.0001358
manager 16135: 00:00:01.0005217
agent 16136: 00:00:00.0004421
manager 16136: 00:00:00.9967724
manager 16139: 00:00:00.9986259
agent 16139: 00:00:00.0004318
agent 16108: 00:00:00.0004470
manager 16108: 00:00:01.9984962
agent 16110: 00:00:00.0003624
manager 16110: 00:00:03.0002475
manager 16124: 00:00:02.0030346
agent 16124: 00:00:00.0003218
agent 16109: 00:00:00.0002877
manager 16109: 00:00:00.0041623
manager 16137: 00:00:01.0059658
agent 16137: 00:00:00.0002914
agent 16125: 00:00:00.0003239
manager 16125: 00:00:03.0100932
agent 16111: 00:00:00.0003317
manager 16111: 00:00:00.0087413
manager 16138: 00:00:00.0051722
manager 16112: 00:00:07.5159084
manager 16126: 00:00:00.0181556
agent 16126: 00:00:00.0003772
manager 16113: 00:00:04.0226611
agent 16114: 00:00:00.0002496
manager 16114: 00:00:01.0136439
agent 16127: 00:00:00.0002799
agent 16112: 00:00:00.0002857
manager 16130: 00:00:00.0168735
agent 16140: 00:00:00.0002709
manager 16127: 00:00:00.0037046
agent 16131: 00:00:00.0003276
manager 16131: 00:00:00.0015115
agent 16113: 00:00:00.0002660
agent 16138: 00:00:00.0002988
agent 16130: 00:00:00.0002853
manager 16140: 00:00:01.0153652
manager 16141: 00:00:00.0012537
agent 16115: 00:00:00.0003300
agent 16141: 00:00:00.0006137
manager 16128: 00:00:00.0011925
manager 16115: 00:00:00.0213027
manager 16129: 00:00:00.0010735
agent 16129: 00:00:00.0009655
agent 16128: 00:00:00.0002898
agent 16116: 00:00:00.0022882
manager 16116: 00:00:00.0026938
agent 16117: 00:00:00.0001654
manager 16117: 00:00:00.0005057
agent 16118: 00:00:00.0000919
manager 16118: 00:00:00.0003440
agent 16119: 00:00:00.0001063
manager 16119: 00:00:00.0003957
agent 16120: 00:00:00.0001038
manager 16120: 00:00:00.0003292
agent 16121: 00:00:00.0001034
manager 16121: 00:00:00.0003058
```

Parallel execution takes even longer to finish, as not only it has no improvement on the initial request, but also it makes some following requests slower.

Profiling only shows the delay comes from System.Net.Sockets.Socket.Receive(), which is less useful.

## Further Analysis

Interestingly the final analysis was performed by adding more time logging to the agent part, which reveals the culprit.

The initial delay comes from the agent, where it takes a very long time to process the initial request. By tuning the thread pool minimal worker thread count to a larger number, the delay can be safely eliminated.
