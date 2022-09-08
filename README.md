# Programming Rust

本书为《Programming Rust - Fast, Safe Systems Development》第2版的个人中文翻译，仅供学习和交流使用，如有侵权请联系作者删除

## 以下为英文原版购买地址

* 电子版[购买地址](https://www.amazon.com/-/zh/dp-B0979PWD4Z/dp/B0979PWD4Z/ref=mt_other?_encoding=UTF8&me=&qid=)
* 印刷版[购买地址](https://www.amazon.com/-/zh/dp-1492052590/dp/1492052590/ref=mt_other?_encoding=UTF8&me=&qid=)

---

## 目录

0. 前言
1. 系统级程序员的福音
2. Rust概览
3. 基本类型
4. 所有权与move
5. 引用
6. 表达式
7. 错误处理
8. crate与模块
9. 结构体
10. 枚举与模式
11. trait与泛型
12. 运算符重载
13. 工具trait
14. 闭包
15. 迭代器
16. 集合
17. 字符串与文本
18. 输入输出
19. 并发
20. 异步编程
21. 宏
22. unsafe代码
23. 外部函数

---

## 下载

见[Nightly Build](https://github.com/MeouSker77/ProgrammingRust/releases/tag/v0.99)

---

## 说明

- pdf文件直接在github中打开可能会失败，建议下载到本地再打开
- 翻译的过程中仅保留了原版的内容，并没有还原原版的格式，例如配色方案、标题格式、页眉页脚格式等都和原版不同
- 因为这本书内容比较长，为了尽快翻译完，在翻译的过程中并不会花时间校对。所以可能错误会比较多，如果发现错误，欢迎提出issue或PR。
- Github Action会每天自动从最新的代码编译pdf，并上传到release的Nightly Build标签里。
- 有些字体并不是所有系统上都有并且不方便传播，所以在github上编译的本书没有指定字体，你可以自己修改指定的字体，然后自己编译。
- 本人在某些时间段可能会很忙没时间翻译。但请放心，如果我哪天决定弃坑，一定会在这里通知，所以请不要担心我是不是弃坑了

---

## 编译

1. 安装`tectonic`
2. 安装`python`
3. 安装`Pygements`
    ```bash
    pip install Pygments
    ```
4. 如果`src/main.tex`中有`\includeonly{xxx}`这一行，请在编译之前删除这一行
5. 编译pdf文件
    ```bash
    cd src
    tectonic -Z shell-escape main.tex
    ```
6. 生成的`main.pdf`就是最后的pdf文件

- note: 安装`Pygements`之后必须确保pip安装的可执行文件在`PATH`中，即`pygmentize -V`必须能正常打印出版本信息
- note: 如果安装`tectonic`之后`tectonic`不在`PATH`中，请把第5步中的`tectonic`替换成完整的路径
- note: 如果所有步骤都正确操作仍编译失败，欢迎提issue
