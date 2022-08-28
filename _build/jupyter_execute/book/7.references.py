#!/usr/bin/env python
# coding: utf-8

# # References and Citations
# 
# ```{note}
# References allow you to refer to other content in your book or to external content.<br/>
# Citations（引用） and bibliographies（参考书目） allow you to cite scholarly work and provide bibliographies that allow readers to follow the references.
# ```

# ## References
# 
# Cross-references in Jupyter Book usually involve two things:
# 
# 1. Create a label for something.
# 2. Create a reference with a target.
# 
# ### 创建 label
# 
# Labels must come just before headers.
# 
# ```md
# (my-label)=
# ## My header
# 
# Some text
# ```
# 
# This is how you specify a label called `my-label` that points to the header just below (`## My header`).
# 
# ### Refer to your label
# 
# Now that you’ve created a label, you can refer to it from elsewhere.
# 
# ```md
# Here's some text and [here's my label](my-label).
# ```
# 
# 其中中括号内是 refer 应当显示的 text.

# ## Citations
# 
# 首先你需要一个 bibtex file 用于存放所需的 citations. 比如说在样书（sample book）中就有 `references.bib`
# 
# ```
# # In references.bib
# @inproceedings{holdgraf_evidence_2014,
# 	address = {Brisbane, Australia, Australia},
# 	title = {Evidence for {Predictive} {Coding} in {Human} {Auditory} {Cortex}},
# 	booktitle = {International {Conference} on {Cognitive} {Neuroscience}},
# 	publisher = {Frontiers in Neuroscience},
# 	author = {Holdgraf, Christopher Ramsay and de Heer, Wendy and Pasley, Brian N. and Knight, Robert T.},
# 	year = {2014}
# }
# ```
# 
# 然后需要再 `_config.yml` 中包括进这个 bibtex file:
# 
# ```yaml
# bibtex_bibfiles:
#     - references.bib
# ```
# 
# In your content, add the following syntax to include a citation:
# 
# ```md
# Here is my nifty citation {cite}`holdgraf_evidence_2014`.
# ```
# 
# 它会被渲染为：
# 
# Here is my nifty citation {cite}`holdgraf_evidence_2014`.
# 
# 
# ## Bibliography
# 
# Finally, we’ll generate a bibliography for our citations. Links to this bibliography will automatically be created when you cite something.
# 
# 点击任一引用时会自动跳转到 bibliography 的相关条目，我们使用如下语句来添加 bibliography:
# 
# ````
# ```{bibliography}
# ```
# ````
# 
# 它会被渲染为：
# 
# ```{bibliography}
# ```

# In[ ]:




