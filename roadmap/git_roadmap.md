# 1. git use roadmap 


## 1.1. git daily ops, update remote repository
1. check code status
```
git status
```
2. add all code
```
git add * 
```
3. commit and add update msg
```
git commit -m "msg"  
```
4. pull remote latest code
```
git pull 
```
5. push to remote repository
``` 
git push origin master 
```
## 1.2. git-ssh 配置
refer: https://segmentfault.com/a/1190000002645623
1. 设置Git的user name和email：
```
    git config --global user.name "humingx"
    git config --global user.email "humingx@yeah.net"
```
2. 生成密钥, 连续3个回车。如果不需要密码的话; 最后得到了两个文件：id_rsa和id_rsa.pub。
```
ssh-keygen -t rsa -C "humingx@yeah.net"
```
3. 添加生成的 SSH key 到 ssh-agent
```
ssh-add ~/.ssh/id_rsa
```
4. 登陆Github, 添加 ssh, 在 setting-> ssh and GPG keys --> New SSH keys, 粘贴 生成的公开密钥，即 ～/.ssh/id_rsa.pub, 如果在生成id_rsa和id_rsa.pub的时候修改了两个文件保存的位置, 到设置的位置拷贝即可。
5. test
```
ssh -T git@github.com
选择yes
```
6. 后面就可以进行 [git daily ops, update remote repository](#git-daily-ops-update-remote-repository)


## 1.3. relate local git repository to remote repository
   refer: [上传本地代码及更新代码到github教程](https://www.cnblogs.com/zlxbky/p/7727895.html)
1. go to github website, login in and create remote Repository, sample name is : MyNote, then your repository link should be: 
   https://github.com/Luminary-S/MyNote.git
2. go to your local directory
3. ```echo "ReadMe" >> README.md```  &nbsp; # just make sure you have a readme file in your repository, if you have, just skip
4. ```echo "*.[oa]" >> .gitignore```  &nbsp; # add a git ignore file, here, I just skip .o and .a file, always they are compling middleware, how to write gitignore, refer [gitignore 文件 编写方法](#gitignore-文件-编写方法)
5. ```git add .``` &nbsp;  # add all files in the local repository
6. ```git commit -m "add new repository"``` &nbsp; # commit your added file
7. ```git remote add origin https://github.com/Luminary-S/MyNote.git ```  &nbsp; # pull remote repository to local to build connection
8. ```git pull origin master``` # pull remote before push, in case of code conflicts
9. ```git push -u origin master``` # push code to remote

note:
1. 出现 `fatal: refusing to merge unrelated histories` using cmd: ```git pull origin master --allow-unrelated-histories```



## 1.4. gitignore 文件 编写方法
refer: [Git ignore文件的设置](https://www.jianshu.com/p/267cd94f1d49)
```
# 以#开头的行都是注释

# 忽略*.o和*.a文件（常见的编译过程中产生的文件）
 *.[oa]

# 忽略*.c和*.C文件，somefile.b除外，!用于在在某规则之后增加例外
*.[bB]
!somefile.b

# 忽略somepath文件和somepath目录
dbg

# 只忽略somepath目录，不忽略somepath文件
somepath/

# 只忽略somepath文件，不忽略somepath目录
somepath 
!somepath/

# 只忽略当前目录下的somepath文件和目录，子目录的somepath不在忽略范围内
/somepath
``` 

## 1.5. 在git conf 中配置username
refer: https://blog.csdn.net/qq_15437667/article/details/51029757
1. 全局的conf 在 ～/.gitconfig, local repository 的在相应的文件夹下的 ./.git/conf 文件中
2. 添加的内容
```
[user]
name=用户名
email=用户邮箱
```
3. 修改 .git/conf 文件,保证不需要每次都输入username,修改url的部分
```
    [remote "origin"]
    url = git@github.com:humingx/humingx.github.io.git
    fetch = +refs/heads/*:refs/remotes/origin/*
```

## 1.6. git 中删除文件
在git中删除, 只删除文件在git记录，不删除文件
```git
git rm --local  filename
```

## 1.7. 不小心误删除
只要git 里面有记录可以， 如下可以还原test.txt文件
```
git checkout -- test.txt
```

## 1.8. git tag
refer: [git tag 用法](https://www.cnblogs.com/senlinyang/p/8527764.html)
### 1.8.1. 创建tag
```
git tag -a V1.2 -m 'release 1.2'
```
上面的命令我们成功创建了本地一个版本 V1.2 ,并且添加了附注信息 'release 1.2'
### 1.8.2. 查看tag
```
git tag
```
要显示附注信息,我们需要用 show 指令来查看
```
git show V1.2
```
但是目前这个标签仅仅是提交到了本地git仓库.如何同步到远程代码库
```
git push origin --tags
```
如果刚刚同步上去,你缺发现一个致命bug ,需要重新打版本,现在还为时不晚.
```
git tag -d V1.2
```
到这一步我们只是删除了本地 V1.2的版本,可是线上V1.2的版本还是存在,如何办?这时我们可以推送的空的同名版本到线下,达到删除线上版本的目标:
```
git push origin :refs/tags/V1.2
```
如何获取远程版本?
```
git fetch origin tag V1.2
```
这样我们可以精准拉取指定的某一个版本.适用于运维同学部署指定版本.

## 1.9. git branch
查看远程分支
```
git branch -a
```
查看本地分支
```
git branch
```
## git fast download
https://github.com <font color=#FFA500> .cnpmjs.org </font> /TixiaoShan/LIO-SAM.git