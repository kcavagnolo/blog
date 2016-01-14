---
layout: post
title: "Plotly Integration"
tagline: "Testing functionality"
author: Ken Cavagnolo
category : ipynotebooks
tags: [python, notebook, jupyter]
comments: true
---

<p>Everything needed to get plotly graphics into an ipynb is provided
here: <a href="https://plot.ly/python/ipython-notebook-tutorial"
target="_blank">Plotly Tutorial</a></p>

<p>In order to make the process described in the <a href="{% post_url
2015-06-04-ipynb-testing %}" target="_blank">IPython Notebook
Integration post</a> function correctly, it needs a tweak. Plotly
images have tags that sometimes lose their whitespace, e.g. note the
lack of whitespace between the tags style and seamless
<code>style="border:none;"seamless="seamless"</code>. This causes the
iframe containing the Plotly image to not render correctly. To fix the
figures, I run the below on the output ipynb:</p>
<script src="https://gist.github.com/kcavagnolo/b9872a0f14ab6bd9a229.js"></script>

**In [1]:**

{% highlight python %}
# plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
tls.set_credentials_file(username='test_user', api_key='**********')

#matplotlib and stuff
import matplotlib.pyplot as plt
%matplotlib inline
{% endhighlight %}

**In [5]:**

{% highlight python %}
# get some data
datadir = '/home/kcavagnolo/data/some_data/'
raw_data = datadir+'data.csv'
{% endhighlight %}

**In [33]:**

{% highlight python %}
# build a plot
mpl_fig_bubble = plt.figure()
ax = mpl_fig_bubble.add_subplot(111)

plt.axis([0, 120, 0, 120])
plt.title('Total Snowfall Per County Nov 1, 2014 to Apr 1, 2015')
plt.xlabel('Measured [in]')
plt.ylabel('Forecasted [in]')

scatter = ax.scatter(
    df['observed'], # x
    df['forecasted'], # y
    c = df['forecasted'], # color scale
    s = np.square(df['observed']), # size scale
    linewidths = 2,
    edgecolor = 'w',
    alpha = 0.6,
    label = df['county']
)

for i_X, X in df.iterrows():
    plt.text(
        X['observed'],
        X['forecasted'],
        X['county'][0:5],
        size=10,
        horizontalalignment='center'
    )

x = range(-1000,1000)
y = x
plt.plot(x, y, label='Equality')
    
# make plotly
py.iplot_mpl(mpl_fig_bubble)#, strip_style=True)
{% endhighlight %}




<iframe id="igraph" scrolling="no" link="False" autosize="True" style="border:none;" seamless="seamless" src="https://plot.ly/~kcavagnolo/178.embed" height="525px" width="100%"></iframe>


