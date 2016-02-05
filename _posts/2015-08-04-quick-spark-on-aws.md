---
layout: post
title: AWS Spark Cluster in 5 Minutes
tagline: How-to create and access a Spark cluster for ad hoc analysis or big jobs
author: Ken Cavagnolo
category : lessons
tags: [spark, python, aws, osx]
comments: true
---

{% include JB/setup %}

<div class="blurb">

<p><b>UPDATE: If you have Spark 1.6.0 installed locally, the
reliability of the spark-ec2 script family has been improved and makes
the below process much simpler -- <a
href="http://spark.apache.org/docs/latest/ec2-scripts.html"
target="_blank">see this link</a>. I've updated the post with the
alternative method at the bottom.</b></p>

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
<br><br>
{% highlight tcsh %}
[local]$ echo 'setenv AWS_ACCESS_KEY_ID "your-aws-access-key-id"' >> ~/.cshrc
[local]$ echo 'setenv AWS_SECRET_ACCESS_KEY "your-aws-secret-key"' >> ~/.cshrc
[local]$ source ~/.cshrc
[local]$ setenv

stuff...
AWS_ACCESS_KEY_ID=<your key>
AWS_SECRET_ACCESS_KEY=<your secret>
{% endhighlight %}

Now <a href="http://aws.amazon.com/cli/" target="_blank">install the
AWS command line interface (CLI)</a> which is much simpler for
accessing AWS than the console:
<br><br>
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
<br><br>
{% highlight tcsh %}
[local]$ aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > ~/.ssh/aws.pem
[local]$ chmod 400 ~/.ssh/aws.pem
{% endhighlight %}

With the keys on your machine and in your AWS account, you can now build a cluster:
<br><br>
{% highlight tcsh %}
[local]$ aws emr create-cluster --name SparkCluster --release-label emr-4.2.0 --applications Name=Spark --ec2-attributes KeyName=MyKeyPair --instance-type m3.xlarge --instance-count 3 --use-default-roles

{
    "ClusterId": "j-2036HWS8HJGNM"
}
{% endhighlight %}

Check that it's running as expected, this can take 1-10 minutes sometimes:
<br><br>
{% highlight tcsh %}
[local]$ aws emr list-clusters

stuff...

"Id": "j-2AL4XXXXXX5T9",

...more stuff
{% endhighlight %}

Let's connect to the master node of our fresh little cluster:
<br><br>
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
<br><br>
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
<br><br>
{% highlight tcsh%}
[hadoop@aws]$ exit
[local]$ aws emr terminate-clusters --cluster-id j-2Z284KB7CTY20
{% endhighlight %}

Below is an alternative method to build a cluster on AWS if you have
Spark installed locally. Add the ec2 folder to your path:
<br><br>
{% highlight tcsh %}
[local]$ echo 'set path=($SPARK_HOME/bin $SPARK_HOME/ec2 $path)' >> ~/.cshrc
[local]$ spark-ec2 -k MyKeyPair -i ~/.ssh/aws.pem -s 2 launch MySparkCluster --instance-type=m3.xlarge --region=us-east-1 --copy-aws-credentials

...lots of stuff...
Spark standalone cluster started at http://ec2-52-91-9-214.compute-1.amazonaws.com:8080
{% endhighlight %}

After the cluster is live (takes ~10m for all the tools to build and
instlal), check the status using the link provided at the end,
something like http://<master-hostname>:8080. You can also just ssh in:
<br><br>
{% highlight tcsh %}
[local]$ ssh -i ~/.ssh/aws.pem root@ec2-52-91-9-214.compute-1.amazonaws.com

[aws_spark]$ cd spark
[aws_spark]$ ./bin/spark-submit --version
Welcome to Spark version 1.6.0

[aws_spark]$
{% endhighlight %}

When you're all done, kill the cluster:
<br><br>
{% highlight tcsh %}
[local]$ spark-ec2 destroy MySparkCluster

Searching for existing cluster MySparkCluster in region us-east-1...
Found 1 master, 2 slaves.
The following instances will be terminated:
> ec2-52-91-9-214.compute-1.amazonaws.com
> ec2-54-84-225-116.compute-1.amazonaws.com
> ec2-54-165-24-74.compute-1.amazonaws.com
ALL DATA ON ALL NODES WILL BE LOST!!
Are you sure you want to destroy the cluster MySparkCluster? (y/N) y
Terminating master...
Terminating slaves...

{% endhighlight %}
</div>
