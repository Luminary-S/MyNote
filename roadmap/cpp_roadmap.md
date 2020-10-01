cpp roadmap
-----

## traits

refer:
1. [【C++模版之旅】神奇的Traits](https://blog.csdn.net/my_business/article/details/7891687)
2. [细说 C++ Traits Classes](https://blog.csdn.net/lihao21/article/details/55043881)

* 当函数，类或者一些封装的通用算法中的某些部分会因为数据类型不同而导致处理或逻辑不同时，traits会是一种很好的解决方案.
* 模板类使用 除了常见的类型以外 还有自定义的类型，或者模板中使用了 多种混合类型，需要使用特化和偏特化进行模板的部分实例成不同的模板，就需要使用traits