#!/usr/bin/env python
# coding: utf-8

# # Markdown 语法
# 
# 参考资料：<https://www.markdownguide.org/basic-syntax/>

# ## 标题
# 
# * 一级标题：`# Heading level 1`
# * 二级标题：`## Heading level 2`
# * 三级标题：`### Heading level 3`
# 
# ```{caution}
# Always put a space between the number signs and the heading name.<br>
# You should also put blank lines before and after a heading for compatibility.
# ```

# ## 段落
# 
# To create paragraphs, 使用一个空行 to separate one or more lines of text.
# 
# If you need to indent paragraphs，在行首加上 `&nbsp;`，它表示按 Space 键产生的空格，可叠加。

# ## 换行
# 
# To create a line break or new line (`<br>`), end a line with two or more spaces, and then type return.
# 
# This is the first line.  
# And this is the second line.
# 
# 最好是显式地使用 `<br>`，因为这样不容易出错。

# ## 强调
# 
# ### 黑体
# 
# `I just love **bold text**.` 会被渲染为 I just love **bold text**.
# 
# ### 斜体
# 
# `Italicized text is the *cat's meow*.` 会被渲染为 Italicized text is the *cat's meow*.
# 
# ### 又黑又斜
# 
# `This text is ***really important***.` 会被渲染为 This text is ***really important***.

# ## 列表
# 
# ### 有序列表
# 
# ```
# 1. First item
# 2. Second item
# 3. Third item
# ```
# 
# 会被渲染为
# 
# 1. First item
# 2. Second item
# 3. Third item
# 
# ### 无序列表
# 
# ```
# - First item
# - Second item
# ```
# 
# 会被渲染为
# 
# * First item
# * Second item
# 
# 其中 `-` 也可以用 `*` or `+` or `-` 替代。
# 
# ### 在列表中添加其它东西
# 
# To add another element in a list while preserving the continuity of the list, indent the element four spaces or one tab, as shown in the following examples.
# 
# ```
# * This is the first list item.
# * Here's the second list item.
# 
#     I need to add another paragraph below the second list item.
# 
# * And here's the third list item.
# ```
# 
# The rendered output looks like this:
# 
# * This is the first list item.
# * Here's the second list item.
# 
#     I need to add another paragraph below the second list item.
# 
# * And here's the third list item.

# ## Blockquotes
# 
# To create a blockquote, add a > in front of a paragraph.
# 
# ```
# > Dorothy followed her through many of the beautiful rooms in her castle.
# ```
# 
# The rendered output looks like this:
# 
# > Dorothy followed her through many of the beautiful rooms in her castle.
# 
# ### Blockquotes with Multiple Paragraphs
# 
# Blockquotes can contain multiple paragraphs. Add a > on the blank lines between the paragraphs.
# 
# ```
# > Dorothy followed her through many of the beautiful rooms in her castle.
# >
# > The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
# ```
# 
# The rendered output looks like this:
# 
# > Dorothy followed her through many of the beautiful rooms in her castle.
# >
# > The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
# 
# ### Nested Blockquotes
# 
# Blockquotes can be nested. Add a >> in front of the paragraph you want to nest.
# 
# ```
# > Dorothy followed her through many of the beautiful rooms in her castle.
# >
# >> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
# ```
# 
# The rendered output looks like this:
# 
# > Dorothy followed her through many of the beautiful rooms in her castle.
# >
# >> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
# 
# ### Blockquotes with Other Elements
# 
# Blockquotes can contain other Markdown formatted elements.
# 
# ```
# > - Revenue was off the chart.
# > - Profits were higher than ever.
# >
# >  *Everything* is going according to **plan**.
# ```
# 
# The rendered output:
# 
# > - Revenue was off the chart.
# > - Profits were higher than ever.
# >
# >  *Everything* is going according to **plan**.

# ## 代码块
# 
# To denote a word or phrase as code, enclose it in backticks (`).

# ### Horizontal Rules
# 
# ```
# ***
# 
# ---
# 
# _________________
# ```
# 
# The rendered output of all three looks identical:
# 
# ***

# ## 链接
# 
# To create a link, enclose the link text in brackets (e.g., [Duck Duck Go]) and then follow it immediately with the URL in parentheses (e.g., (https://duckduckgo.com)).
# 
# ```
# My favorite search engine is [Duck Duck Go](https://duckduckgo.com).
# ```
# 
# The rendered output looks like this:
# 
# My favorite search engine is [Duck Duck Go](https://duckduckgo.com).
# 
# ### URLs and Emails
# 
# ```
# <https://www.markdownguide.org>
# <fake@example.com>
# ```
# 
# The rendered output:
# 
# <https://www.markdownguide.org>
# <fake@example.com>

# ## 图片
# 
# To add an image, add an exclamation mark (!), followed by alt text（是为了给那些不能看到你文档中图像的浏览者提供文字说明） in brackets, and the path or URL to the image asset in parentheses.
# 
# ```
# ![mona](../images/mona.jpeg)
# ```
# 
# The rendered output:
# 
# ![mona](../images/mona.jpeg)

# In[ ]:




