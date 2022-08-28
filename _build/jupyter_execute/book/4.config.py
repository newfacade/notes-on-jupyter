#!/usr/bin/env python
# coding: utf-8

# # 配置项和目录
# 
# ```{note}
# 之前我们通过样书简单介绍了配置项（_config.yml）和目录（_toc.yml），这节我们来更详细地介绍它们。
# ```

# ## 配置项
# 
# 下面大部分都是 Configuration defaults
# 
# ### Book settings
# ```yaml
# # The title of the book. Will be placed in the left navbar.
# title                       : My Jupyter Book
# 
# # The author of the book
# author                      : The Jupyter Book community
# 
# # Copyright year to be placed in the footer
# copyright                   : "2022"
# 
# # A path to the book logo
# logo                        : ""
# 
# # Patterns to skip when building the book. Can be glob-style (e.g. "*skip.ipynb")
# exclude_patterns            : [_build, Thumbs.db, .DS_Store, "**.ipynb_checkpoints"]
# 
# # Auto-exclude files not in the toc
# only_build_toc_files        : false
# ```
# 
# ### Execution settings
# ```yaml
# execute:
#   # Whether to execute notebooks at build time. 
#   # Must be one of ("auto", "force", "cache", "off")
#   execute_notebooks         : auto
#   
#   # The maximum time (in seconds) each notebook cell is allowed to run.
#   timeout                   : 30
#   
#   # If `False`, when a code cell raises an error the execution is stopped.
#   allow_errors              : false
# ```
# 
# ### HTML-specific settings
# 
# ```yaml
# html:
#   favicon                   : ""  # A path to a favicon image
# ```
# 
# ### Citations and bibliographies
# 
# ```yaml
# bibtex_bibfiles:
#     - references.bib  # A path to bibtex file
# ```

# ## 目录
# 
# 可以按 part-chapter-section 组织，就像（`注意格式`）：
# 
# ```yaml
# format: jb-book
# root: index
# parts:
#   - caption: Name of Part 1
#     chapters:
#     - file: path/to/part1/chapter1
#     - file: path/to/part1/chapter2
#       sections:
#       - file: path/to/part1/chapter2/section1
#   - caption: Name of Part 2
#     chapters:
#     - file: path/to/part2/chapter1
#     - file: path/to/part2/chapter2
#       sections:
#       - file: path/to/part2/chapter2/section1
# ```

# In[ ]:




