#!/usr/bin/env python
# coding: utf-8

# # JupyterLab 概述
# 
# ```{note}
# JupyterLab is the next-generation web-based user interface for Project Jupyter.<br/>
# JupyterLab enables you to work with documents and activities such as Jupyter notebooks, text editors, and terminals in a flexible, integrated, and extensible manner.
# ```
# 
# 官网：<https://jupyterlab.readthedocs.io/en/stable/>

# ## JupyterLab 的功能
# 
# * Jupyter notebooks (.ipynb files) are fully supported in JupyterLab（核心功能）.
# * Use Code consoles.
# * Use Terminals.
# * Multiple views of documents with different editors or viewers（分屏）.
# * JupyterLab offers a unified model for viewing and handling data formats.
# 
# 那为什么要使用 JupyterLab 呢？Personally:
# 
# 1. 确实很适合做数据科学。
# 2. 别人也在用 Jupyter notebooks（或者类似的 Google colab），比如说某些 GitHub 项目、很多 Coursera 课程的作业、《Dive into Deep Learning》每个页面都是一个 notebook、去 Kaggle 参加比赛需要自己写 notebook 等。
# 3. 用来写 Markdown 文档。
# 4. 用来写 Jupyter Book（我们将在第二部分做详细介绍）。

# ## 安装 JupyterLab
# 
# 通过 pip 安装：
# 
# ```
# pip install jupyterlab
# ```
# 
# 通过 conda 安装：
# 
# ```
# conda install -c conda-forge jupyterlab
# ```

# ## 启动 JupyterLab
# 
# Once installed, launch JupyterLab with:
# 
# ```
# jupyter lab
# ```
# 
# JupyterLab will open automatically in your browser（本地运行的 JupyterLab 的 url 一般是 `http://localhost:8888/lab`）:
# 
# ```{image} ../images/lab1.jpg
# :alt: launch
# :class: bg-primary mb-1
# :width: 700px
# ```
# 
# 
# You may also access JupyterLab by entering the notebook server’s URL into the browser:
# 
# ```
# http(s)://<server:port>/<lab-location>/lab
# ```

# ## Jupyter 界面
# 
# ```{note}
# While JupyterLab has many features found in traditional IDEs, it remains focused on interactive, exploratory computing. The JupyterLab interface consists of a `main work area` containing tabs of documents and activities, a collapsible `left sidebar`, and a `menu bar`.
# ```
# 
# Left Sidebar 从上到下依次是:
# 
# * a file browser,
# * a list of tabs in the main work and of running kernels and terminals,
# * the table of contents,
# * the extension manager.
# 
# Menu Bar 和 Main Work Area functioning as you expected.

# In[ ]:




