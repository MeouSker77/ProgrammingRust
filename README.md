# Programming Rust

本书为《Programming Rust - Fast, Safe Systems Development》第2版的个人中文翻译，仅供学习和交流使用，如有侵权请联系作者删除

## 以下为英文原版购买地址

* 电子版[购买地址](https://www.amazon.com/-/zh/dp-B0979PWD4Z/dp/B0979PWD4Z/ref=mt_other?_encoding=UTF8&me=&qid=)
* 印刷版[购买地址](https://www.amazon.com/-/zh/dp-1492052590/dp/1492052590/ref=mt_other?_encoding=UTF8&me=&qid=)

---

## 下载（pdf）

见[Nightly Build](https://github.com/MeouSker77/ProgrammingRust/releases/tag/v0.99)

---

## 在线阅读

见[前言](https://meousker77.github.io/ProgrammingRust/index.html)

感谢 @knowaywood 提供了静态网站的部署方案。

本站点使用 [BookML](https://github.com/vlmantova/bookml) 从 LaTeX 直接构建 HTML，并使用其原版 GitBook 风格。前言、译者序和各章节与 PDF 共享同一组 `.tex` 文件，按章生成网页。由于 LaTeXML 不支持 `minted`，构建脚本仅在临时副本中把代码环境转换为 `listings`；PDF 源文件不变。章节更新会通过 GitHub Actions 自动重新构建并发布。

---

## 说明

- ~第17章没有翻译~ 感谢 @knowaywood 提供了latex版第17章的翻译。
- 翻译的过程中仅保留了原版的内容，并没有还原原版的格式，例如配色方案、标题格式、页眉页脚格式等都和原版不同。
- 如果发现错误，欢迎提出issue或PR。
- Github Action会每天自动从最新的代码编译pdf，并上传到release的Nightly Build标签里。
- 有些字体并不是所有系统上都有并且不方便传播，所以在github上编译的本书没有指定字体，你可以自己修改指定的字体，然后自己编译。

---


## 编译 pdf

1. 安装`tectonic`
2. 安装`python`
3. 安装`Pygements`
    ```bash
    pip install Pygments
    ```
4. 如果`src/main.tex`中有`\includeonly{xxx}`这一行且未被注释掉（%后的内容是注释），请在编译之前删除这一行
5. 编译pdf文件
    ```bash
    cd src
    tectonic -Z shell-escape main.tex
    ```
6. 生成的`main.pdf`就是最后的pdf文件

- note: 安装`Pygements`之后必须确保pip安装的可执行文件在`PATH`中，即`pygmentize -V`必须能正常打印出版本信息
- note: 如果安装`tectonic`之后`tectonic`不在`PATH`中，请把第5步中的`tectonic`替换成完整的路径
- note: 如果所有步骤都正确操作仍编译失败，欢迎提issue


---


## 本地构建网站

需要 Python 3 和 Docker。构建脚本使用固定版本的 BookML 官方镜像：

```bash
# 构建（生成 dist/index.html 和静态资源）
bash scripts/build-html.sh

# 预览构建产物
python3 -m http.server 4173 --directory dist
```

也可以设置 `BOOKML_IMAGE` 环境变量指定其他 BookML 镜像。
