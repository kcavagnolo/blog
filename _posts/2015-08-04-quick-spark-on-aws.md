---
layout: post
title: Start an AWS Spark Cluster in 5 Minutes
author: Ken Cavagnolo
category : lessons
tags: [spark, python, aws, osx]
comments: true
---

{% include JB/setup %}

<div class="blurb">

<p>When tackling a new project, I will hit an ostensibly simple, yet
very specific, problem at which point I search reference material for
an answer. I have no qualms relying on reference material for two
reasons:

<ul>
<li>I have a memory leak and things I learn I unlearn.</li>
<li>I learned in grad school that it's more important how one thinks
rather than what one knows -- assuming some base knowledge to allow
thinking through a problem.</li>
</ul>

I'm an avid consumer and contributor at <a
href="http://stackoverflow.com/" target="_blank">Stackoverflow</a>,
and when on my Mac, I'm a devout user of <a
href="https://kapeli.com/dash" target="_blank">Dash Docs</a>
integrated via <a href="https://www.alfredapp.com/"
target="_blank">Alfred</a>. As a data science person, these resources,
along with blogs, are exceptionally useful for niche problems or tasks
many developers consider trivial or obvious, for example quickly
setting up a Spark cluster on AWS. <b>Note: I'm a savage and use tcsh
for my shell language.</b> First, <a
href="https://aws-portal.amazon.com/gp/aws/developer/registration/index.html"
target="_blank">create an AWS account</a> and <b>retain your access
and secret keys</b>. Using those keys, set some local environment
variables so you can reference them later:
{% highlight tcsh %}
[local]$ echo 'setenv AWS_ACCESS_KEY "your-aws-access-key-id"' >> ~/.cshrc
[local]$ echo 'setenv AWS_SECRET_KEY "your-aws-secret-key"' >> ~/.cshrc
[local]$ source ~/.cshrc
[local]$ setenv

stuff...
AWS_ACCESS_KEY=<your key>
AWS_SECRET_KEY=<your secret>
{% endhighlight %}

Now <a href="http://aws.amazon.com/cli/" target="_blank">install the
AWS command line interface (CLI)</a> which is much simpler for
accessing AWS than the console:

{% highlight tcsh%}
[local]$ wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip
[local]$ unzip awscli-bundle.zip
[local]$ wget sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
[local]$ rehash; aws ec2 describe-regions
[local]$ rm -rf awscli-bundle*
{% endhighlight %}

To access the cluster, you'll need an ssh keypair. Amazon recommends
using their IAM profiles now since the CLI keys are global access to
your account. That's a risk/simplicity left to you:

{% highlight tcsh %}
[local]$ aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > ~/.ssh/aws.pem
[local]$ chmod 400 ~/.ssh/aws.pem
{% endhighlight %}

With the keys on your machine and in your AWS account, you can now build a cluster:

{% highlight tcsh %}
[local]$ aws emr create-cluster --name SparkCluster --release-label emr-4.2.0 --applications Name=Spark --ec2-attributes KeyName=my-key-pair --instance-type m3.xlarge --instance-count 3 --use-default-roles

{
    "ClusterId": "j-2036HWS8HJGNM"
}
{% endhighlight %}

Check that it's running as expected, this can take 1-10 minutes sometimes:

{% highlight tcsh %}
[local]$ aws emr list-clusters

stuff...

"Id": "j-2AL4XXXXXX5T9",

...more stuff
{% endhighlight %}

Let's connect to the master node of our fresh little cluster:

{% highlight tcsh %}
[local]$ aws emr ssh --cluster-id j-2AL4XXXXXX5T9 --key-pair-file ~/.ssh/aws.pem
[hadoop@aws]$ spark-shell

...lots of init stuff

scala>
{% endhighlight %}

Cool, this thing is live! Now you can dump any kind of Spark code here
and run days or years of computations in minutes to hours. For example
<a href="http://spark.apache.org/examples.html" target="_blank">brute
force estimating pi</a> to nine digits (about 24 hours of calculation
time in a few seconds):

{% highlight scala %}
scala> sc
res0: org.apache.spark.SparkContext = org.apache.spark.SparkContext@334e0329

scala> val NUM_SAMPLES = 1000000000
val count = sc.parallelize(1 to NUM_SAMPLES).map{i =>
  val x = Math.random()
  val y = Math.random()
  if (x*x + y*y < 1) 1 else 0
}.reduce(_ + _)
println("Pi is roughly " + 4.0 * count / NUM_SAMPLES)

Pi is roughly 3.141629432
{% endhighlight %}

Always be sure to terminate the cluster unless you like spending money:
{% highlight tcsh%}
[hadoop@aws]$ exit
[local]$ aws emr terminate-clusters --cluster-id j-2Z284KB7CTY20
{% endhighlight %}

</div>
