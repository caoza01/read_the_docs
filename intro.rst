第一章：简介
============

这是一个 Sphinx 文档工程示例，使用 Read the Docs 主题。

项目目标
--------

- 演示 reStructuredText 基本语法
- 演示多章节文档的组织方式
- 作为后续正式文档的起点

目录结构
--------

.. code-block:: text

   read_the_docs/
   ├── conf.py            # Sphinx 配置
   ├── index.rst          # 文档入口
   ├── build.py           # 构建脚本
   └── _build/html/       # 构建产物

.. note::

   编辑 ``.rst`` 文件后，执行 ``python build.py`` 重新生成 HTML。
