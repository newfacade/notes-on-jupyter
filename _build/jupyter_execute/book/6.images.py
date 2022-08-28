#!/usr/bin/env python
# coding: utf-8

# # 图片
# 
# MyST Markdown provides a few different syntaxes for including images in your documents, as explained below.

# ## 标准 markdown 语法
# 
# ```
# ![fishy](../images/fun-fish.png)
# ```
# 
# 其中中括号里是图片的描述（caption），小括号里是图片位置，它会被渲染为
# 
# ![fishy](../images/fun-fish.png)
# 
# 这种方法很简便，但是不能调宽度，对齐等。

# ## MyST 语法
# 
# MyST 有专门的语法用来插入图片：
# 
# ````
# ```{image} ../images/fun-fish.png
# :alt: fishy
# :class: bg-primary mb-1
# :width: 200px
# :align: center
# ```
# ````
# 
# 其中 class 用于指定样式，它会被渲染为
# 
# ```{image} ../images/fun-fish.png
# :alt: fishy
# :class: bg-primary mb-1
# :width: 200px
# :align: center
# ```

# ## Raw HTML 图片
# 
# The image syntax described above gives you more customizability, but note that this syntax will not show the image in common Markdown viewers.
# 
# 要使用 HTML 图片，得先在 `_config.yml` 中做如下设置：
# 
# ````
# parse:
#   myst_enable_extensions:
#     # don't forget to list any other extensions you want enabled,
#     # including those that are enabled by default!
#     - html_image
# ````
# 
# HTML images will be parsed like any other image. For example:
# 
# ````
# <img src="../images/fun-fish.png" alt="fishy" class="bg-primary" width="200px">
# ````
# 
# will correctly render
# 
# <img src="../images/fun-fish.png" alt="fishy" class="bg-primary" width="200px">
# 
# ```{warning}
# Using raw HTML is usually a bad choice, so be careful before doing so!
# ```

# ## Figures
# 
# MyST Markdown also lets you include figures in your page. Figures are like images, except that they are `easier to reference elsewhere` in your book, and they include things like captions. To include a figure, use this syntax:
# 
# ````
# ```{figure} ../images/C-3PO_droid.png
# ---
# height: 150px
# name: directive-fig
# ---
# Here is my figure caption!
# ```
# ````
# 
# which will produce the following:
# 
# ```{figure} ../images/C-3PO_droid.png
# ---
# height: 150px
# name: directive-fig
# ---
# Here is my figure caption!
# ```

# In[ ]:




