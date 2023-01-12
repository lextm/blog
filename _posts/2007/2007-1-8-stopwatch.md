---
layout: post
title: "Stopwatch的手术"
description: "这篇文章讲述了 Stopwatch 相关的代码重构。"
tags: Code-Beautifier-Collection Delphi
permalink: /stopwatch的手术-ecd03c9b6020
excerpt_separator: <!--more-->
---
(CSDN Jan 08, 2007)

本来设计Stopwatch的时候，仅仅打算实现Boost库中的timer类型就好了。不过，一个用来测量时间间隔的Elapse函数也用处不小。这样的一个单元本来已经够用了。但是元旦的时候遇上了一个新的问题，一个Stopwatch能否在某段时间停止工作，然后在另一个时刻被唤醒然后继续工作？这样的需求导致了我又加上了挂起和继续两个操作。代码也就因此变得复杂起来。 这样一来自然就引发了重构的问题。
<!--more-->

从感觉来看，向着State模式前进总是可以的。所以开始的时候加入了一些状态的东西，不过仔细看起来还是问题不少。

``` csharp
// lextm: this is stopwatch class.
// Copyright © 2006–2007 Lex Li
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111–1307

using System;

namespace Lextm.Diagnostics {

    ///
    /// Stopwatch class.
    ///
    public class Stopwatch {

        ///
        /// Constructor.
        ///
        public Stopwatch( ) {}

        ///
        /// Starts the timing.
        ///
        public void Restart( ) {
            internalState = new State();
            internalState.Start();
        }

        ///
        /// Stops the timing.
        ///
        /// Once stopped, you have to it.
        ///
        public void Stop( ) {
            internalState.Stop();
            internalState = null;
        }

        ///
        /// Resumes a timing.
        ///
        ///
        public void Resume( ) {
            if (internalState != null) {
                internalState.Wake();
            }
        }

        ///
        /// Suspends timing.
        ///
        ///
        public void Suspend( ) {
            if (internalState != null) {
                internalState.Sleep(null);
            }
        }

        ///
        /// Count in milliseconds.
        ///
        /// This counts from the beginning of timing.
        ///
        public int Value {
            get {
                if (internalState == null) {
                    return 0;
                } else {
                    return internalState.GetValue();
                }
            }
        }

        ///
        /// Interval in milliseconds.
        ///
        ///
        /// This returns a count of interval since last call of this function.
        public int Interval {
            get {
                if (internalState == null) {
                    return 0;
                } else {
                    return internalState.GetInterval();
                }
            }
        }

        private State1 internalState;
    }
}
```

看看上面的代码你可以感觉到两种明显的Bad Smell。

首先，太多的if == null判断。熟悉模式的同志自然看出可以使用Null Object――不过还是按照Martin Fowler的习惯叫作Special Cases更好。

其次，sleeping这个标志位引发了太多的判断，造成了代码书写的凌乱。这个可以通过向State模式重构来解决。

此外的问题是很多例外的情况都没有做处理，比如连续Stop两次，会是什么情况？不过一旦完成了整个重构，这样的问题应该会迎刃而解。

重构的步骤在BDS 2006中可以分为下面几步：

1. 将涉及状态转换的几个函数参数列表修改。Start，Sleep，Wake，Stop都加上一个Stopwatch类型的参数，因为Stopwatch这个类在最后的State模式中将作为Context存在。此外为了统一起见，后面将四个状态转换操作统一命名为Start, Stop, Suspend, Resume。
1. 从已有的State类型中抽离出一个CustomState基类型。同时给Stopwatch和CustomState加上SetState函数。这个自然是State模式的一点要求了。
1. 创建一个继承于CustomState的Dead类型，作为Special Case。该类型仅仅在Start函数被调用时修改Context状态为State。同时在Dead类型下面的Value和Interval输出都设为0。
1. 将原来的State拆分为两个具体的状态，Working和Idle。根据就是sleeping标志。这样最后实现了下图所示的一个状态转换设计。

上面几步中比较复杂的就是第四步，因为Idle和Working两者的转换比较复杂。到底保存哪些信息可以很好的保存Working状态下面的数据到Idle中，怎么才能够很好的从Idle状态复原到Working状态。这都有些许的麻烦。

总体来说，重构到模式的确很方便，免去了开头就要一步设计到位的难度。虽然Stopwatch是一个很小的部件，但是看得出来想实现一些更加灵活的测量功能，没有合理的设计是比较复杂和容易出错的。

![img-description](/images/stopwatch-statemachine.png)
_Figure 1: Stopwatch state machine._

![img-description](/images/stopwatch-classes.png)
_Figure 2: Stopwatch classes._

重构的结果如上图，分为五个单元：

Stopwatch.cs
``` csharp
// lextm: this is stopwatch class.
// Copyright © 2006–2007 Lex Li
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111–1307

using System;

namespace Lextm.Diagnostics {

    ///
    /// Stopwatch class.
    ///
    public class Stopwatch {

        ///
        /// Constructor.
        ///
        public Stopwatch( ) {
            internalState = new Dead();
        }

        ///
        /// Starts the timing.
        ///
        /// If it is working, it will ignore other calls.
        public void Start( ) {
            internalState.Start(this);
        }

        ///
        /// Stops the timing.
        ///
        /// Once stopped, you have to it.
        ///
        public void Stop( ) {
            internalState.Stop(this);
        }

        ///
        /// Resumes a timing.
        ///
        ///
        public void Resume( ) {
            internalState.Resume(this);
        }

        ///
        /// Suspends timing.
        ///
        ///
        public void Suspend( ) {
            internalState.Suspend(this);
        }

        ///
        /// Count in milliseconds.
        ///
        /// This counts from the beginning of timing.
        ///
        public int Value {
            get {
                return internalState.GetValue();
            }
        }

        ///
        /// Interval in milliseconds.
        ///
        ///
        /// This returns a count of interval since last call of this function.
        public int Interval {
            get {
                return internalState.GetInterval();
            }
        }

        private Lextm.Diagnostics.CustomState internalState;

        internal void SetState( CustomState state ) {
            this.internalState = state;
        }
    }
}
```
CustomState.cs

``` csharp
// lextm: this is custom state class.
// Copyright © 2007 Lex Li
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111–1307

namespace Lextm.Diagnostics {

    ///
    /// Base class for stopwatch states.
    ///
    internal abstract class CustomState {

        public abstract int GetInterval( );

        public abstract void Suspend( Lextm.Diagnostics.Stopwatch context );

        public abstract void Resume( Lextm.Diagnostics.Stopwatch context );

        public abstract void Stop( Lextm.Diagnostics.Stopwatch context );

        public abstract void Start( Lextm.Diagnostics.Stopwatch context );

        public abstract int GetValue( );

        public static void SetState( Stopwatch context, CustomState state ) {
            context.SetState(state);
        }
    }
}
```

Dead.cs

``` csharp
// lextm: this is dead state class.
// Copyright © 2007 Lex Li
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111–1307

namespace Lextm.Diagnostics {

    ///
    /// The dead state.
    ///
    /// A stopwatch is in this state before and after
    /// . As a result , ,
    /// calls will be ignored.
    internal class Dead : CustomState {

        public override void Suspend( Lextm.Diagnostics.Stopwatch context ) {
        }

        public override void Resume( Lextm.Diagnostics.Stopwatch context ) {
        }

        public override void Stop( Lextm.Diagnostics.Stopwatch context ) {
        }

        public override int GetInterval( ) {
            return 0;
        }

        public override void Start( Lextm.Diagnostics.Stopwatch context ) {
            etState(context, new Working());
        }

        public override int GetValue( ) {
            return 0;
        }
    }
}
```

Working.cs

``` csharp
// lextm: this is working state class.
// Copyright © 2007 Lex Li
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111–1307

using System;

namespace Lextm.Diagnostics {

    ///
    /// The working state.
    ///
    /// and calls are ignored.
    internal class Working : CustomState {

        private readonly int lastTick;
        private int lastValueBeforeInterval;

        public override void Suspend( Lextm.Diagnostics.Stopwatch context ) {
            int valueBeforeSleep = Environment.TickCount - lastTick;
            int lastInterval = GetInterval();
            SetState(context, new Idle(valueBeforeSleep, lastInterval));
        }

        public override void Resume( Lextm.Diagnostics.Stopwatch context ) {
        }

        public override void Stop( Lextm.Diagnostics.Stopwatch context ) {
            SetState(context, new Dead());
        }

        public override int GetInterval( ) {
            int result = (Environment.TickCount - lastTick) - lastValueBeforeInterval;
            lastValueBeforeInterval = (Environment.TickCount - lastTick);
            return result;
        }

        public override void Start( Lextm.Diagnostics.Stopwatch context ) {}

        public override int GetValue( ) {
            return Environment.TickCount - lastTick;
        }

        public Working( ) :
            this(0, 0) {}

        public Working( int value ) :
            this(value, 0) {}

        public Working( int value, int interval ) {
            lastTick = Environment.TickCount - value;
            lastValueBeforeInterval = value - interval;
        }
    }
}
```

Idle.cs

``` csharp
// lextm: this is idle state class.
// Copyright © 2007 Lex Li
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111–1307

using System;

namespace Lextm.Diagnostics {

    ///
    /// The idle state.
    ///
    /// The stopwatch is in this state between and
    /// . So and calls
    /// are ignored.
    internal class Idle : CustomState {
        public override void Start( Stopwatch context ) {
        }

        public override void Stop( Stopwatch context ) {
            SetState(context, new Dead());
        }

        public override void Suspend( Stopwatch context ) {
        }

        public override void Resume( Stopwatch context ) {
            if (thisInterval == 0) {
                SetState(context, new Working(valueBeforeIdle));
            } else {
                SetState(context, new Working(valueBeforeIdle, intervalBeforeIdle));
            }
        }

        public override int GetValue( ) {
            return valueBeforeIdle;
        }

        public override int GetInterval( ) {
            int result = thisInterval;
            thisInterval -= thisInterval;
            return result;
        }

        private readonly int valueBeforeIdle;
        private readonly int intervalBeforeIdle;
        private int thisInterval;

        public Idle( int value, int interval ) {
            valueBeforeIdle = value;
            intervalBeforeIdle = interval;
            thisInterval = interval;
        }
    }
}
```
