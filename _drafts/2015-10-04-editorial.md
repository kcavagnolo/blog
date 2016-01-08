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

started w/ a few obs
about 10 files each
files varied in size from few Mb to few 100's Mb
mosaic radio files get even larger (10's Gb)
archival study grew into let's do a sample
to let's do a survey
to let's do them all!
started with managing cores on my machine
moved to managing multiple machines on "cluster"
moved to 'shuttler' which shipped products to any available resource
moved to xgrid on campus computing labs silent at night

crazy thing? CORP and Shuttler were written completely in Perl and
IDL. That it worked at all is a miracle.

shuttler eventually was running 24/7 shipping data and processes back
and forth between my machine (head node) to literally any machine on
campus running xgrid that had an idle core

the end result: reduced from raw data every observation in the CXC
archive and extracted finished data products for all galaxies or
galaxy clusters

why since that wasn't part of my science objective? because I
could. it was badass infrastructure that was crushing a time consuming
problem. I got to spend time inspecting the finished results and doing
science.

I once calculated my actual and automated workloads (a bad idea for a
grad student because you discover how little you make per labor hour),
and though I crammed 10 years of man hours into six years, the huge
win was wringing 4 years of manual computing time out of 1 years of
coding. Quadrupaling output isn't impressive for an automated process,
until you consider the cost of abandoning a problem because the scope
or scale is too large for manual intervention. If you told me I was
going to spend 4 years as a <a href="turk">turk</a> reducing data, I'd
have said "fuck no" and done something else.

the end result: some awesome papers. I'm priviledged to have my name
attached anywhere to Megan and Mark's work, let alone to have had a
subtle impact on their thinking that led to the (soon to be seminal?)
precipitation papers.

things I wish I knew then that I know now:
hadoop

</div>
