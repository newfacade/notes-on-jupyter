#!/usr/bin/env python
# coding: utf-8

# # 使用 Jupyter notebooks
# 
# ```{note}
# Jupyter notebooks（.ipynb 文件） are documents that combine live runnable code with narrative text (Markdown), equations (LaTeX), images, interactive visualizations and other rich output.
# ```
# 
# Create a notebook by clicking the ``+`` button in the file browser and then selecting a kernel in the new Launcher tab:
# 
# ```{image} ../images/lab2.jpg
# :alt: notebook
# :class: bg-primary mb-1
# :width: 700px
# ```
# 
# Jupyter notebooks 支持三类 cell: Code, Markdown and Raw.

# ## 小技巧
# 
# * 可以 Drag and drop cells to rearrange your notebook.
# 
# * 可以先分屏，再 Drag cells between notebooks to quickly copy content.
# 
# * 可以在文件标题处右键选择 New View for Notebook 分屏，Create multiple synchronized views of a single notebook.
# 
# * 输出太长了，可以 Collapse and expand code and output using the View menu or the blue collapser button on left of each cell.
# 
# * 输出太长了，可以 Enable scrolling for long outputs by right-clicking on a cell and selecting “Enable Scrolling for Outputs”.

# ## 一些命令

# In[1]:


# 加 ! 转变为命令行命令
get_ipython().system('ls')


# In[2]:


# 运行脚本
get_ipython().run_line_magic('run', 'hello.py')


# In[3]:


# 监测代码运行时间
get_ipython().run_line_magic('timeit', '[x ** 2 for x in range(1000)] ')


# In[4]:


# 优雅地使用 matplotlib
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")

plt.plot([x ** 2 for x in range(1000)])
plt.show()


# In[5]:


# 设置 pandas 的输出
import pandas as pd
pd.set_option('display.max_rows', 1000)  # None 为不限制输出


# In[ ]:




