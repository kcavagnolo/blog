---
layout: post
title: Simple Spark Use Case
tagline: "Counting Words: the 'Hello, world!' of Big Data"
author: Ken Cavagnolo
category : lessons
tags: [spark, python, aws, osx]
comments: true
tweets: true
---

{% include JB/setup %}

<div class="blurb">

Install Java

- Download Oracle Java SE Development Kit 7 or 8 at Oracle JDK downloads page.
- Double click on .dmg file to start the installation
- Open up the terminal.
- Type java -version, should display the following 

java version "1.7.0_71" 
Java(TM) SE Runtime Environment (build 1.7.0_71-b14) 
Java HotSpot(TM) 64-Bit Server VM (build 24.71-b01, mixed mode)  



Set JAVA_HOME 

export JAVA_HOME=$(/usr/libexec/java_home) 


 
Install Homebrew 
  
           ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 



Install Scala 

brew install scala 



Set SCALA_HOME 

export SCALA_HOME=/usr/local/bin/scala  
export PATH=$PATH:$SCALA_HOME/bin 

  
Download Spark from https://spark.apache.org/downloads.html  

tar -xvzf spark-1.1.1.tar 
cd spark-1.1.1  


Build and Install Apache Spark 

sbt/sbt clean assembly 



Fire up the Spark 

For the Scala shell: 
./bin/spark-shell 

For the Python shell: 
./bin/pyspark 



Run Examples 

Calculate Pi: 

./bin/run-example org.apache.spark.examples.SparkPi 

MLlib Correlations example: 

./bin/run-example org.apache.spark.examples.mllib.Correlations 

MLlib Linear Regression example: 

./bin/spark-submit 
--class org.apache.spark.examples.mllib.LinearRegression 
examples/target/scala-*/spark-*.jar data/mllib/sample_linear_regression_data.txt  

------
------

brew install scala
brew install sbt

Since this is more about gcc not installing as a result of not finding
the java jdk, you'll want to find the current version of java used as
default:

ls -l `which java`
/usr/libexec/java_home -v 1.8 # To locate a specific version
/usr/libexec/java_home -V # To locate all versions

You'll need to update your PATH to reflect the location of the jdk
(normally for 1.8.0 it should be):

Add these to the path in .cshrc
setenv JAVA_HOME `/usr/libexec/java_home -v 1.8.0`
set PATH=($PATH $JAVA_HOME/bin)

sudo sbt clean assembly

</div>
