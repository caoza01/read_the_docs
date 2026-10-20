第四章：工程组织实践
====================

本章记录本文档工程的组织方式与相关决策，内容整理自实际搭建过程。

当前目录结构
------------

.. code-block:: text

   read_the_docs/
   ├── conf.py                # Sphinx 配置（主题、扩展、版本号）
   ├── index.rst              # 入口 + 目录树
   ├── intro.rst              # 第一章
   ├── usage.rst              # 第二章
   ├── faq.rst                # 第三章
   ├── layout.rst             # 第四章（本章）
   ├── build.py               # 构建脚本
   ├── requirements.txt       # 依赖清单
   ├── .readthedocs.yaml      # Read the Docs 构建配置
   └── .gitignore             # 忽略 _build/ 等产物

为什么保持平铺
--------------

- 纯文档仓库的标准形态就是 ``conf.py`` 与 ``index.rst`` 位于根目录，
  这也是 ``sphinx-quickstart`` 和 Read the Docs 官方教程的默认布局，
  工具链无需额外配置
- ``docs/`` 子目录是"代码 + 文档混合仓库"为隔离源码而引入的层级，
  纯文档仓库没有这个诉求，提前套一层只会增加配置成本

嵌入代码仓库
------------

将来本工程内容整体拷贝至代码仓库的 ``docs/`` 目录，目标形态：

.. code-block:: text

   gd32_800kw_dev/
   ├── .readthedocs.yaml      # 必须位于代码仓库根目录
   ├── docs/                  # 本工程内容原样拷入
   ├── 1_Application/
   ├── 2_Bussiness/
   └── ...

操作时注意三点：

1. ``.readthedocs.yaml`` 要放在代码仓库**根目录**，
   其中 ``sphinx.configuration`` 指向 ``docs/conf.py``
2. ``build.py`` 使用相对自身位置的路径，拷入 ``docs/`` 后无需修改
3. 拷贝时带上 ``docs/.gitignore``（Git 支持嵌套忽略规则，
   作用于该子树），或在代码仓库主 ``.gitignore`` 中添加 ``docs/_build/``

拷贝还是子模块
--------------

.. list-table:: 拷贝与子模块对比
   :header-rows: 1

   * - 维度
     - 直接拷贝
     - Git 子模块
   * - 操作
     - 拷贝文件即可
     - add 后还需 init --recursive
   * - 版本关系
     - 代码与文档同一 commit 演进
     - 各自独立，需手动更新指针
   * - 克隆体验
     - 一次克隆全部拿到
     - 忘记初始化则 docs/ 为空目录
   * - RTD 构建
     - 零配置
     - 需开启 submodules: true
   * - 适用场景
     - 文档随代码一起走
     - 多个仓库共用同一份文档

推荐**直接拷贝**。文档即代码（Docs as Code）的核心理念是代码与文档
在同一仓库、同一次提交中同步变更；子模块会打破这个耦合，仅当一份
文档需要被多个仓库共享时才值得引入。

版本管理回顾
------------

- ``conf.py`` 中的 ``version`` / ``release`` 控制页面显示的版本号
- Git tag（如 ``v1.0``）对应托管平台上的定版，``stable`` 指向最高 tag
- 默认分支（``main``）持续构建为 ``latest``，推送即自动更新
