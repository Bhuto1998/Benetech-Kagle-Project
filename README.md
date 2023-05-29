# Description

Let's now dive into what the problem really is, I will do that in a separate notebook named exploratory data analysis and stored the results I got from that in this notebook.

**Goal of the Competition**

* Millions of students experience **learning, physical, or visual disabilities** that prevent them from accessing conventional print. A large proportion of **STEM (science, technology, engineering, and math)** educational materials remains inaccessible to these students.
* The competition aims to address this challenge by creating an automatic solution to interpret and extract data from **four types of charts** typically found in STEM textbooks.
* Current processes to make educational materials accessible are **manual, expensive, time-consuming**, and require multiple rounds of quality checks. This often means these materials aren't accessible to schools or teachers with insufficient funding.
* The challenge involves leveraging **machine learning techniques** to make the written word accessible to all, potentially benefiting millions of students with learning differences or disabilities.

**Context**

* The competition is hosted by **Benetech**, a nonprofit organization committed to reducing social and economic disparities through 'software for social good'. Benetech's initiatives strive to make education, literacy, and employment more accessible to those with differences or disabilities.
* The best solutions from the competition will be integrated into **Benetech's PageAI product**, a tool that converts books and other educational materials into accessible formats. This could make accessible STEM education a reality for millions of students with learning differences or disabilities.

**Competition Objective**

* The aim of the competition is to predict the data series represented by four types of scientific charts: **bar graphs, dot plots, line graphs, and scatter plots**.
* For detailed information on what kind of predictions to make for each chart type, please refer to the page [Graph Conventions](https://www.example.com).
* A Python implementation of the evaluation metric is provided in the notebook [Benetech Competition Metric](https://www.example.com).

**Evaluation Metric**

* The data series of a single figure includes two instances for evaluation: the series of values along the **x-axis** and the **y-axis**. Each data series can be either numerical or categorical, depending on the chart type.
* Predicted data series are evaluated using a combination of **Levenshtein distance** for categorical data types and **RMSE (Root Mean Square Error)** for numerical data types. An exact-match criterion is initially applied for the chart type and the number of values in the series. These distances are then rescaled and mapped to a common similarity scale by a sigmoid-type transform with an optimum value of 1.
* Evaluation of a single instance consists of first checking the number of values and type of chart predicted for a series. If these differ from the ground truth, the score for that series is zero. Otherwise, the predicted series is evaluated based on the data type of that series.
* For numerical series, predictions are evaluated by a normalized RMSE.
* For categorical series, predictions are evaluated by a normalized Levenshtein distance.
* The overall score is the mean of the similarity scores over all instances.

**Submission File**

* Each row in the submission file should contain predicted series for one axis of a figure in the test set. The series values should be within a single string and separated by a semicolon (;). Also, the appropriate type for the chart the axis belongs to should be specified.
* The file should contain a header and follow this format:

```
id,data_series,chart_type
abc123_x,2;3;4;5,horizontal_bar
abc123_y,a;b;c;d,horizontal_bar
```

### **Data Prediction Conventions for Different Scientific Figure Types** <a href="#data-prediction-conventions-for-different-scientific-figure-types" id="data-prediction-conventions-for-different-scientific-figure-types"></a>

This section provides guidelines on how to make consistent predictions across a variety of chart formats.

**General Rules:**

* Categorical values always correspond to a tick label on an axis.
* Numerical values must be inferred from the tick labels through interpolation.

### **1. Bar Charts** <a href="#1.-bar-charts" id="1.-bar-charts"></a>

* Bar charts in the dataset can be vertical or horizontal. Vertical bar charts have independent values on the x-axis and dependent values on the y-axis. The reverse is true for horizontal bar charts.
* Independent values are always categorical and are identified by the tick labels below each bar. Dependent values are always numeric and are identified by the bar's height or length.
* Bar charts may also be histograms where x labels occur at each bar's ends. For scoring purposes, the x-axis values are treated as categorical type, not numeric.

### **2. Dot Plots** <a href="#2.-dot-plots" id="2.-dot-plots"></a>

* Dot plots have independent values on the x-axis and dependent values on the y-axis.
* The x-axis values will be numeric if the tick labels can be parsed as Python floats; otherwise, they are categorical.
* The y-axis values represent the number of dots in each column.

### **3. Line Graphs** <a href="#3.-line-graphs" id="3.-line-graphs"></a>

* Line graphs always have categorical x-axis values and numeric y-axis values.
* X-axis values are the tick labels beneath some portion of the line graph.
* Y-axis values are the corresponding dependent values indicated by the graph.

### **4. Scatter Plots** <a href="#4.-scatter-plots" id="4.-scatter-plots"></a>

* Scatter plots always have numeric x-axis values and numeric y-axis values.
* Predict both x and y values for each point present in the figure.

**Other Notes and Conventions:**

* For a numerical axis, a percentage like X% is labeled as the number X, not X/100.
* With one exception, both series for a figure will have the same number of values. With histograms, the x-axis series has an additional value.
* A figure may contain annotations with value labels. These values may differ from ground-truth values, which are calculated based on the positioning of graphical elements on the page.
* In the absence of an obvious corresponding tick/tick label pair, the center of the bounding box should be used for vertical/horizontal labels or the top corner of the bounding box for diagonal labels.
