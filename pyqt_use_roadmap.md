# pyqt use roadmap
<!-- TOC -->

- [pyqt use roadmap](#pyqt-use-roadmap)
  - [insert *pictures, gif, video* in the QLabel](#insert-pictures-gif-video-in-the-qlabel)
    - [style setting](#style-setting)
    - [insert txt， use htmlcss](#insert-txt-use-htmlcss)
    - [insert *pic*](#insert-pic)
    - [insert video](#insert-video)
  - [](#)

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

## 