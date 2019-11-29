# 1. Solution for different Ubuntu Problems
<!-- TOC -->

- [1. Solution for different Ubuntu Problems](#1-solution-for-different-ubuntu-problems)
  - [1.1. clean Ubuntu core](#11-clean-ubuntu-core)
  - [1.2. clean apt-get lock](#12-clean-apt-get-lock)
    - [1.2.1. 解决dpkg/apt-get error : 子进程 post-installation script 返回了错误号 1](#121-%e8%a7%a3%e5%86%b3dpkgapt-get-error--%e5%ad%90%e8%bf%9b%e7%a8%8b-post-installation-script-%e8%bf%94%e5%9b%9e%e4%ba%86%e9%94%99%e8%af%af%e5%8f%b7-1)
  - [1.3. “下载额外数据文件失败 ttf-mscorefonts-installer”的问题](#13-%e4%b8%8b%e8%bd%bd%e9%a2%9d%e5%a4%96%e6%95%b0%e6%8d%ae%e6%96%87%e4%bb%b6%e5%a4%b1%e8%b4%a5-ttf-mscorefonts-installer%e7%9a%84%e9%97%ae%e9%a2%98)
  - [1.4. dpkg: 处理软件包 xxx (--configure)时出错：](#14-dpkg-%e5%a4%84%e7%90%86%e8%bd%af%e4%bb%b6%e5%8c%85-xxx---configure%e6%97%b6%e5%87%ba%e9%94%99)
  - [1.5. sudo apt-get -f install 出现 gzip: stdout: No space left on device](#15-sudo-apt-get--f-install-%e5%87%ba%e7%8e%b0-gzip-stdout-no-space-left-on-device)
  - [1.6. possible missing firmware](#16-possible-missing-firmware)
  - [1.7. USB device not found](#17-usb-device-not-found)
  - [1.8. Failed to restart network.service: Unit network.service failed to load: No such file or directory. OR 重启网卡提示:/org/freedesktop/NetworkManager/ActiveConnection/(n)](#18-failed-to-restart-networkservice-unit-networkservice-failed-to-load-no-such-file-or-directory-or-%e9%87%8d%e5%90%af%e7%bd%91%e5%8d%a1%e6%8f%90%e7%a4%baorgfreedesktopnetworkmanageractiveconnectionn)
  - [1.9. 让ubuntu使用更多的物理内存](#19-%e8%ae%a9ubuntu%e4%bd%bf%e7%94%a8%e6%9b%b4%e5%a4%9a%e7%9a%84%e7%89%a9%e7%90%86%e5%86%85%e5%ad%98)
  - [ubuntu 不能访问 127GB卷](#ubuntu-%e4%b8%8d%e8%83%bd%e8%ae%bf%e9%97%ae-127gb%e5%8d%b7)

<!-- /TOC -->
## 1.1. clean Ubuntu core
```
dpkg --list|grep linux-image
dpkg --list|grep linux-headers
sudo apt-get purge linux-image-3.19.0-{18,20,21,25}
sudo apt-get purge linux-headers-3.19.0-{18,20,21,25}
```

## 1.2. clean apt-get lock
```
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
```

### 1.2.1. 解决dpkg/apt-get error : 子进程 post-installation script 返回了错误号 1
   refer: https://blog.csdn.net/gatieme/article/details/52839814 ，recommend Method 3, details:
1. sudo mv /var/lib/dpkg/info /var/lib/dpkg/info_old //现将info文件夹更名
2. sudo mkdir /var/lib/dpkg/info //再新建一个新的info文件夹
3. sudo apt-get update
4. apt-get -f install
5. sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info_old //执行完上一步操作后会在新的info文件夹下生成一些文件，现将这些文件全部移到info_old文件夹下
6. sudo rm -rf /var/lib/dpkg/info //把自己新建的info文件夹删掉
7. sudo mv /var/lib/dpkg/info_old /var/lib/dpkg/info //把以前的info文件夹重新改回名字


## 1.3. “下载额外数据文件失败 ttf-mscorefonts-installer”的问题 
refer: https://www.zeyes.org/blog/2017/09/solve-ubuntu-download-ttf-mscorefonts-installer-failed.html
```
cd /usr/share/package-data-downloads/
sudo rm ttf-mscorefonts-installer
cd /var/lib/update-notifier/package-data-downloads/
sudo rm ttf-mscorefonts-installer
cd /var/lib/update-notifier/user.d/
sudo rm data-downloads-failed
```

## 1.4. dpkg: 处理软件包 xxx (--configure)时出错：
refer: https://www.cnblogs.com/EasonJim/p/7215988.html
```
#将info文件夹更名
sudo mv /var/lib/dpkg/info /var/lib/dpkg/info_old  
#再新建一个新的info文件夹
sudo mkdir /var/lib/dpkg/info  
#更新
sudo apt-get update  
sudo apt-get -f install  
#执行完上一步操作后会在新的info文件夹下生成一些文件，现将这些文件全部移到info_old文件夹下
sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info_old   
#把自己新建的info文件夹删掉
sudo rm -rf /var/lib/dpkg/info  
#把以前的info文件夹重新改回名字
sudo mv /var/lib/dpkg/info_old /var/lib/dpkg/info  
```
## 1.5. sudo apt-get -f install 出现 gzip: stdout: No space left on device
ref : https://blog.csdn.net/w5688414/article/details/79952389
```
cd /boot
ls
然后我删了一点，空出点空间，自己根据自己的情况删吧：
sudo rm System.map-4.13.0-37-generic
sudo rm config-4.13.0-31-generic
sudo rm vmlinuz-4.13.0-26-generic
sudo apt-get autoremove
```

## 1.6. possible missing firmware
refer：https://blog.csdn.net/dzhongjie/article/details/84306900 

1. just download the firmware in:

https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/i915

2. press "plain" to download
3. sudo copy the firmware to "/lib/firmware/i915"
4. sudo updatedb
5. sudo apt-get update

## 1.7. USB device not found
1. 安装usbmount
```
sudo apt-get install usbmount
```
2. 更改usbmount配置文件
```
sudo gedit /etc/usbmount/usbmount.conf
```
3. 在打开的文件中找到FILESYSTEM，并在其中添加vfat,ntfs
4. FS_MOUNTOPTIONS这个选项里加入”"-fstype= vfat,iocharset=utf8,codepage=936,umask=000,users”
5. 重启udev
```
sudo /etc/init.d/udev restart
```
6. 重启Ubuntu
```
sudo reboot
```
重启之后即可识别USB。

## 1.8. Failed to restart network.service: Unit network.service failed to load: No such file or directory. OR  重启网卡提示:/org/freedesktop/NetworkManager/ActiveConnection/(n)
refer : https://blog.csdn.net/guotong1988/article/details/50419142 and https://blog.csdn.net/langkeziju/article/details/10508909
```
不用service network restart
用service network-manager restart
```


## 1.9. 让ubuntu使用更多的物理内存
refer:https://whusl.iteye.com/blog/1402341
problem: 查看资源管理器(htop)你会发现一个奇怪的现象。物理内存使用率没超过50%，就开始使用swap空间了。用swap显然没有使用物理内存快。如何修改？

在ubuntu 里面，swappiness的值的大小对如何使用swap分区是有着很大的联系的。
swappiness=0的时候表示最大限度使用物理内存，然后才是 swap空间；swappiness＝100的时候表示积极的使用swap分区，并且把内存上的数据及时的搬运到swap空间里面。两个极端，对于 ubuntu的默认设置，这个值等于60，建议修改为10。具体这样做：

1. 查看你的系统里面的swappiness，在终端输入 cat /proc/sys/vm/swappiness，不出意外结果应该是60
2. 修改swappiness值为10。在终端输入sudo gedit /etc/sysctl.conf ，然后在最后一行添加vm.swappiness=10 ，保存。
3. 重启电脑，使设置生效。

## ubuntu 不能访问 127GB卷
```
sudo fdisk -l
找到所在卷
sudo ntfsfix /dev/sdb4
```