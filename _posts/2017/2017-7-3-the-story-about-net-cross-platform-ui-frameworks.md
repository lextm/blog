---
categories: [Operating Systems]
description: A comprehensive analysis of .NET cross-platform UI frameworks for 2025, comparing native bindings, custom rendering approaches, and control mapping technologies like MAUI, Blazor Hybrid, Avalonia UI, and Uno Platform for modern desktop and mobile development.
excerpt_separator: <!--more-->
layout: post
permalink: /the-story-about-net-cross-platform-ui-frameworks-dd4a9433d0ea
tags: .net visual-studio open-source linux windows macos xamarin microsoft
title: The Story About .NET Cross Platform UI Frameworks
---
> Disclaimer: All contents are based on my personal observation. Please leave a comment if you find anything incorrect, and I will revise it often.
>
> Current version was revised on Oct 27, 2025.

The .NET ecosystem offers numerous UI frameworks for developing cross-platform GUI applications. This comprehensive guide examines the major frameworks available in 2025, analyzing their approaches, capabilities, and trade-offs to help you make an informed choice for your next project.

<!--more-->

## Inheritance Relationship Among Frameworks

Some relationships among these frameworks can be illustrated as below,

```d2
vars: {
  d2-config: {
    layout-engine: elk
  }
  colors: {
    win: "#ffe5e0"
    mac: "#ecc9ed"
    cross: "#e0f0ff"
    ms: "#0078d4"
  }

  d2-legend: {
    framework-a: {
      label: "Windows only"
      style: {
        fill: ${colors.win}
      }
    }
    framework-b: {
      label: "macOS only"
      style: {
        fill: ${colors.mac}
      }
    }
    framework-c: {
      label: "cross platform"
      style: {
        fill: ${colors.cross}
      }
    }
    framework-d: {
      label: "deprecated"
      style: {
        stroke-dash: 6
      }
    }

    framework-a -> framework-b: "successor"
    framework-a <-> framework-b: "API-compatible" {
      style.stroke: red
      style.stroke-dash: 4
    }
    framework-a -> framework-b: "backend provider" {
      style: {stroke-dash: 4}
      target-arrowhead.shape: circle
    }
    framework-a -> framework-b: "somehow related" {
      style: {stroke-dash: 4}
    }
  }
}
direction: down

WinForms: {
  label: "Windows Forms (Microsoft)"
  style: {
    fill: ${colors.win}
    stroke: ${colors.ms}
  }
}
WPF: {
  label: "WPF (Microsoft)"
  style: {
    fill: ${colors.win}
    stroke: ${colors.ms}
  }
}
UWP: {
  label: "UWP (Microsoft)"
  style: {
    fill: ${colors.win}
    stroke: ${colors.ms}
  }
}
WinUI: {
  label: "WinUI 3 (Microsoft)"
  style: {
    fill: ${colors.win}
    stroke: ${colors.ms}
  }
}
MonoMac: {
  label: "MonoMac (Mono)"
  style: {
    fill: ${colors.mac}
    stroke-dash: 6
  }
}
DotNet_macOS: {
  label: ".NET for macOS (Microsoft)"
  style: {
    fill: ${colors.mac}
  }
}
Silverlight: {
  label: "Silverlight (Microsoft)"
  style: {
    fill: ${colors.cross}
    stroke: ${colors.ms}
    stroke-dash: 6
  }
}
Moonlight: {
  label: "Moonlight (Mono)"
  style: {
    fill: ${colors.cross}
    stroke-dash: 6
  }
}
OpenSilver: {
  label: "OpenSilver (OSS)"
  style: {
    fill: ${colors.cross}
  }
}
Avalonia_UI: {
  label: "Avalonia UI (Avalonia)"
  style: {
    fill: ${colors.cross}
  }
}
Avalonia_XPF: {
  label: "Avalonia XPF (Avalonia)"
  style: {
    fill: ${colors.cross}
  }
}
Uno: {
  label: "Uno Platform (Uno)"
  style: {
    fill: ${colors.cross}
  }
}
Xamarin_Forms: {
  label: "Xamarin.Forms (Microsoft)"
  style: {
    fill: ${colors.cross}
    stroke: ${colors.ms}
    stroke-dash: 6
  }
}
MAUI: {
  label: ".NET MAUI (Microsoft)"
  style: {
    fill: ${colors.cross}
    stroke: ${colors.ms}
  }
}
Blazor: {
  label: "Blazor (Microsoft)"
  style: {
    fill: ${colors.cross}
    stroke: ${colors.ms}
  }
}
MAUI_Blazor: {
  label: "MAUI Blazor Hybrid (Microsoft)"
  style: {
    fill: ${colors.cross}
    stroke: ${colors.ms}
  }
}
XWT: {
  label: "xwt (Mono)"
  style: {
    fill: ${colors.cross}
    stroke-dash: 6
  }
}
Eto_Forms: {
  label: "Eto.Forms (OSS)"
  style: {
    fill: ${colors.cross}
  }
}
GTK: {
  label: "GTK# (OSS)"
  style: {
    fill: ${colors.cross}
  }
}

WPF -> Avalonia_UI: "inspired approach" {
  style: {stroke-dash: 4}
}
WPF -> Silverlight: "derived subset" {
  style: {stroke-dash: 4}
}
Silverlight <-> Moonlight: {
  style.stroke: red
  style.stroke-dash: 4
}
Silverlight -> OpenSilver
Moonlight -> OpenSilver
WPF -> UWP: "inspired approach" {
  style: {stroke-dash: 4}
}
UWP -> WinUI
WinUI <-> Uno: {
  style: {
    stroke: red
    stroke-dash: 4
  }
}
WPF -> Avalonia_XPF
Avalonia_UI <-> Avalonia_XPF: "shared rendering engine" {
  style: {
    stroke: orange
    stroke-dash: 4
  }
}
WinUI -> MAUI: {
  style: {stroke-dash: 6}
  target-arrowhead.shape: circle
}
Xamarin_Forms -> MAUI
MAUI -> MAUI_Blazor: "hosting" {
  style: {stroke-dash: 4}
}
Blazor -> MAUI_Blazor: "embedded" {
  style: {stroke-dash: 4}
}
XWT -> Xamarin_Forms: "inspired approach" {
  style: {stroke-dash: 4}
}
WinForms -> Eto_Forms: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
WPF -> Eto_Forms: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
WPF -> XWT: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
WPF -> Xamarin_Forms: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
MonoMac -> DotNet_macOS
MonoMac -> XWT: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
MonoMac -> Xamarin_Forms: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
MonoMac -> Eto_Forms: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
DotNet_macOS -> Eto_Forms: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
GTK -> Xamarin_Forms: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
GTK -> Eto_Forms: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
GTK -> MAUI: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
GTK -> XWT: {
  style: {stroke-dash: 4}
  target-arrowhead.shape: circle
}
```
Figure 1: Inheritance Relationships Among .NET UI Frameworks.

## Native Bindings

In modern .NET development, we can create cross-platform applications using C# while easily sharing non-UI code through .NET Standard and .NET Core libraries. The native bindings approach has historically been considered optimal, as it allows applications to leverage platform-specific controls and third-party libraries to achieve full OS integration.

> By saying "full OS integration", I mean our apps have full access to system standard controls, such as buttons, check boxes and so on. More examples are,
>
> - Windows system tray
> - Windows jump lists
> - Windows system themes
> - iOS native scrolling
>
> Most importantly, other apps on the same OS are written using the same set of controls, which allows our apps to blend in naturally, instead of being aliens.
>
> Some app types, such as full screen games, are usually aliens everywhere and people get used to that fact. However, not all apps should go that route.

Below are the native UI frameworks for C# developers,

- Windows: Windows Forms (note 1).
- macOS: Xamarin.Mac (wrapper over Cocoa) (note 2).
- Linux: GTK# (wrapper over GTK+) (note 3).
- iOS: Xamarin.iOS (wrapper over Cocoa Touch).
- Android: Xamarin.Android (wrapper over Android UI).

> A few notes,
>
> Note 1: Windows is a monster that has multiple UI frameworks. Here I only list WinForms as "native". WPF and UWP are actually supported frameworks by Microsoft. Many Windows 10 built-in apps are now written in UWP. So UWP is becoming the next native framework.
>
> Note 2 MonoMac is obsolete.
>
> QtSharp is considered not mature enough.

Most projects choose to use this approach, such as

- [NI LabView](https://www.ni.com/en/shop/labview.html) uses Xamarin.iOS on iOS, and Windows Forms (not quite sure) on Windows.
- [Plastic SCM](https://www.plasticscm.com/) once used GTK# on Linux, Xamarin.Mac on macOS, and Windows Forms on Windows before migrating to Avalonia in February 2022, exemplifying the shift toward unified cross-platform frameworks.
- [iCircuit](https://icircuitapp.com/) uses Xamarin.Mac on macOS, Xamarin.iOS on iOS, Xamarin.Android on Android, and native Windows technologies for Windows platforms.

## Cross Platform Frameworks

Despite the advantages of native bindings, many developers seek true cross-platform UI frameworks that reduce code duplication and simplify maintenance. This article examines the various approaches that have emerged, which can be categorized into three main strategies:

- **Full custom rendering**: Frameworks that draw their own UI elements and emulate native controls.
- **Hybrid platforms**: Frameworks that are native on some platforms while emulating controls on others.
- **Native control mapping**: Frameworks that dynamically map to the appropriate native controls on each platform.

### Unity/MonoGame

|                         | Comment                                           |
| :---------------------- | :------------------------------------------------ |
| Approach                | Full custom rendering.                            |
| Supported Platforms     | Desktop and mobile (and more, like game consoles) |
| OS Native Look and Feel | Almost none.                                      |
| Third Party Controls    | Some                                              |

If you're comfortable with fully rendering your own controls, frameworks like Unity and MonoGame offer extensive cross-platform support, including desktop, mobile, web, and even game consoles.

While this approach excels for games and specialized applications, it has limitations for traditional business software where users expect platform-consistent interfaces. Applications built this way won't have the native look and feel since they can't access the operating system's native control system.

> Third-party solutions such as [noesisGUI](https://noesisengine.com/) enhance these frameworks by providing XAML-based UI capabilities and controls, offering a more structured approach to UI development while maintaining cross-platform compatibility.

### GTK#

|                         | Comment                                           |
| ----------------------- | ------------------------------------------------- |
| Approach                | Native on Linux, emulating on others.             |
| Supported Platforms     | Desktop and mobile (and more, like game consoles) |
| OS Native Look and Feel | Linux only.                                       |
| Third Party Controls    | Not too many.                                     |

GTK has been a portable framework to build desktop apps. Thus, its C# binding GTK# enables cross platform apps.

However, GTK# applications only truly look and feel native on Linux distributions. When running on macOS or Windows, these applications often appear visually inconsistent with platform conventions and don't integrate seamlessly with system themes. Furthermore, GTK# has significant limitations for mobile development, making it an impractical choice for applications targeting iOS or Android.

> MonoDevelop used GTK# on all platforms initially, and gradually (in Xamarin Studio phase) started to utilize xwt to render some components with native controls. Thus, its successor Visual Studio for Mac inherited both GTK# and Xamarin.Mac bits. Before its end-of-life, Microsoft was able to port Visual Studio for Mac fully to Xamarin.Mac, which was a great achievement.

Mono's GTK# wrapper is GTK 2 compatible and not yet upgraded to support GTK 3. To explore the full potential of GTK 3, you need to use the NuGet package from [a new repo](https://github.com/GtkSharp/GtkSharp) created by a MonoGame maintainer Harry which fills the gaps.

In recent years, the .NET community has also made progress on GTK 4 integration. The [gir.core project](https://github.com/gircore/gir.core) now provides .NET bindings for GTK 4, enabling developers to build modern Linux desktop applications with the latest GTK features. While GTK 4 .NET integration is still maturing and the ecosystem is smaller than for other frameworks, it is a promising option for those targeting Linux-first or Linux-only scenarios.

### Windows Forms

|                         | Comment                                 |
| ----------------------- | --------------------------------------- |
| Approach                | Native on Windows, emulating on others. |
| Supported Platforms     | Desktop                                 |
| OS Native Look and Feel | Windows only.                           |
| Third Party Controls    | Many on Windows.                        |

Windows Forms works for Windows (including Windows CE, though no serious interest on that now). Mono has a clone of Windows Forms, and some projects used that to port .NET Framework Windows Forms apps to macOS and Linux. So, it sounds like a cross platform framework candidate.

However, Mono's implementation is buggy and requires significant effort to improve. As a result, some projects (such as [Plastic SCM](https://blog.plasticscm.com/2014/12/native-linux-gui-gtkplastic.html)) initially took this approach but later moved to more modern frameworks.

What's more, Mono's initial WinForms implementation on macOS uses some legacy interfaces like Carbon and is 32 bit only. So, when recent macOS releases deprecated/removed those APIs and no longer supports 32 bit applications, this approach becomes a dead end. [There was an attempt](https://github.com/mono/mono/pull/7100) to port Mono WinForms on macOS to 64 bit, but no further news from there.

[Microsoft decided in 2017](https://github.com/dotnet/corefx/issues/20325) to port `System.Drawing` to non-Windows platforms, which gives an opportunity to also [port Windows Forms officially to non-Windows platforms](https://github.com/dotnet/corefx/issues/21803). It would be welcome if that port becomes a better alternative than Mono's implementation, but whether third parties (commercial/open source) can catch up is uncertain. Third party controls are fantastic on Windows, but rarely they support other OS. Developers usually find it pretty painful to move Windows Forms apps to non-Windows platforms due to such controls they use.

More importantly the design of Windows Forms is suitable for desktop apps, but may be not for mobile platforms (personal opinion clearly). Xamarin guys initially had [an idea to port Windows Forms to iOS](https://tirania.org/blog/archive/2009/Sep-14.html). They gave that up and instead decided to bind natively to Cocoa Touch.

Microsoft started to support Windows Forms on .NET Core 3.0. Officially Microsoft made it available on Windows, and we didn't see anyone seriously ported it to other systems.

During .NET 6 development, Microsoft decided to stop supporting `System.Drawing` on non-Windows platform, due to the poor maintenance status of `libgtkplus`, and Windows Forms on .NET Core/.NET is now doomed to be Windows only.

At least Windows Forms is not considered a cross-platform option by Microsoft, and its future for non-Windows platforms is uncertain. However, there is renewed hope for cross-platform Windows Forms: the Mono implementation is now maintained by the WineHQ team, and the very first new Mono release ([6.14.0](https://gitlab.winehq.org/mono/mono/-/releases/mono-6.14.0)) already included updates and fixes for Windows Forms. This collaboration may bring further improvements for running Windows Forms apps on Linux and macOS in the future.

### WPF/UWP/WinUI

|                         | Comment                       |
| ----------------------- | ----------------------------- |
| Approach                | Full Custom Rendering.        |
| Supported Platforms     | Desktop (and possibly mobile) |
| OS Native Look and Feel | Windows only.                 |
| Third Party Controls    | Many on Windows.              |

Similar to Unity/MonoGame, WPF internally renders everything on its own, so technically speaking it can go cross platform.

> Delphi has a similar framework called FireMonkey, which is already cross platform (both desktop and mobile).

However, this approach has the same disadvantages as Unity/MonoGame: controls do not render like native ones, and the user experience can feel less integrated with the host OS.

> Microsoft does ship many themes for WPF apps to look quite good with Windows, but still in certain area the look and feel differs.
>
> FireMonkey met such issues and its developers have tried to resolve that for a long time.
>
> Again (personal opinion) Windows apps should move gradually from Windows Forms/WPF to UWP/WinUI if required. So in the near future, WinUI 3 would become the "native" solution on Windows.

Microsoft started to support WPF on .NET Core 3.0. Officially Microsoft only made it available on Windows, but anyone can attempt to port to other systems.

Mono was trying to port WPF, but that project was not finished due to [lack of resources](https://www.mono-project.com/docs/gui/wpf/). The Mono documentation explains:

> "Windows Presentation Foundation is a complicated beast. Unlike Windows Forms which is a thin wrapper over the native Win32 toolkit, WPF is a complete toolkit and rendering system based on DirectX. Porting WPF to other platforms would be a major effort because there isn't a proper DirectX implementation on Mac or Linux."

While UWP is a closed platform, [WinUI 3 has been open sourced gradually and will be fully available on GitHub](https://github.com/microsoft/microsoft-ui-xaml/discussions/10700). However, porting WinUI 3 itself to non-Windows platforms remains a significant challenge due to its deep integration with Windows-specific technologies, so a compatible solution like Uno Platform is a better choice for cross-platform development.

### Avalonia UI and Avalonia XPF

|                         | Comment                                           |
| ----------------------- | ------------------------------------------------- |
| Approach                | Custom rendering with XAML-based architecture     |
| Supported Platforms     | Windows, macOS, Linux, iOS, Android, WebAssembly  |
| OS Native Look and Feel | Consistent custom UI with platform adaptations    |
| Third Party Controls    | Growing commercial and community ecosystem         |

[Avalonia UI](https://github.com/AvaloniaUI/Avalonia) has emerged as one of the leading cross-platform UI frameworks in the .NET ecosystem. While not a strict WPF clone, it offers a familiar XAML-based approach that has attracted significant community adoption and commercial interest.

As of 2025, Avalonia UI has matured into a production-ready solution for developing sophisticated desktop applications targeting Windows, macOS, and Linux, with expanding support for mobile platforms. The framework fully supports .NET 8, provides a robust designer experience, and is backed by an expanding ecosystem of controls and tools. Key strengths include:

- Modern XAML-based architecture with reactive programming support
- Flexible styling system inspired by CSS
- Strong community and commercial backing, including support from JetBrains and Devolutions
- Growing ecosystem of third-party controls and extensions
- Support for multiple design patterns (MVVM, ReactiveUI, etc.)
- A healthy revenue structure

Major technology companies have recognized Avalonia's potential, with JetBrains notably deploying it in significant products like Rider. Today, Avalonia UI stands alongside Uno Platform as a premier .NET cross-platform UI framework, with both solutions considered equally viable options for sophisticated applications extending beyond the Windows ecosystem.

#### Avalonia's Business Model and Sustainability

The Avalonia team has strategically diversified their offerings to ensure long-term sustainability while maintaining their commitment to the open-source community. Their business model includes:

1. **Core Framework (Open Source)**: The main Avalonia UI framework remains fully open source under the MIT license.

2. **[Avalonia XPF](https://avaloniaui.net/XPF) (Commercial)**: A specialized commercial product that delivers enhanced WPF compatibility for teams migrating existing applications. As described on their website:

   > "Avalonia XPF empowers developers to bring their WPF applications to the macOS platform with minimal changes required, ensuring that your WPF applications can now enjoy a wider audience. This development marks a significant milestone, heralding a new era of versatility and accessibility for WPF developers committed to broadening the reach of their software."

3. **[Avalonia Accelerate](https://avaloniaui.net/accelerate) (Subscription)**: A tiered subscription service providing additional tools, controls, and support. As the Avalonia team explains:

   > "When you purchase Accelerate, you're doing more than unlocking powerful tools. You're directly supporting the continued development of Avalonia itself. Every purchase helps us to fund new features, enhancements, and long-term innovation, ensuring that Avalonia stays the leading cross-platform UI framework for .NET developers."

Noticeable changes recently included:

- Changes of Avalonia XPF's pricing model have significantly lowered the adoption barrier. After initially launching with a higher price point focused on enterprise customers, the vendor has introduced more flexible licensing options and reduced entry-level pricing tiers in 2025. These changes make the commercial products more accessible to smaller teams and organizations.
- The potential of shipping foundational components like Wayland backend with AGPL/commercial dual licensing has been hinted in its team blog, but no concrete plans have been announced yet. This could open new revenue streams while maintaining open-source accessibility, but also impact on some users that prefer fully permissive licenses.
- The discontinuation of Avalonia Accelerate Indie tier and the introduction of Community tier reflect an ongoing effort to balance community support with sustainable funding.
- The uncertainty around VS Code extension reveals that for a small team, the balance between different audiences (VS, Rider, VS Code) is challenging.

Developers and businesses should carefully evaluate both the technical merits and business model when considering Avalonia for long-term projects, or evaluate alternative frameworks like Uno Platform/OpenSilver that choose a different path.

### Xamarin.Forms/MAUI

|                         | Comment                 |
| ----------------------- | ----------------------- |
| Approach                | Native control mapping. |
| Supported Platforms     | Mobile and desktop.     |
| OS Native Look and Feel | Always.                 |
| Third Party Controls    | Growing.                |

Xamarin.Forms was originally created for mobile platforms, but has since expanded to support desktop targets such as macOS, WPF, and GTK# backends.

Unlike Unity/MonoGame/WPF/Avalonia who performs custom rendering and emulates OS controls, Xamarin.Forms apps pick up native controls at startup, so all you see is purely native. This kind of UI element mapping makes sure your apps are not different from any other apps written natively.

More importantly, Xamarin.Forms also gives you flexibility to embed native controls whenever necessary, and its pages can also be embedded into native apps. So hopefully it is the most flexible option for you.

While Xamarin.Forms was initially designed for mobile apps, it has matured to support many desktop scenarios. However, for complex desktop applications like Office or Visual Studio, other frameworks may be a better fit. For most business and line-of-business apps, Xamarin.Forms remains a flexible and productive choice.

Quite a lot of third party vendors are now offering Xamarin.Forms controls, so that you can build Line-of-Business apps efficiently,

- [ComponentOne](https://www.componentone.com/Xamarin/)
- [Telerik](https://www.telerik.com/xamarin-ui)
- [Synfusion](https://www.syncfusion.com/products/xamarin)
- [Infragistics](https://www.infragistics.com/products/xamarin-forms)
- [DevExpress](https://www.devexpress.com/products/xamarin/)

Microsoft announced [MAUI](https://devblogs.microsoft.com/dotnet/introducing-net-multi-platform-app-ui/), a major upgrade of Xamarin.Forms, as a new option to build cross platform applications. However, due to the pandemic, its delivery was delayed several times. You can play with it on .NET 6/7 and above.

While MAUI has many differences from Xamarin.Forms, the most significant is that

- On macOS its backend is iOS Catalyst (not Xamarin.Mac), which is the officially recommended way to build macOS apps using iOS codebase.
- On Windows its backend is WinUI 3 (not WPF), which is the officially recommended way to build Windows apps using modern UI framework.

### MAUI Blazor Hybrid

|                         | Comment                                                      |
| ----------------------- | ------------------------------------------------------------ |
| Approach                | Hybrid: Web-based UI rendered in a native app container.     |
| Supported Platforms     | Desktop and mobile (via .NET MAUI).                          |
| OS Native Look and Feel | Partial (depends on host and integration).                   |
| Third Party Controls    | Growing ecosystem.                                           |

MAUI Blazor Hybrid allows you to build cross-platform desktop and mobile applications using Blazor components rendered inside a native WebView, hosted by .NET MAUI. This approach enables developers to reuse web UI logic and components while still accessing native device APIs and features through .NET MAUI.

MAUI Blazor Hybrid enables code sharing between desktop, mobile, and web applications using C# and Razor components. It leverages modern web development patterns and tooling while providing access to native device features through the .NET MAUI APIs. The growing ecosystem includes third-party UI component libraries from major vendors like Telerik, Syncfusion, and DevExpress.

However, since the UI is rendered in a WebView, it's not truly native, which can affect the look and feel on different platforms. Performance and resource usage may differ from fully native frameworks, especially for graphics-intensive scenarios. Additionally, achieving platform-specific UI nuances may require extra configuration and customization.

MAUI Blazor Hybrid works well for teams looking to maximize code reuse across different platforms, especially when web skills and assets are already available. While it might not be ideal for applications requiring deep OS integration, it offers a good balance of productivity and reach for many business applications.

> MAUI Blazor Hybrid shares conceptual similarities with React Native, as both frameworks aim to simplify cross-platform development. While their technical approaches differ, they both address the challenge of building applications that run consistently across multiple platforms.

### Uno Platform

|                         | Comment                                               |
| ----------------------- | ----------------------------------------------------- |
| Approach                | WinUI/UWP APIs with native rendering and custom Skia  |
| Supported Platforms     | Windows, iOS, Android, macOS, Linux, WebAssembly      |
| OS Native Look and Feel | Platform-adaptive with consistent cross-platform UX   |
| Third Party Controls    | Robust ecosystem with major vendor support            |

Uno Platform has solidified its position as a leading cross-platform UI solution for .NET developers. It enables the creation of single-codebase applications across multiple platforms using familiar WinUI/UWP APIs and XAML. By 2025, Uno Platform has achieved several significant milestones:

- Full support for .NET 8 and above with optimized performance across all platforms
- Comprehensive WebAssembly optimizations for web applications
- Strengthened collaboration with Microsoft, giving it semi-official status in the .NET ecosystem
- Widespread enterprise adoption for applications requiring consistent experiences across web, desktop, and mobile
- Strong tooling support with advanced Hot Reload and Hot Design capabilities integrated into major IDEs
- [Official collaboration with Microsoft on .NET/MAUI tooling](https://platform.uno/blog/announcing-unoplatform-microsoft-dotnet-collaboration/) and ecosystem development announced during .NET 10 timeframe

#### Technical Approach and Architecture

Uno Platform takes a unique approach to cross-platform development:

1. **WinUI/UWP Foundation**: Uno chose UWP/WinUI as its starting point, so all basic APIs mirror what Microsoft offers, making it easy for Windows developers to transition.

2. **Multiple Rendering Options**:
   - Native controls on supported platforms
   - Custom Skia-based rendering for pixel-perfect consistency
   - WebAssembly implementation for web applications

3. **Complete XAML Support**: Unlike some other frameworks that implement partial XAML support, Uno provides comprehensive XAML capabilities.

> Uno supports fully custom rendering upon Skia in its latest release, giving developers more flexibility in creating consistent UIs across platforms.

The Uno team has significantly improved developer productivity through advanced tooling that includes sophisticated Hot Reload capabilities, enhanced XAML editing experiences, and deep integration with major IDEs including Visual Studio, JetBrains Rider, and Visual Studio Code. The [Uno Platform Studio](https://platform.uno/studio/) with Hot Design is one step further and offers a visual designer that streamlines UI development and accelerates the design-to-code workflow. Integration with designer tools like Figma further enhances the application development experience.

#### Ecosystem and Industry Support

Since Microsoft Ignite 2019, when the Microsoft WinUI team [embraced Uno as their recommended cross-platform approach](https://blogs.windows.com/windowsdeveloper/2019/11/04/developer-platform-updates-at-microsoft-ignite-2019/), the framework has gained significant industry support. Major third-party control vendors including Syncfusion (who announced [collaboration](https://www.syncfusion.com/blogs/post/collaboration-syncfusion-uno-platform.aspx) in September 2019), Telerik, and DevExpress now offer comprehensive control libraries for Uno Platform.

#### Business Model and Sustainability

While Uno Platform maintains its core as open source under the Apache 2.0 license, it has developed a sustainable business model through strategic commercial offerings:

1. **Open Source Core**: The main framework remains freely available and open source, ensuring community access and contributions.

2. **Commercial Components**: The team offers premium tools such as the Uno Platform Studio with Hot Design (their visual designer).

3. **Professional Support**: Enterprise customers can access various subscription tiers that include priority support, consulting services, and additional tools ([platform.uno/select-subscription](https://platform.uno/select-subscription/)).

This balanced approach allows the team to fund continued development while keeping the main framework accessible to the broader developer community.

Today, Uno Platform and Avalonia UI represent the two preeminent .NET cross-platform UI frameworks, each offering distinct advantages while maintaining robust community support and active development. Uno's strong alignment with Microsoft's WinUI strategy gives it a particular advantage for teams with existing UWP/WinUI expertise or applications.

### xwt/Eto.Forms

|                         | Comment                        |
| ----------------------- | ------------------------------ |
| Approach                | Native control mapping.        |
| Supported Platforms     | Desktop (and possibly mobile). |
| OS Native Look and Feel | Always.                        |
| Third Party Controls    | Not many.                      |

Both are desktop UI frameworks using Xamarin.Forms approach (native control mapping).

xwt is a mature project and may have inspired the design of Xamarin.Forms. Eto.Forms is newer and has recently started to support mobile platforms.

As of 2025, the two projects have taken divergent paths. The mono/xwt project has seen minimal development activity in recent years, with its assembly versions still marked as "0.1.0.0-prerelease". Meanwhile, Eto.Forms continues active development with a small but dedicated community, powering applications like the MonoGame Pipeline Tool and maintaining integrations with modern technologies such as SkiaSharp. Eto.Forms has a growing ecosystem of third-party libraries and controls, making it a viable option for certain specialized desktop applications. Neither framework has achieved the level of ecosystem maturity, corporate backing, or community adoption of frameworks like MAUI, Avalonia, or Uno Platform, but Eto.Forms remains an option worth considering for cross-platform desktop development.

> **Some Incomplete Information on Qt**
>
> I don't do much Qt programming, so my knowledge of this cross platform framework is limited.
>
> It is also not quite well supported on .NET/Mono due to the following challenges,
>
> - Its API is C++ based so very hard to wrap in C#/.NET. That's why libraries such as QtSharp cannot map all the functionality.
> - I cannot comment much on its rendering effect, but it seems to use custom rendering.
> - Interestingly that Qt guys do develop their own markup language called QML.
> - You might use QtSharp to develop a Qt app, and a new project called [Qml.Net](https://github.com/pauldotknopf/Qml.Net) is another option.

## Electron Related Solutions

The landscape of web technologies for desktop development has evolved significantly. Electron continues to power many successful cross-platform applications (VS Code, Azure Data Studio, etc.), and combining it with Blazor has become a viable approach for .NET developers.

Several options now exist for this integration:

- [Electron.NET](https://github.com/ElectronNET/Electron.NET) remains an active community project providing robust Electron integration
- [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/) with Blazor provides a lighter alternative to Electron for Windows-focused applications
- [BlazorHybrid.Electron](https://github.com/BinaryBrockSoftware/BlazorHybrid.Electron) offers another approach to Electron integration

These approaches allow .NET developers to leverage web UI technologies while still accessing native platform capabilities, offering an excellent balance of cross-platform reach and native functionality for many application types.

## Final Thoughts

The .NET cross-platform UI landscape continues to evolve in 2025, presenting developers with several approaches to consider:

- **Native bindings** provide excellent platform integration and performance
- **MAUI** offer native control mapping with growing ecosystem support
- **MAUI Blazor Hybrid** combines web technologies with native capabilities
- **Avalonia UI & Uno Platform** present robust options for desktop/mobile/web cross-platform development

Framework selection might depend on factors like your team's expertise, target platforms, UI requirements, and long-term goals. Each option has its own advantages and considerations worth exploring.

> Looking for other interesting posts like this one? You can visit [the index page]({% post_url 2017/2017-11-2-all-in-one-for-the-legends-of-net-materials %}) or explore all posts tagged [.NET](/tags/net/).
