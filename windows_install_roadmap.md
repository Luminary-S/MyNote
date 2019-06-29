# windows software install 

# microsoft office
refer: [windows 激活工具](https://www.52pojie.cn/thread-806566-1-1.html)
1. 链接：https://pan.baidu.com/s/1WfnlGvtL0vGxlZrA5wsj1w 密码：kph5
2. 实用工具，激活；如果没有下载到下载

# Texstudio + miktex
refer：[LaTeX (MikTeX+TeXstudio) 在win10上的配置教程](https://blog.csdn.net/weixin_39278265/article/details/81348752)
1. 下载[TeXstudio](http://texstudio.sourceforge.net/)
  * [texstuido usermanual](http://texstudio.sourceforge.net/manual/current/usermanual_en.html)
2. 安装[MikTeX](https://miktex.org/howto/install-miktex)
3. test: test.tex
```
\documentclass{article} 
    \title{A Test for TeXstudio} 
    \author{Dale无双} 
\begin{document} 
	\maketitle
	\tableofcontents 
	\section{Hello China} China is in East Asia. 
	\subsection{Hello Beijing} Beijing is the capital of China. 
	\subsubsection{Hello Dongcheng District} 
	\paragraph{Hello Tian'anmen Square}is in the center of Beijing 
	\subparagraph{Hello Chairman Mao} is in the center of Tian'anmen Square 
\end{document} 
```
3. 中文支持，实用option->configuration->build->compiler choose "xelatex",and add ```\usepackage{xeCJK}```
