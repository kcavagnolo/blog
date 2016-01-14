---
layout: post
title: Build Spark Cluster Locally on OSX
tagline: "How I installed Spark on some spare Macs"
author: Ken Cavagnolo
category : lessons
tags: [spark, python, osx]
comments: true
---

{% include JB/setup %}

<div class="blurb">

<p>For a client project, I came into possession of a couple old
Macbooks. The client's on-prem Spark cluster was in-development and
accessing the AWS cluster was extremely slow because of the security
setup. So I took the old Macs and set them up from the ground to be
part of a mini-cluster. Below are the steps needed to install Spark
locally on each machine. Like my other posts, this is trivial and
simple, but there wasn't a tutorial online, so maybe this will be
useful for someone else in the future.</p>

<p>Install Homebrew and update:
<br>
{% highlight tcsh %}
[local]$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
[local]$ brew doctor
{% endhighlight %}
</p>

<p><a
href="http://www.oracle.com/technetwork/java/javase/downloads/index.html"
target="_blank">Download and install Oracle Java SE Development Kit
(SDK).</a> I don't use Homebrew here since the versions can get all
over the place which will infuriate Spark. Standard install process:
double click on dmg file to start the installation and follow
prompts. Open up a terminal to check version and set env vars:
<br>
{% highlight tcsh %}
[local]$ ls -l `which java`

lrwxrwxrwx 1 root 22 Apr 10  2015 /usr/bin/java -> /usr/libexec/java_home

[local]$ java -version

java version "1.7.0_71"
Java(TM) SE Runtime Environment (build 1.7.0_71-b14)
Java HotSpot(TM) 64-Bit Server VM (build 24.71-b01, mixed mode)

[local]$ echo 'setenv JAVA_HOME /usr/libexec/java_home' >> ~/.cshrc
[local]$ source ~/.cshrc
{% endhighlight %}
</p>

<p>Install Scala and setup some env vars:
<br>
{% highlight tcsh %}
[local]$ brew install scala
[local]$ brew install sbt
[local]$ echo 'setenv SCALA_HOME /usr/local/bin/scala' >> ~/.cshrc
[local]$ echo 'set path=($path $SCALA_HOME/bin)' >> ~/.cshrc
[local]$ source ~/.cshrc
{% endhighlight %}
</p>

<p><a href="https://spark.apache.org/downloads.html"
target="_blank">Download Spark and save tarball somewhere</a> Install Spark and build:
<br>
{% highlight tcsh %}
[local]$ tar -xvzf spark-x.x.x.tar; cd spark-x.x.x
[local]$ build/sbt clean assembly
[local]$ echo 'setenv SPARK_HOME /usr/local/spark' >> ~/.cshrc
[local]$ echo 'setenv PYSPARK_DRIVER_PYTHON ipython' >> ~/.cshrc
[local]$ echo 'set path=($path $SPARK_HOME/bin)' >> ~/.cshrc
[local]$ source ~/.cshrc
{% endhighlight %}
</p>

<p>After doing this on all the machines and pointing the nodes to the
head (get the IP from the config file -- ensure all machines have an
address on your subnet and can speak to each other), start-up Spark
and play around: <br>

{% highlight tcsh %}
[local]$ spark-submit --class org.apache.spark.examples.mllib.LinearRegression examples/target/scala-*/spark-*.jar data/mllib/sample_linear_regression_data.txt
[local]$ pyspark

Welcome to Pyspark version 1.5.2
Using Python version 2.7.10 (default, Oct 14 2015 16:09:02)
SparkContext available as sc, HiveContext available as sqlContext.
{% endhighlight %}
{% highlight python %}
[pyspark]$ run-example org.apache.spark.examples.SparkPi
{% endhighlight %}
</p>
</div>
