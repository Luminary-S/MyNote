# vscode

## latex-workshop
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
