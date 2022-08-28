#!/usr/bin/env python
# coding: utf-8

# # 发布到网上
# 
# ```{note}
# Once you’ve built the HTML for your book, you can host it online. In this tutorial, we’ll cover how to publish your book online with GitHub Pages.
# ```

# ## 创建 GitHub 仓库
# 
# In order to connect your hosted book with your book’s source content, you should put your book’s source content in a public repository.
# 
# 1.在 <https://github.com/new> 创建一个新的 repository,` Make your repository public and do not initialize it with a README file`.
# 
# 2.Clone the (currently empty) online repository to a location on your local computer:
# 
# ```
# git clone https://github.com/<user>/<my-repository-name>
# ```
# 
# 3.Copy all of your book files and folders into this newly cloned repository:
# 
# ```
# cp -r mybookname/* myonlinebook/
# ```
# 
# 4.同步 local and remote repositories:
# 
# ```
# cd myonlinebook
# git add ./*
# git commit -m "adding my first book!"
# git push
# ```

# ## 发布到网上
# 
# We have just pushed the `source files` for our book into our GitHub repository. This makes it publicly accessible for you or others to see.
# 
# 将书发布到 Github 需要借助工具 `ghp-import`，可以通过如下命令安装：
# 
# ```md
# pip install ghp-import
# ```
# 
# 然后在本地的 myonlinebook/ 文件夹下执行如下命令：
# 
# ```md
# ghp-import -n -p -f _build/html
# ```
# 
# Typically after a few minutes your site should be viewable online at a url such as: `https://<user>.github.io/<myonlinebook>/`.

# In[ ]:




