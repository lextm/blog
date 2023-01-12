---
layout: post
title: "PowerShell with Oh My Posh as Default Shell on macOS"
description: A post about how to configure PowerShell with Oh My Posh as your preferred shell on macOS
tags: PowerShell macOS Visual-Studio-Code
excerpt_separator: <!--more-->
---

While I am using more and more macOS and PowerShell, the need of enriching the look-and-feel starts to reveal. So in this post, I will show you how to properly configure PowerShell with Oh My Posh as your default shell on macOS.

![img-description](/images/pwsh-mac.png)
_Figure 1: PowerShell on macOS_

<!--more-->
## Install PowerShell
I won't waste too much time here, as Microsoft already has [an excellent article](https://docs.microsoft.com/powershell/scripting/install/installing-powershell-on-macos) with popular options. Personally I used Homebrew,

``` sh
brew install --cask powershell
```

Now at terminal check where PowerShell is installed to,

``` sh
whereis pwsh
```

On my machine, the output is `/usr/local/bin/pwsh`. We will use this value later.

## Enable Homebrew in PowerShell
Make sure you have `~/.config/powershell/profile.ps1` created, and it contains a line similar to,

``` powershell
$(/opt/homebrew/bin/brew shellenv) | Invoke-Expression
```

> Your machine might require a path other than `/opt/homebrew/bin/brew`. Learn the right path to use from the output of `brew install --cask powershell`.

## Install iTerm2
Oh My Posh requires a modern terminal (that supports Nerd Fonts), so we need to install iTerm2 now,

``` sh
brew install --cask iterm2
```

## Install Nerd Fonts
Oh My Posh themes usually require [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) to render its effects, so here we install Meslo Nerd Font

``` sh
brew tap homebrew/cask-fonts && brew install --cask font-meslo-lg-nerd-font
```

> In case you prefer another font, search its installation command from here,
> {% gist davidteren/898f2dcccd42d9f8680ec69a3a5d350e %}

## Add PowerShell Profile in iTerm2
Now we can open iTerm2 and its Preferences.

Under Profiles, create a new Profile called PowerShell.

For this profile, set its Command as `/usr/local/bin/pwsh -l -nol`.

> `-nol` suppresses the copyright banner.
>
> `-l` loads the login profiles (including environment variables). Without this many commands might not be found (such as `code` for VS Code).
>
> More on pwsh arguments can be found in [this article](https://docs.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh).

![img-description](/images/iterm2-general.png)
_Figure 2: iTerm2 General section_

Under Text section, choose MesloLGM Nerd Font Mono.

![img-description](/images/iterm2-text.png)
_Figure 3: iTerm2 Text section_

Use "Set as Default" menu item from "Other Actions" dropdown to set PowerShell as default profile.

## Install Oh My Posh
With Homebrew, the installation is still simple,

``` sh
brew install jandedobbeleer/oh-my-posh/oh-my-posh
```

Learn the installation path of Oh My Posh via,

``` sh
brew --prefix oh-my-posh
```

Once installation finishes, open `~/.config/powershell/profile.ps1` and add another line,

``` powershell
oh-my-posh init pwsh --config /opt/homebrew/opt/oh-my-posh/themes/cloud-native-azure.omp.json | Invoke-Expression
```

![img-description](/images/pwsh-profile.png)
_Figure 4: PowerShell default profile_

Now open a new tab in iTerm2 and you should see your PowerShell prompt with cloud-native-azure theme.

In case you want to preview different themes quickly, run

``` powershell
Get-PoshThemes /opt/homebrew/opt/oh-my-posh/themes
```

![img-description](/images/ohmyposh-themes.png)
_Figure 5: Oh My Posh themes_

## Visual Studio Code Terminal
If you plan to set PowerShell as default shell in VS Code terminal, make sure that you use the following settings,

``` json
{
    "terminal.external.osxExec": "iTerm.app",
    "terminal.integrated.fontFamily": "MesloLGM Nerd Font Mono"
}
```

## Side Notes
Now you can keep iTerm2 in Dock and easily open a terminal with PowerShell for everyday usage, instead of the default Terminal.

To learn Oh My Posh on Windows, you can always trust [Scott Hanselman](https://www.hanselman.com/blog/my-ultimate-powershell-prompt-with-oh-my-posh-and-the-windows-terminal).
