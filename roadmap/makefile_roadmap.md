# make file roadmap

# 基本格式为“目标:依赖 命令”
refer: [makefile实例（1）-helloworld](https://www.cnblogs.com/jacklikedogs/p/4125317.html)

一个 makefile 主要含有一系列的规则，如下：
```
A: B
(tab)<command>
(tab)<command>
```
```
target ... : prerequisites ...         
         command
```        
重要： 每个命令行前都必须有tab符号
举例来说，一种简单写法如下：
```
main : main.c
　　gcc main.c –o main
```
在终端执行make命令就可以得到main文件了
```
make
```

# makefile 的执行过程
1.  通常make命令会逐行解释makefile文件，然后执行第一个”目标格式行”及其后的”目标命令“。直到碰到下一个”目标格式行”为止。
    1.  注意这里指的是下一个”目标格式行“，而不是文件末尾。
    2.  所以我们把生成最后的可执行文件的makefile代码放在第一行时，只需要键入make就可以。
2.  而有些makefile文件未将生成最后的可执行文件的代码放在第一行，所以如果make的话，就只能执行到第一个目标格式行的code.


# makefile 中的符号
再写一下其它符号的意义，记住就行了：
```
    $(Files)，取File变量的值。
    $@ 目标文件
    $^ 全部依赖
    $< 第一个依赖
    $? 第一个变化的依赖
```

# phony
clean不是一个文件，它只不过是一个动作名字，其冒号后面为空，make就不会找文件的依赖性，也就不会自动执行其后所定义的命令。

要执行其后的命令，就需要在make 命令后显式指出这个名字。这样我们就可以定义一些与编译无关的命令：打包程序，清理程序等外围操作等。

 用".PHONY {目标名}"定义一个伪目标， 用"make {目标名}"执行该伪目标
```makefile
.PHONY : clean
clean :
　　@rm -f main *.o
　　@echo 'clean'
```
此时执行make命令，终端会显示系统执行的每条命令，如果你不想系统显示它执行的命令，在每条命令的前面加上“@”即可。