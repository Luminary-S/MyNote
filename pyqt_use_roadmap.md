# pyqt use roadmap
<!-- TOC -->

- [pyqt use roadmap](#pyqt-use-roadmap)
  - [insert *pictures, gif, video* in the QLabel](#insert-pictures-gif-video-in-the-qlabel)
    - [style setting](#style-setting)
    - [insert txt， use htmlcss](#insert-txt-use-htmlcss)
    - [insert *pic*](#insert-pic)
    - [insert video](#insert-video)
    - [opencv2 video stream into QLabel](#opencv2-video-stream-into-qlabel)
  - [pyserial in python2 and python3](#pyserial-in-python2-and-python3)
  - [QlineEdit](#qlineedit)

<!-- /TOC -->

## insert *pictures, gif, video* in the QLabel
    refer: https://zhuanlan.zhihu.com/p/32134728
In QLabel, you can insert:

|type| method|
|-----------|-------------|
| txt       | setText()   |
| pic       | setPixmap() |
| movie,gif | setMovie()  |
|数字|setNum()|

### style setting
```python
lb3.setWordWrap(True)  # 自动换行
lb1.setAlignment(Qt.AlignVCenter | Qt.AlignRight) #对齐方式
lb2.setScaledContents(True)   #内容适应label尺寸大小

lb1.setGeometry(0,0,300,200) #设置位置，0,0是起始位置,300,200是大小
lb1.setStyleSheet("border: 2px solid red")

lb.setAlignment(Qt.AlignBottom | Qt.AlignRight) # should import from PyQt5.QtCore import Qt
```

### insert txt， use htmlcss
```python
        lb = QLabel(self)

        html = '''
                <style type="text/css">
                    table.imagetable {
                        font-family: verdana,arial,sans-serif;
                        font-size:11px;
                        color:#333333;
                        border-width: 1px;
                        border-color: #999999;
                        border-collapse: collapse;
                    }
                  #...里面众多的CSS内容，我就省略了，节约空间
            '''
        lb.setText(html)
```

### insert *pic*

```python
cuhk_pix = QPixmap('img/cuhk.png') #need to create a QPixmap
icon_cuhk_label.setPixmap(cuhk_pix)
```

### insert video
```python
        movie = QMovie("movie.gif")
        self.lb.setMovie(movsie)
        if self.sender() == self.bt1:
            movie.start()
        else:
            movie.stop()
            self.lb.setPixmap(self.pix)
```

### opencv2 video stream into QLabel
refer: https://blog.csdn.net/ccchen706/article/details/71425653 
1. should transfer cv BGR to RGB 
2. still create a QImage
```
img=cv2.resize(src=img,dsize=None,fx=0.2,fy=0.2)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
self._image = QtGui.QImage(img2,img2.shape[1], img2.shape[0],img2.shape[1] * 3, QtGui.QImage.Format_RGB888)
```



## pyserial in python2 and python3
refer: https://blog.csdn.net/weixin_38685248/article/details/71356712
1. python3.5的write函数要encode，pyhon2.7不用
2. python2.7如果要连接虚拟串口，要加rtscts=True,dsrdtr=True 

## QlineEdit
1. set focus or no focus, make the lineEdit human avialable or not. not available:```focusPolicy: no focus ```
2. set placeholderText to set the default show txt in the box
3. get text and set text：
```python
QString	text () const
void	setText ( const QString & )
```
4. alignment
```
Qt::Alignment	alignment () const
void	setAlignment ( Qt::Alignment flag )
```
5. get and set selected text
```
QString	selectedText () const
void QLineEdit::setSelection ( int start, int length )
```
6. set text mode: code,normal,noecho,PasswordEchoOnEdit
```
    EchoMode	echoMode () const
    void	setEchoMode ( EchoMode )
```
```
QLineEdit::Normal	0	Display characters as they are entered. This is the default.
QLineEdit::NoEcho	1	Do not display anything. This may be appropriate for passwords where even the length of the password should be kept secret.
QLineEdit::Password	2	Display asterisks instead of the characters actually entered.
QLineEdit::PasswordEchoOnEdit	3	Display characters as they are entered while editing otherwise display asterisks.
```
7. get multi-lines text
```
textEdt->setPlainText("12345\nabcdef");
	QString str;
	str = textEdt->toPlainText();
```