# 1. python roadmap

## 1.1. useful links
[online visulization tutorial](http://www.pythontutor.com/visualize.html#mode=edit)
p
# 2. sympy
refer: [数值 Python: 常微分方程](https://vlight.me/2018/05/01/Numerical-Python-Ordinary-Differential-Equations/)

# 3. numpy
refer: [python 数据处理中各种存储方式里数据类型的转换](https://www.cnblogs.com/niuchen/p/6187217.html)

类型  | 类型代码  | 说明
------- | ------- | -------
int8,uint8  | i1,u1  | 有符号和无符号的8位（1个字节）整型
int16,uint16  | i2,u2  | 有符号和无符号的16位（2个字节）整型
int32,uint32  | i4,u4  | 有符号和无符号的32位（4个字节）整型
int64,uint64  | i8,u8  | 有符号和无符号的64位（8个字节）整型
float16  | f2  | 半精度浮点数
float32  | f4或f  | 标准的单精度浮点数。与c的float兼容
float64  | f8或d  | 标准的双精度浮点数。与c的double和python的float对象兼容
float128  | f16或g  | 扩展精度浮点数
complex64，complex128  | c8,c16  | 分别用两个32位，64位或128位浮点数表示的
complex256  | c32  | 复数
bool  | ?  | 存储true和false值的布尔类型
obiect  | O  | python对象类型
string  | S  | 固定长度的字符串类型（每个字符1个字节）
unicode  | U  | 固定长度的uincode类型（字数由平台决定）跟字符创的定义方式一样（如U10）

# 4. 使用非 用 not 不要用 ～


## 4.1. force to reinstall pip
also for problem:
"ModuleNotFoundError: No module named 'pip._internal'"
```bash
           curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
           python get-pip.py --force-reinstall
```

# 5. pip
```
# install
sudo apt install python3-pip
sudo apt install build-essential python3-dev  python3-setuptools

pip uninstall scrapy
pip search scrapy
pip list
pip --version
# list outdated package
pip list --outdated
```
# 6. view all package in browser
python doc 查看所有的 安装包
   ```
   python -m pydoc -p 1234
   pydoc server ready at http://localhost:1234/
   ```

# 7. 引用不同文件夹下的文件
在此处有一个文件   `application/app/folder/file.py`
想在 `application/app2/some_folder/some_file.py`  中应用`file.py`
* method: ```from application.app.folder.file import func_name```
* 保证folder文件夹（也就是需要的文件夹下）包含__init__.py，若是没有，可以新建一个

# 8. virtualenv and virtualenvwrapper 的 基本使用

## 8.1. 安装
```
pip install virtualenv virtualenvwrapper
export WORKON_HOME=~/Envs  #设置环境变量
mkdir -p $WORKON_HOME #创建虚拟环境管理目录
find / -name virtualenvwrapper.sh #找到virtualenvwrapper.sh的路径
source 路径 #激活virtualenvwrapper.sh
```

## 8.2. 使用
1、创建一个虚拟环境：

mkvirtualenv project_env

   这会在Envs 中创建 project_env虚拟环境

　  选择一个python解释器来搭建：

mkvirtualenv env  --python=python2.7

 

2、在虚拟环境上工作：

```
workon project_env
或者，您可以创建一个项目，它会创建虚拟环境，并在 $WORKON_HOME 中创建一个项目目录。 当您使用 workon project_env 时，会 cd -ed 到项目目录中。
mkvirtualenv project_env
virtualenvwrapper 提供环境名字的tab补全功能。当您有很多环境， 并且很难记住它们的名字时，这就显得很有用。
workon 也能停止您当前所在的环境，所以您可以在环境之间快速的切换。
```
3、停止虚拟环境
```
deactivate
```
4、删除：
```
 rmvirtualenv project_env
```
5、其他有用的命令
```
lsvirtualenv    #列举所有的环境。

cdvirtualenv    #导航到当前激活的虚拟环境的目录中，比如说这样您就能够浏览它的 site-packages。

cdsitepackages   # 和上面的类似，但是是直接进入到 site-packages 目录中。

lssitepackages     #显示 site-packages 目录中的内容。
```
6、查看当前安装库版本
pip freeze #查看当前安装库版本
#创建 requirements.txt 文件，其中包含了当前环境中所有包及 各自的版本的简单列表
#保持部署相同，一键安装所有包
pip install -r requirements.txt
pip freeze > requirements.txt 