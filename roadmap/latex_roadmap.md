latex usage problem solution
------

## texlive 缺少包 如何apt 查询安装

在Linux下用 latex 编译 ××.tex 文件有时候时会提示:
`
 ! LaTeX Error: File `××××.sty' not found.
`
### Solution:
Method 1:
去[CTAN](http://www.ctan.org/)，把该文件下下来后直接放到你所编译的文件夹中再重新编译即可

Method 2:
1. download tool:  `sudo apt-get install apt-file`
2. check lost style file `apt-file -x search ‘/×××.sty$’`
3. download package 

e.g.:
```bash
apt-file -x search '/wrapfig.sty$' 
    #系统会给出
texlive-latex-extra: /usr/share/texlive/texmf-dist/tex/latex/wrapfig/wrapfig.sty
    #再去下载 texlive-latex-extra 这个包即可：
sudo apt-get intall texlive-latex-extra
```