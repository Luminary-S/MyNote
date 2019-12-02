reference
1. [乾坤平台](https://qiankunpingtai.cn/article/1558878943974)
2. [mermaid](https://mermaid-js.github.io/mermaid/#/pie)
3. [more drawing plugin](https://shd101wyy.github.io/markdown-preview-enhanced/#/diagrams?id=mermaid)
4. [mermaid online tool](https://mermaidjs.github.io/ermaid-live-editor/)

```mermaid
gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid
        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2               :         des4, after des3, 5d
        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d
```

```flow
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End:>http://www.google.com
op1=>operation: get_hotel_ids|past
op2=>operation: get_proxy|current
sub1=>subroutine: get_proxy|current
op3=>operation: save_comment|current
op4=>operation: set_sentiment|current
op5=>operation: set_record|current

cond1=>condition: ids_remain空?
cond2=>condition: proxy_list空?
cond3=>condition: ids_got空?
cond4=>condition: 爬取成功??
cond5=>condition: ids_remain空?

io1=>inputoutput: ids-remain
io2=>inputoutput: proxy_list
io3=>inputoutput: ids-got

st->op1(right)->io1->cond1
cond1(yes)->sub1->io2->cond2
cond2(no)->op3
cond2(yes)->sub1
cond1(no)->op3->cond4
cond4(yes)->io3->cond3
cond4(no)->io1
cond3(no)->op4
cond3(yes, right)->cond5
cond5(yes)->op5
cond5(no)->cond3
op5->e 
```

```mermaid
pie
   title Pets adopted by volunteers
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15 
```

```mermaid
sequenceDiagram
起床->>吃饭: 稀饭油条
吃饭->>上班: 不要迟到了
上班->>午餐: 吃撑了
上班->>下班: time
Note right of 下班: 下班了
下班->>回家: bus
Note right of 回家: 到家了
回家-->>起床:c
Note left of 起床: 新的一天
```

```latex {cmd=true}
\documentclass{standalone}
\begin{document}
   Hello world!
\end{document}
```