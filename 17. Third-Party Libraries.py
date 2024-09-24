"""
Modules are pre-written code libraries that provide additional functionality. However, it is different from standard libraries which comes pre-installed with Python.
Import modules require separate installation by typing pip install -r requirements.txt (Python Package Installer) and it is not part of standard Python distribution as it is developed by third-party.

Examples of External Libraries:
1. numpy: The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
2. pandas: A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
3. requests: Provides easy to use methods to make web requests. Useful for accessing web APIs.
4. flask: a lightweight framework for making web applications and APIs.
5. scikit-learn

When to Use Each:
Standard Library: For basic tasks, such as file I/O, mathematical operations, or data type conversions.
External Libraries: For specialized tasks, such as data analysis (pandas), web development (flask), or machine learning (scikit-learn).

Example Use Case:
Suppose you want to perform statistical analysis on a dataset.
For basic statistical calculations, use the standard library math.
For advanced data analysis, use an external library like pandas or numpy.

import math #Using standard library (math) for basic statistics
data = [1, 2, 3, 4, 5]
mean = sum(data) / len(data)
std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
print(f"Mean: {mean}, Standard Deviation: {std_dev}")

import pandas as pd #Using external library (pandas) for advanced data analysis
data = pd.Series([1, 2, 3, 4, 5])
print(f"Mean: {data.mean()}, Standard Deviation: {data.std()}")
"""
