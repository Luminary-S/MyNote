# Solution for different Ubuntu Problems

## clean Ubuntu core
```
dpkg --list|grep linux-image
dpkg --list|grep linux-headers
sudo apt-get purge linux-image-3.19.0-{18,20,21,25}
sudo apt-get purge linux-headers-3.19.0-{18,20,21,25}
```

## clean apt-get lock
```
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
```

### 解决dpkg/apt-get error : 子进程 post-installation script 返回了错误号 1
   refer: https://blog.csdn.net/gatieme/article/details/52839814 ，recommend Method 3, details:
1. sudo mv /var/lib/dpkg/info /var/lib/dpkg/info_old //现将info文件夹更名
2. sudo mkdir /var/lib/dpkg/info //再新建一个新的info文件夹
3. sudo apt-get update
4. apt-get -f install
5. sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info_old //执行完上一步操作后会在新的info文件夹下生成一些文件，现将这些文件全部移到info_old文件夹下
6. sudo rm -rf /var/lib/dpkg/info //把自己新建的info文件夹删掉
7. sudo mv /var/lib/dpkg/info_old /var/lib/dpkg/info //把以前的info文件夹重新改回名字


## “下载额外数据文件失败 ttf-mscorefonts-installer”的问题 
refer: https://www.zeyes.org/blog/2017/09/solve-ubuntu-download-ttf-mscorefonts-installer-failed.html
```
cd /usr/share/package-data-downloads/
sudo rm ttf-mscorefonts-installer
cd /var/lib/update-notifier/package-data-downloads/
sudo rm ttf-mscorefonts-installer
cd /var/lib/update-notifier/user.d/
sudo rm data-downloads-failed
```

## dpkg: 处理软件包 xxx (--configure)时出错：
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
## sudo apt-get -f install 出现 gzip: stdout: No space left on device
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

## possible missing firmware
refer：https://blog.csdn.net/dzhongjie/article/details/84306900 

1. just download the firmware in:

https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/tree/i915

2. press "plain" to download
3. sudo copy the firmware to "/lib/firmware/i915"
4. sudo updatedb
5. sudo apt-get update

## USB device not found
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

## Failed to restart network.service: Unit network.service failed to load: No such file or directory. OR  重启网卡提示:/org/freedesktop/NetworkManager/ActiveConnection/(n)
refer : https://blog.csdn.net/guotong1988/article/details/50419142 and https://blog.csdn.net/langkeziju/article/details/10508909
```
不用service network restart
用service network-manager restart
```