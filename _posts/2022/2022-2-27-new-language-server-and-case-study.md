---
layout: post
title: New Language Server and Case Study
description: A post about the new Esbonio language server and how to troubleshoot issues with it
tags: Visual-Studio-Code
excerpt_separator: <!--more-->
---

It was around the year end of 2020 that I noticed the existence of the Snooty language server from MongoDB and [integrated it with the reStructuredText extension for VSCode]({% post_url 2020/2020-12-18-integration-with-snooty-language-server %}). After about a year, it's time to move to another language server in this field.

<!--more-->

## Limitation of Snooty

While Snooty is a nice language server, it has several things that bother me often.

First, as a MongoDB internal project, its priority is always the internal users and internal features. So many of the issues reported by outside users are not resolved in a timely manner.

Second, its issue tracker is internal so even I have no idea what the guys are working on.

Third, it is pretty large a program with performance cost.

## Esbonio History

The new language server is called Esbonio, and created by Alex Carney. Compared to Snooty, it uses a different approach and features a few important parts,

- Good focus on IntelliSense
- Tight integration with Sphinx to generate HTML pages on the fly
- Lightweight
- High test coverage and stable

It was launched in August 2020 and has been improved significantly in 2021.

As a result, starting from release 170.0.0, the reStructuredText extension for VSCode moved to Esbonio language server.

## Case Study

If you just install this extension and would like to work on a ReadTheDocs project, you might notice an error saying "Unable to initialize Sphinx, see output window for details", so here I try to reveal how to troubleshoot and learn the cause.

> Note that with this error in place, features like live preview stop working, because now live preview relies Esbonio to work.

First, this error asks you to open VSCode OUTPUT panel. And there you should switch to Esbonio Language Client channel. You should see something similar to below,

``` text
[esbonio.lsp] Workspace root file:///c%3A/Users/lextudio/source/repos/vscode-restructuredtext/test-resources/sphinx
[esbonio.lsp] Sphinx Config {'version': None, 'conf_dir': 'c:\\Users\\lextudio\\source\\repos\\vscode-restructuredtext\\test-resources\\sphinx', 'src_dir': 'c:\\Users\\lextudio\\source\\repos\\vscode-restructuredtext\\test-resources\\sphinx', 'build_dir': 'c:\\Users\\lextudio\\source\\repos\\vscode-restructuredtext\\test-resources\\sphinx\\_build', 'builder_name': 'html'}
[esbonio.lsp] Config dir c:\Users\lextudio\source\repos\vscode-restructuredtext\test-resources\sphinx
[esbonio.lsp] Src dir c:\Users\lextudio\source\repos\vscode-restructuredtext\test-resources\sphinx
[esbonio.lsp] Build dir c:\Users\lextudio\source\repos\vscode-restructuredtext\test-resources\sphinx\_build\html
[esbonio.lsp] Doctree dir c:\Users\lextudio\source\repos\vscode-restructuredtext\test-resources\sphinx\_build\doctrees
[esbonio.lsp] Traceback (most recent call last):
  File "C:\Users\lextudio\AppData\Local\Programs\Python\Python310\lib\site-packages\sphinx\config.py", line 340, in eval_config_file
    exec(code, namespace)
  File "c:\Users\lextudio\source\repos\vscode-restructuredtext\test-resources\sphinx\conf.py", line 127, in <module>
    import sphinx_rtd_theme
ModuleNotFoundError: No module named 'sphinx_rtd_theme'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\lextudio\AppData\Local\Programs\Python\Python310\lib\site-packages\esbonio\lsp\sphinx.py", line 233, in _initialize_sphinx
    return self.create_sphinx_app(self.user_config)
  File "C:\Users\lextudio\AppData\Local\Programs\Python\Python310\lib\site-packages\esbonio\lsp\sphinx.py", line 328, in create_sphinx_app
    app = Sphinx(
  File "C:\Users\lextudio\AppData\Local\Programs\Python\Python310\lib\site-packages\sphinx\application.py", line 209, in __init__
    self.config = Config.read(self.confdir, confoverrides or {}, self.tags)
  File "C:\Users\lextudio\AppData\Local\Programs\Python\Python310\lib\site-packages\sphinx\config.py", line 173, in read
    namespace = eval_config_file(filename, tags)
  File "C:\Users\lextudio\AppData\Local\Programs\Python\Python310\lib\site-packages\sphinx\config.py", line 353, in eval_config_file
    raise ConfigError(msg % traceback.format_exc()) from exc
sphinx.errors.ConfigError: There is a programmable error in your configuration file:

Traceback (most recent call last):
  File "C:\Users\lextudio\AppData\Local\Programs\Python\Python310\lib\site-packages\sphinx\config.py", line 340, in eval_config_file
    exec(code, namespace)
  File "c:\Users\lextudio\source\repos\vscode-restructuredtext\test-resources\sphinx\conf.py", line 127, in <module>
    import sphinx_rtd_theme
ModuleNotFoundError: No module named 'sphinx_rtd_theme'
```

The first few lines indicate what settings (like build folder) are passed from VSCode to the language server. The last few lines indicate the actual error, which is caused by a missing Python module called `sphinx_rtd_theme`. Of course, as a long time Sphinx user you might have known it from the very start.

Second, we need to know where is the Python interpreter that this dependency should be installed to. So time to switch to reStructuredText channel in OUTPUT panel, and read what it says,

``` text
[Log - 7:13:11 p.m.] Running cmd: "C:\Users\lextudio\AppData\Local\Programs\Python\Python310\python.exe" -c "import esbonio.lsp; from distutils.version import LooseVersion; print(LooseVersion(esbonio.lsp.__version__) < LooseVersion('0.8.0'))"
```

Clearly, the interpreter is `C:\Users\lextudio\AppData\Local\Programs\Python\Python310\python.exe`.

Finally, we can add this dependency via `C:\Users\lextudio\AppData\Local\Programs\Python\Python310\python.exe -m pip install sphinx_rtd_theme`.

But even now, you find features relying on Esbonio do not come back normally. That's because we need to manually restart Esbonio by clicking "esbonio: idle" in status bar.

## Future Plan

The migration to Esbonio is going to take a few months, as some existing features of Snooty are missing in Esbonio.

This is a very promising language server design, and let's wait and see.
