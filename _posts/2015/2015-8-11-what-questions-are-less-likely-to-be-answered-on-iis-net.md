---
layout: post
title: "What Questions are Less Likely to Be Answered on IIS.net?"
description: "This post is about what questions are less likely to be answered on IIS.net forums."
tags: IIS
permalink: /what-questions-are-less-likely-to-be-answered-on-iis-net-49310b254eb9
excerpt_separator: <!--more-->
---

Of course questions are welcome on any Microsoft forums, and that's why Microsoft spends so much each year on them. However, some questions won't get the answers you wanted, and even never be processed due to their weird nature at the very beginning. It is OK to post them over and over again, but you should be aware that they are less welcome (or not welcome if I don't pretend to be polite). Why or why will be explained later. Here I only focus on http://forums.iis.net as I am just familiar with IIS.

<!--more-->

## Category 1: Third party components (not Microsoft products at all)

The following examples are quite common but I personally never find good answers for them,

- How can I let IIS and Apache co-exist?
- How can I get WebSphere/Tomcat work with IIS?
- How can I publish a ColdFusion application onto IIS?
- …

As there are far too many things might work with IIS, you can imagine this list can be quite lengthy. However, posting them at IIS.net forums is probably the last thing you should ever do.

Each such components has its own mailing lists or forums where experts stay, and commercial products such as WebSphere and ColdFusion even have vendor support (from IBM and Adobe respectively). Thus, if you do want to get a quick answer or proper guidance, search on the Internet for the proper resources.

Another example is the PHP support on IIS, which I documented in more details [in another post]({% post_url 2018/2018-3-31-why-you-should-forget-php-manager-for-iis %}).

IIS.net is very Microsoft centric and many experts I know of (including myself) never have a chance to play with such third party components. We are willing to help, but we are obvious not the guys you are looking for.

## Category 2: Microsoft products that rely on IIS

IIS is so flexible that whenever possible Microsoft's own products rely on it. SharePoint, Exchange, Lync and so on usually have a few components that depend on IIS. The following questions are also common, related to them,

- What IIS settings I should change to speed up SharePoint?
- What to do when Exchange Web Access gives me a 500 error page?
- Why Lync Web Access portal does not allow me to log in?
- …

Many of them appear to be typical IIS questions, about performance tuning, authentication, and so on. However, you should always remember the facts that Microsoft products are all huge. For example, SharePoint builds a complex platform upon IIS, and sometimes completely changes IIS behaviors (such as enforcing NTLM in some versions). Blindly applying an IIS general trick might unexpectedly break the product you are troubleshooting.

Again, Microsoft has dedicate TechNet forums (now tags) for those products. To get a proper answer from MVPs and product support guys for those products, your first step is to post the questions to those dedicate forums. That's why you see a million times that on IIS.net forums, users are redirected to TechNet.

## Category 3: Questions related to development

Sometimes we see ASP.NET developers post questions on IIS.net forums, asking like,

- How can I write this function in VS?
- What's wrong with my code?
- Why WCF on IIS does not work while it works in VS?

Well, that's why Microsoft has MSDN WCF forum and http://forums.asp.net for you developers. Such questions should go there when you can meet thousands of good developers who have the experience to answer that. The fact is crude that IIS administration and web site development are two worlds apart.

## Category 4: Questions that require significant amount of effort

Your expectation must be to receive some help from someone by posting on such a forum. However, don't set the bar too high, as most experts there are not paid by Microsoft, who volunteer their spare time answering questions and giving out hints.

Thus, if something really requires lots of effort, such as

- FRT log analysis
- Dump analysis
- Performance log analysis
- Complex environment analysis
- many other cases …

Then you should really consider opening a support case with Microsoft support via http://support.microsoft.com. Web forums have their natural limitation, that you cannot share all important data to others. But for a product as complicated as IIS, troubleshooting a difficult case requires lots of data and sometimes even direct access to server settings and source code.

Yes, there are Microsoft employees hanging out there. You might be lucky if they happen to have the time to cover you.

## Sidenote: Why I am redirected everywhere?

The most horrible part is that some users were kicked from forums to forums and never received the help they expected. You should understand that some forum members might not have enough experience with the certain components (even MVPs or Microsoft employees can make mistakes as we are all human), so they could not find the answer you wanted and simply redirect you to another forum that you might meet another expert who might know the answer. Again, open a support case should help you out.
