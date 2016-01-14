---
layout: post
title: "Testing IPython Notebook Integration"
tagline: "Testing"
author: Ken Cavagnolo
category: ipynotebooks
tags: [python, notebook, jupyter]
comments: true
---

# Define the problem

## What's the problem?
* Describe the problem informally, e.g. "I need a program that will tell me which tweets will get retweets."

* Describe the problem formally, e.g.
    * Task (T): Classify a tweet that has not been published as going to get retweets or not.
    * Experience (E): A corpus of tweets for an account where some have retweets and some do not.
    * Performance (P): Classification accuracy, the number of tweets predicted correctly out of all tweets considered as a percentage.

* List assumptions, e.g.
    * The specific words used in the tweet matter to the model.
    * The specific user that retweets does not matter to the model.
    * The number of retweets may matter to the model.
    * Older tweets are less predictive than more recent tweets.

* List similar problems, e.g. "A related problem would be email spam discrimination that uses text messages as input data and needs binary classification decision."

**In [41]:**

{% highlight python %}
import pandas as pd

data = '/Library/Python/2.7/site-packages/pandas/tests/data/iris.csv'
iris_data = pd.read_csv(data, na_values=['NA'])
iris_data.describe()
{% endhighlight %}




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SepalLength</th>
      <th>SepalWidth</th>
      <th>PetalLength</th>
      <th>PetalWidth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.843333</td>
      <td>3.054000</td>
      <td>3.758667</td>
      <td>1.198667</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.828066</td>
      <td>0.433594</td>
      <td>1.764420</td>
      <td>0.763161</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.300000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.100000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.100000</td>
      <td>2.800000</td>
      <td>1.600000</td>
      <td>0.300000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.800000</td>
      <td>3.000000</td>
      <td>4.350000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.400000</td>
      <td>3.300000</td>
      <td>5.100000</td>
      <td>1.800000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.900000</td>
      <td>4.400000</td>
      <td>6.900000</td>
      <td>2.500000</td>
    </tr>
  </tbody>
</table>
</div>



**In [5]:**

{% highlight python %}
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sb

sb.pairplot(iris_data.dropna(), hue='Name')
{% endhighlight %}




    <seaborn.axisgrid.PairGrid at 0x108963350>




![png]({{ site.baseurl }}/notebooks/test_files/test_3_1.png)


**In [34]:**

{% highlight python %}
iris_data.loc[
    (iris_data['SepalLength'] < 5.25) &
    (iris_data['PetalWidth'] > 0.75)
]
{% endhighlight %}




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SepalLength</th>
      <th>SepalWidth</th>
      <th>PetalLength</th>
      <th>PetalWidth</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>59</th>
      <td>5.2</td>
      <td>2.7</td>
      <td>3.9</td>
      <td>1.4</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>60</th>
      <td>5.0</td>
      <td>2.0</td>
      <td>3.5</td>
      <td>1.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>93</th>
      <td>5.0</td>
      <td>2.3</td>
      <td>3.3</td>
      <td>1.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>98</th>
      <td>5.1</td>
      <td>2.5</td>
      <td>3.0</td>
      <td>1.1</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>106</th>
      <td>4.9</td>
      <td>2.5</td>
      <td>4.5</td>
      <td>1.7</td>
      <td>Iris-virginica</td>
    </tr>
  </tbody>
</table>
</div>



**In [None]:**

{% highlight python %}

{% endhighlight %}
