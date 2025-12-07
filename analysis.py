# Marimo interactive notebook
# Author: 23f3001018@ds.study.iitm.ac.in
# This notebook demonstrates variable relationships with interactive widgets.

import marimo as mo

# --- Cell 1: Load or create data ------------------------------------------
# Data flow: x_values is used by later cells for analysis.
x_values = list(range(1, 101))  # example dataset

# --- Cell 2: Widget input --------------------------------------------------
# Data flow: slider_value influences computed_y and dynamic markdown.
slider = mo.ui.slider(1, 100, label="Select multiplier")

slider

# --- Cell 3: Compute dependent variable ------------------------------------
# computed_y depends on both x_values and the slider widget.
computed_y = [x * slider.value for x in x_values]

computed_y[:10]   # preview first 10 values

# --- Cell 4: Dynamic Markdown output ---------------------------------------
# Data flow: markdown updates reactively whenever slider.value changes.
mo.md(f"""
## Interactive Data Relationship

The slider value is: **{slider.value}**

This controls the computation:  
`y = x * {slider.value}`

### Sample Output  
First 10 computed values:  
**{computed_y[:10]}**
""")
