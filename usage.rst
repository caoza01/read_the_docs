第二章：使用说明
================

环境准备
--------

.. _install-deps:

安装依赖
~~~~~~~~

.. code-block:: powershell

   pip install -r requirements.txt

.. _build-docs:

构建文档
~~~~~~~~

.. code-block:: powershell

   python build.py

常用语法
--------

代码块
~~~~~~

.. code-block:: c

   #include <stdio.h>

   int main(void)
   {
       printf("hello, docs\n");
       return 0;
   }

提示框
~~~~~~

.. warning::

   删除 ``_build`` 目录后需要重新构建。

表格
~~~~

=======  ===========  ===================
命令     作用          输出目录
=======  ===========  ===================
build    构建 HTML     _build/html
clean    清理产物      无
=======  ===========  ===================
