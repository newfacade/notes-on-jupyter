#!/usr/bin/env python
# coding: utf-8

# # Build your book
# 
# 在创建好一系列的 notebook/Markdown 内容文件，编辑好配置文件 `_config.yml` 和目录文件 `_toc.yml` 后。<br/>
# Now build the HTML for your book by runing the following command:
# 
# ```
# jupyter-book build mybookname/
# ```
# 
# 这会生成一个 fully-functioning HTML site, the site will be placed in the _build/html folder, something like this:
# 
# ```
# mybookname
#  └──_build
#     └── html
#        ├── _images
#        ├── _static
#        ├── index.html
#        ├── intro.html
#        ...
# ```
# 
# These are the static files for a standalone website! They contain the HTML and all assets needed to view your book in a browser.
# 
# 现在点击 `index.html` 就可以本地预览啦！

# In[ ]:




