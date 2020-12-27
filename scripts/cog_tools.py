# copyright Janto Dreijer

from pathlib import Path

import numpy as np

import seaborn as sns

sns.set_theme()
sns.set_style("darkgrid")

import pandas as pd
import pylab

import matplotlib.pyplot as plt
import pylab

plt.viridis()  # better colormap


import cog

# ----------------------
# common tools


def comment(item):
    cog.outl(f"<!-- {str(item)} -->")

# ----------------------
# python code blocks and output


def print_block(item):
    """Output python codeblock with str(item)"""
    comment("START print_block() output")
    cog.outl(f"```python\n{item}\n```")
    comment("STOP print_block() output")


def exec_python_block_and_output(code, _globals, _locals, inter="result:"):
    """remove md wrappers, execute and write md wrapped output"""
    code = "\n".join(code.split("\n")[2:-2])
    _globals = _globals.copy()
    _globals["print"] = print_block  # override in code
    cog.outl(inter)
    return exec(code, _globals, _locals)
