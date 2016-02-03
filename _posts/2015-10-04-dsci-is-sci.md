---
layout: post
title: All Science is Data Science
tagline: "Large-scale analysis is not new"
author: Ken Cavagnolo
category : editorial
tags: [astrophysics, xgrid, perl, idl]
comments: true
tweets: false
---

{% include JB/setup %}

<div class="blurb">

<p>At the <a href="http://conf.dato.com/" target="_blank">2015 Dato
DSci Summit</a> in SF, the co-founder of <a
href="http://vibrantdata.is" target="_blank">Mappr</a>, <a
href="https://www.linkedin.com/in/eric-berlow-9865194"
target="_blank">Eric Berlow</a>, started his lightning talk with a
great observation I'm regurgitating below:
<ul>
<li>Around 2011, the sexy term was "Big Data."</li>
<li>Then it mutated to "Big Data Science."</li>
<li>The term was re-marketed to it's current state of just "Data Science."</li>
<li>Hopefully, we return to just "Science."</li>
</ul>
</p>

<p>While my site is lathered in "data science" and dsci terminology,
that's just to maintain the parlance everyone has adopted. I don't
particularly like the term, I think it's disingenuous, and every time
I use it a subtle cringe creeps over me. An analysis that relies on
data and the scientific method is science, it's not data science, it's
science. I can't think of a science that doesn't use data, is there
science without data? So bear with the narrative below, there's a
point.</p>

<p>When I started my grad research in 2002, like all good projects, we
started small (rule #1: no spaceships). We collected a few obs from
the <a href="http://cxc.harvard.edu/cda/" target="_blank">Chandra Data
Archive</a> for some interesting objects and plugged away. Each
dataset had about 10 files each that varied in size from few Mb's to
few 100's Mb's. I dabbled with some mosaic interferometric radio data
that ventured into the 10's Gb's range (big data in 2002).</p>

<p>As the work progressed, the sample size, and the datasets, grew as
did the complexity of the data being managed. Between 2002-2006, the
sample study grew into an archival study, and by 2007 the attitude had
become, "Analyze them all!" I had so much data, there were external
drives all over my workspace because the cluster was full and so were
all the remote machines. Worse, I was micromanaging cores on local
machines scattered about to do the analysis. This progressed into
managing multiple machines in a pseudo-cluster I setup with some
software I named "Shuttler" since the idea was to shuttle data and
chunks of analysis to available machines.</p>

<p>In 2004, I remember when <a
href="https://en.wikipedia.org/wiki/Xgrid" target="_blank">Xgrid</a>
made its appearance because it shipped on the new iMac's our research
group bought. At the time, we paid it no mind. But by 2005, I had
dabbled with it. By 2006, I was using it heavily since our real
cluster were Apple blades and Xgrid was a beast at crushing some
processes. Turns out, in 2007, all the MSU computer labs ugraded to
iMac's, and they all had Xgrid client software on-board. A little
shmoozing with campus IT, and they opened the clients to me at night
when the machines sat silent. So at the peak of our research program
(2007-2008) we had so many machines grinding on data, it was more
bookkeeping I did than coding. The crazy part? The analysis pipeline,
named <a href="http://www.pa.msu.edu/astro/MC2/accept/"
target="_blank">CORP</a>, was 90% Perl and 10% IDL! That it worked at
all is a miracle. CORP eventually was running 24/7 shipping data and
processes back and forth between my machine (Apocalypse aka
"headnode") to literally any machine on campus running Xgrid that had
an idle core.</p>

<p>The end result: I reduced from raw data products every observation
in the CXC archive and extracted finished data products for all
galaxies or galaxy clusters. At that time, it was a monumental effort
for one person. But why do that since that wasn't part of my science
objective? See, it was though -- it was available resources that
helped crush a time consuming problem. I was able to re-focus time on
inspecting the finished results and doing science to write
papers. Today, that might be called data science, but it's really just
science.</p>

<p>I once calculated my actual and automated workloads (a bad idea for
a grad student because you discover how little you make per labor
hour), and though I crammed 10 years of man hours into six years, the
huge win was wringing four years of manual computing time out of one
year of coding. Quadrupaling output isn't impressive for an automated
process, until you consider the cost of abandoning a problem because
the scope or scale is too large for manual intervention. If you told
me I was going to spend four years as a <a
href="https://en.wikipedia.org/wiki/Mechanical_Turk"
target="_blank">turk</a> reducing data, I'd have said "fuck no" and
done something else. To me, science creates the necessity to work
smarter, not harder, which is the ethos of "data science." Another
reason I don't understand the disambiguation and desire to make data
science this thing which is so much sexier and valuable than standard
science.</p>

<p>When it was all done, we had some awesome papers, I had a PhD, and
my admittance to the dyed-in-the-wool scientist guild was
completed. I'm priviledged to have my name attached to <a
href="http://www.pa.msu.edu/~donahue" target="_blank">Megan
Donahue's</a> and <a
href="https://www.pa.msu.edu/people/voit/Mark.html"
target="_blank">Mark Voit's</a> work. It was a privilege to work with
them. In hindsight, I'd change nothing about my "data science"
education, but man, I really wish we'd had AWS, Hadoop, and Spark back
then!</p>

</div>
