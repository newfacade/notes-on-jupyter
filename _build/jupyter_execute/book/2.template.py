#!/usr/bin/env python
# coding: utf-8

# # 样书
# 
# ```{note}
# 通过案例来学习是最快的！
# ```
# 
# ## 创建样书
# 
# Jupyter Book comes bundled with a lightweight sample book to help you understand a book’s structure. 创建样书（sample book）的命令：
# 
# ```
# jupyter-book create mybookname/
# ```

# ## 样书结构
# 
# Take a look at the book that you just created:
# 
# ```
# mybookname/
# ├── _config.yml
# ├── _toc.yml
# ├── intro.md
# ├── logo.png
# ├── markdown-notebooks.md
# ├── markdown.md
# ├── notebooks.ipynb
# ├── references.bib
# └── requirements.txt
# ```
# 
# 其中最重要的是
# 
# * _config.yml 总配置文件，配置书名、作者、build方式等
# 
# * _toc.yml 目录文件
# 
# * 内容文件，包括 intro&#46;md,  markdown&#46;md,  notebooks.ipynb,  markdown-notebooks&#46;md

# ## 配置文件 (_config.yml)
# 
# 我们主要关心以下几项:
# 
# ```yaml
# title: My sample book  # 书名
# author: The Jupyter Book Community  # 作者名
# logo: logo.png  # 书 logo 图片的地址
# 
# # force: force the execution of all notebooks.
# # auto: will only execute notebooks that are missing at least one output.
# # off: turn off notebook execution.
# execute:
#   execute_notebooks: force
# ```

# ## 目录文件 (_toc.yml)
# 
# Each entry relates to a file, they should be added as names with `no extensions` and `relative to your book's root folder`.
# 
# ```yaml
# format: jb-book  # 可选 jb-book 或 jb-article
# root: intro  # 落地页 intro.md
# chapters:
# - file: markdown  # 第一章 markdown.md
# - file: notebooks  # 第二章 notebooks.ipynb
# - file: markdown-notebooks  # 第三章 markdown-notebooks.md
# ```

# ## 内容
# 
# A collection of text files make up your book's content, these can be:
# 
# ### Markdown 文件 (.md)
# 
# intro&#46;md 和 markdown&#46;md 是这种格式
# 
# 我们的 markdown 文件除了可以使用通用的 markdown 语法外(e.g., using `**bold**` to denote **bold**)，还可以使用一些扩展语法使我们的文档更漂亮，比如说
# 
# ````md
# ```{note}
# Here is a note
# ```
# ````
# 
# 会被 Jupyter Book 渲染为
# 
# ```{note}
# Here is a note
# ```
# 
# ```{caution}
# All content files must have a page title (specified as the first header). All subsequent headers must increase linearly (so no jumps from H1 to H3).
# ```
# 
# 
# ### Jupyter Notebooks (.ipynb)
# 
# notebooks.ipynb 是这种格式
# 
# 每一个 notebook 都会对应到一个 kernel (Python, R, Julia 等，我们只使用 Python 3) that defines the language used to execute the notebook's computational content.
# 
# ### MyST Markdown Notebooks (.md)
# 
# markdown-notebooks&#46;md 是这种格式
# 
# Finally, you can combine Jupyter Notebook and text formats with Jupyter Book. This allows you to write the structure of a Jupyter Notebook entirely with text.
# 
# 这种格式的特征是开头有一个 YAML metadata blog ，我们一般不会用到，了解即可。

# In[ ]:




