---
layout: post
title: "Touch Mouse Mate: Homepage Delay and 1.5 Release Technical Details"
description: "This post is about the technical details of TMM 1.5."
tags: Windows
permalink: /touch-mouse-mate-homepage-delay-and-1-5-release-technical-details-4e0b6c212eeb
excerpt_separator: <!--more-->
---
Our 1.4 installers are not yet available. CodePlex guys have not yet identified what prevents me from publishing this project, so we have to wait for more days. The good news is that now we have nice progress on version 1.5. Details are provided below.
<!--more-->

## TMM 1.4 Revisit

TMM 1.4 uses J5's implementation of touch-over-click and middle-click.

A touch-over-click is that when you place a finger on the surface of Touch Mouse, if this touch lasts longer than minimal single-click timeout and shorter than maximal single-click timeout, TMM simulates a mouse key down event and a mouse key up event. In this way, Windows treats this touch like a physical click.

A middle-click is that when TMM finds out that you have one finger touched in the left touch zone, and another in the right touch zone, it simulates a middle key down event and a middle key up event. In this way, Windows treats this as a physical middle click.

The disadvantages of J5's implementation is that,

1. key down and key up events are simulated at the same time.
1. The use of minimal and maximal single-click timeout prevents you from doing a long enough click.

Both of them lead to the difficulty of supporting drag and drop. For example, when you left click on a window's title bar, and hold for a while, you can drag this window around by moving your mouse. However, with TMM 1.4 touch-over-click, you cannot achieve the same behavior, so from time to time you still need to physically click the mouse to perform some actions in Windows, which weakens the joy of touch-over-click.

In TMM 1.4, I more focused on packaging the binaries with a convenient installer, and added necessary UI elements (notify icon, and menu items) for end users to tune TMM for personal experience, so I was not able to do much on tuning the low level implementation.

## TMM 1.5 Preview

If you watch our repository on GitHub, https://github.com/lextm/touchmousemate, you should have noticed significant changes recently, as I heavily changed the low level implementation, and now we almost have a brand new engine for touch detection.

So let's first see how a touch can be analyzed by numbers.

### Section 1 Touch Mouse Sensor

The Touch Mouse sensor returns a bitmap of 13*15, from which we can detect your finger spot, (picture is taken from Touch Mouse SDK WPF sample)

![img-description](/images/touch-mouse-sample.png)
_Figure 1: Touch Mouse SDK Sample._

Then we horizontally divide the whole Touch Mouse surface to fourth parts (J5's definition, note that middle click zone is removed in 1.3 and 1.4),

* The left most zone (for your thumb right-handed)
* The left click zone (for left click)
* The right click zone (for right click)
* The right most zone (for ring finger and pinky)

The left/right most zones are generally not used in TMM for touch detection, as you often need to put thumb/ring finger/pinky there to move the mouse around.

### Section 2 Touch Strength and Key Down/Up Detection

OK. Now let's focus on left click zone and see what is defined as "touch strength".

The dark area in the above bitmap is dark because the sensor sends back integer 0 for that pixel. So if we sum up all pixel values in left click zone, we get a value that represent the "strength" of a touch at the sampling time slot.

![img-description](/images/touch-mouse-strength.png)
_Figure 2: Touch Strength._

Observation shows that if two clicks are made sequentially, a strength-time curve can be drawn as above. If the sudden increase/decrease can be calculated, we can simulate key down/up events separately and the whole simulation can be more accurate. In TouchZone.cs you can find how I implemented such detection.

However, we still need to pay attention to the time difference between the key down and key up events. If the time difference is too small, we should consider that as a false alarm and ignore it.

### Section 3 State Machine Processing Pipeline

In order to better process the key down/up events, a state machine is constructed (see StateMachine.cs).

![img-description](/images/touch-diagram.png)
_Figure 3: Touch State Machine._

The above chart shows the different states and the state transformation (red arrows indicate key down event triggers, while blue ones indicate key up event triggers).

To detect finger movement, currently we keep calculating center of mass for the touch spot and the total amount of movement in each touch zone. Therefore, when the movement is larger than a threshold (0.04 currently) TMM tells the state machine that a move is detected, and the related state transformation is triggered. This extra check is added to prevent TMM from breaking Microsoft's default gestures.

## Notice

Note that TMM 1.5 is still in its early stage and many parameters (timeout values and thresholds) are subject to change so as to achieve better performance.

Stay tuned.
