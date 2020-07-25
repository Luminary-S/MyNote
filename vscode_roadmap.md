# vscode
<!-- TOC -->

- [vscode](#vscode)
  - [1. latex-workshop](#1-latex-workshop)
  - [2. vscode markdown TOC](#2-vscode-markdown-toc)
  - [3. matlab](#3-matlab)
    - [matlab python](#matlab-python)
    - [reference:](#reference)

<!-- /TOC -->
## 1. latex-workshop 
refer: 
* [latex-workshop](https://github.com/James-Yu/LaTeX-Workshop/wiki)
* [Visual Studio Code 折腾记：LaTeX 集成编辑环境](https://blog.ceba.tech/2018/11/Visual-Studio-Code-LaTeX/index.html)

```
Linux for external configuration

This is trickier, but works. See here.

    Download this file (modified to work with VScode):
        for Python 2: evince_synctex2.zip
        for Python 3: evince_synctex3.zip

    Unzip it in any folder in your PATH (for instance, $HOME/bin/ or $HOME/.local/bin).

    Add the following options to your configuration(setting.json):

    "latex-workshop.view.pdf.external.viewer.command": "evince2".
    "latex-workshop.view.pdf.external.viewer.args": [
        "%PDF%"
    ],
    "latex-workshop.view.pdf.external.synctex.command": "evince_forward_search",
    "latex-workshop.view.pdf.external.synctex.args": [
        "%PDF%",
        "%LINE%",
        "%TEX%"
    ],

To make this work both ways, first open the pdf file with the external viewer.
Zathura support

Forward: --synctex-forward flag

Backward: Use %{input} and %{line} as placeholders.

"latex-workshop.view.pdf.viewer": "external",
"latex-workshop.view.pdf.external.viewer.command": "zathura",
"latex-workshop.view.pdf.external.viewer.args": [
    "--synctex-editor-command",
    "code --reuse-window -g \"%{input}:%{line}\"",
    "%PDF%"
],
"latex-workshop.view.pdf.external.synctex.command": "zathura",
"latex-workshop.view.pdf.external.synctex.args": [
    "--synctex-forward=%LINE%:0:%TEX%",
    "%PDF%"
],

```
## 2. vscode markdown TOC 
refer: [VSCode为Markdown自动生成目录，解决目录不整齐问题](https://blog.csdn.net/u014171091/article/details/89629634)
setting-> eol change it into '\r\n'(unix) or '\n'(windows)

## 3. matlab
extension install: matlab, matlab interactive terminal, matlab snippets( code hint)

### matlab python 
1. go to /usr/local/MATLAB/R2018a/extern/engines/python (必须去这个下面)
2. 安装matlab 的 python engine ```sudo python setup.py build --build-base="builddir" install --prefix="installdir"
```
3. 安装 python的 matlab_kernel  ```sudo pip3 install matlab_kernel```
4. copy step 2 生成的 installdir 内面的python sitepackage to 你自己的python（对应版本）的site-packages 目录下面(主要是matalb文件夹和一个egg-info的文件)。```sudo cp -r  /usr/local/MATLAB/R2018a/extern/engines/python/installdir/lib/python3.6/site-packages/ ~/.local/lib/python3.6/site-packages/```
### reference: 
1. [搭建 MatLab 轻量级编写环境（VSCode，Jupyter）](https://zhuanlan.zhihu.com/p/129254524)
2. [python3.7环境下jupyter notebook安装matlab内核完全指南（Centos）](https://blog.csdn.net/ajacker/article/details/89266099)