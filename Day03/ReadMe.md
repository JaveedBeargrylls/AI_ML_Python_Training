### Topics Discussed on Day 03

How to merge two DataFrames (`data1` and `data2`) using different types of joins (like SQL joins).

### Step 1: Creating the DataFrames

First, you define two dictionaries (`info` and `customer`), which contain some customer data:

```python
info = {
    "name": ["jhon", "abhi", "Jessica", "ankit"],
    "age": [23, 34, 45, 23],
    "cc_score": [678, 789, 810, 450],
    "id": [1, 3, 4, 6]
}

customer = {
    "id": [1, 3, 0, 8, 9],
    "salary": [9078, 8978.09, 897687, 8989, 4524],
    "gender": ["male", "male", "female", "male", "female"]
}
```

- `info` contains **customer names**, **ages**, **credit card scores**, and **IDs**.
- `customer` contains **IDs**, **salaries**, and **genders** of customers.

Next, you create `pandas` DataFrames from these dictionaries:

```python
data1 = pd.DataFrame(info)
data2 = pd.DataFrame(customer)
```

The resulting DataFrames look like this:

**`data1`**:

| name    | age | cc_score | id |
|---------|-----|----------|----|
| jhon    | 23  | 678      | 1  |
| abhi    | 34  | 789      | 3  |
| Jessica | 45  | 810      | 4  |
| ankit   | 23  | 450      | 6  |

**`data2`**:

| id | salary   | gender |
|----|----------|--------|
| 1  | 9078.00  | male   |
| 3  | 8978.09  | male   |
| 0  | 897687   | female |
| 8  | 8989.00  | male   |
| 9  | 4524.00  | female |

### Step 2: Merging the DataFrames

Now, you will perform **merge operations** on these DataFrames using the common column `id`.

### 1. **Inner Join**:

```python
print(pd.merge(data1, data2, on='id', how='inner'))
```

An **inner join** returns only the rows where **both DataFrames have matching values for the specified key (`id` in this case)**. If an `id` exists in `data1` but not in `data2`, or vice versa, those rows will be excluded from the result.

- For example, the IDs `1` and `3` appear in both `data1` and `data2`, so they will be kept in the result.

**Result (inner join)**:

| name    | age | cc_score | id | salary   | gender |
|---------|-----|----------|----|----------|--------|
| jhon    | 23  | 678      | 1  | 9078.00  | male   |
| abhi    | 34  | 789      | 3  | 8978.09  | male   |

### 2. **Outer Join**:

```python
print(pd.merge(data1, data2, on='id', how='outer'))
```

An **outer join** returns all the rows from **both DataFrames**. If a row in one DataFrame doesn't have a match in the other DataFrame, the result will contain `NaN` for the missing values.

- All the `id` values from both `data1` and `data2` are included, and where there is no match, the respective columns will have `NaN`.

**Result (outer join)**:

| name    | age  | cc_score | id | salary   | gender |
|---------|------|----------|----|----------|--------|
| jhon    | 23   | 678      | 1  | 9078.00  | male   |
| abhi    | 34   | 789      | 3  | 8978.09  | male   |
| Jessica | 45   | 810      | 4  | NaN      | NaN    |
| ankit   | 23   | 450      | 6  | NaN      | NaN    |
| NaN     | NaN  | NaN      | 0  | 897687   | female |
| NaN     | NaN  | NaN      | 8  | 8989.00  | male   |
| NaN     | NaN  | NaN      | 9  | 4524.00  | female |

### 3. **Left Join**:

```python
print(pd.merge(data1, data2, on='id', how='left'))
```

A **left join** returns all the rows from the **left DataFrame (`data1`)**, and only the matching rows from the **right DataFrame (`data2`)**. If there is no match, the right DataFrame’s columns will contain `NaN`.

- All rows from `data1` are kept. For rows in `data1` that don’t have a match in `data2`, you'll see `NaN` for the `salary` and `gender`.

**Result (left join)**:

| name    | age | cc_score | id | salary  | gender |
|---------|-----|----------|----|---------|--------|
| jhon    | 23  | 678      | 1  | 9078.00 | male   |
| abhi    | 34  | 789      | 3  | 8978.09 | male   |
| Jessica | 45  | 810      | 4  | NaN     | NaN    |
| ankit   | 23  | 450      | 6  | NaN     | NaN    |

### 4. **Right Join**:

```python
print(pd.merge(data1, data2, on='id', how='right'))
```

A **right join** returns all the rows from the **right DataFrame (`data2`)**, and only the matching rows from the **left DataFrame (`data1`)**. If there is no match, the left DataFrame’s columns will contain `NaN`.

- All rows from `data2` are kept. For rows in `data2` that don’t have a match in `data1`, you'll see `NaN` for the `name`, `age`, and `cc_score` columns.

**Result (right join)**:

| name    | age  | cc_score | id | salary  | gender |
|---------|------|----------|----|---------|--------|
| jhon    | 23   | 678      | 1  | 9078.00 | male   |
| abhi    | 34   | 789      | 3  | 8978.09 | male   |
| NaN     | NaN  | NaN      | 0  | 897687  | female |
| NaN     | NaN  | NaN      | 8  | 8989.00 | male   |
| NaN     | NaN  | NaN      | 9  | 4524.00 | female |

---

### Summary of Merge Types:

1. **Inner Join** (`how='inner'`): Only keeps rows where `id` matches in both DataFrames.
2. **Outer Join** (`how='outer'`): Keeps all rows from both DataFrames, filling missing values with `NaN`.
3. **Left Join** (`how='left'`): Keeps all rows from the left DataFrame and only the matching rows from the right.
4. **Right Join** (`how='right'`): Keeps all rows from the right DataFrame and only the matching rows from the left.

---
---
---

Here’s a list of the main plotting functions we can  use from **Matplotlib** and **Seaborn**:

### From **Matplotlib** (`import matplotlib.pyplot as plt`):
1. **`plt.plot()`** – Line plot
2. **`plt.hist()`** – Histogram
3. **`plt.scatter()`** – Scatter plot
4. **`plt.bar()`** – Bar chart
5. **`plt.barh()`** – Horizontal bar chart
6. **`plt.pie()`** – Pie chart
7. **`plt.boxplot()`** – Box plot
8. **`plt.subplot()`** – Multiple plots in a single figure
9. **`plt.grid()`** – Add gridlines
10. **`plt.title()`** – Set title for the plot
11. **`plt.xlabel()`** – Set x-axis label
12. **`plt.ylabel()`** – Set y-axis label
13. **`plt.legend()`** – Add legend
14. **`plt.xlim()`** – Set x-axis limits
15. **`plt.ylim()`** – Set y-axis limits

### From **Seaborn** (`import seaborn as sns`):
1. **`sns.histplot()`** – Histogram with options for density plots
2. **`sns.countplot()`** – Count plot (categorical data)
3. **`sns.boxplot()`** – Box plot
4. **`sns.violinplot()`** – Violin plot
5. **`sns.scatterplot()`** – Scatter plot
6. **`sns.lineplot()`** – Line plot
7. **`sns.barplot()`** – Bar plot
8. **`sns.kdeplot()`** – Kernel Density Estimation plot
9. **`sns.pairplot()`** – Pairwise relationship plots
10. **`sns.heatmap()`** – Heatmap (often used for correlation matrices)
11. **`sns.regplot()`** – Regression plot
12. **`sns.lmplot()`** – Linear model plot (with regression)
13. **`sns.jointplot()`** – Joint plot (showing bivariate relationships)
14. **`sns.factorplot()`** (deprecated, but still usable) – Factor plot (for categorical data visualization)
15. **`sns.heatmap()`** – Heatmap for correlation matrices or other data

---

### Summary:

- **Matplotlib** provides a wide range of basic plotting functions, including line plots, histograms, bar charts, scatter plots, and more.
- **Seaborn** builds on **Matplotlib** and provides more specialized functions for statistical plots, such as `countplot`, `heatmap`, `pairplot`, and more.
