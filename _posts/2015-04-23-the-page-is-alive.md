---
layout: post
title: The Blog is Alive!
tagline: "Small Successes Feel Amazing"
author: Ken Cavagnolo
category : lessons
tags: [javascript, jquery, html5, python, jekyll, git]
comments: true
tweets: false
---

{% include JB/setup %}

<div class="blurb">
     <p>This time I truly mean it: hello, world! I have owned the
     domain kcavagnolo.com for many years, and I never did anything
     with it. The plan had always been to expos&eacute; some aspect of
     my work, which at the time was astrophysics research. But, those
     efforts usually fell into job hunting season and polishing a site
     to accompany my resum&eacute;'s.</p>

     <p>Well, now that I have been out of academia for several years,
     and I have dabbled long enough in "data science" activities to
     have a decent portfolio of stuff to share -- this site finally
     made sense. After 24 hours of mucking around, it's finally
     working correctly and I can post to it as a remote platform via
     some cool automated tools I coded up. Without further ado, the
     details of how the site came to be, and the accompanying code so
     someone else can do the same thing.</p>

     <p>First things first: bite the bullet and buy a custom
     domain. The simplest route I've found in years is [Google
     Domains](http://domains.google.com). Prices are
     competitive and the interface is intuitive.</p>

     <p>The steps I need to describe:<br>
     <ul>
     <li>google domains</li>
     <li>setup github pages</li>
     <li>dns and email forwarding for custom domain</li>
     <li>starter site template</li>
     <li>hacking together the pieces I liked and needed</li>
     <li>building a local instance of github pages and projects w/ jekyll</li>
     <li>installing jekyll-bootstrap to handle subdir instance of blog</li>
     <li>validating all the code and testing</li>
     <li>kick the whole thing live</li>
     </ul>
     </p>

     <p>The shit that's still broken:<br>
     <ul>
     <li>fancybox</li>
     <li>ipython integration</li>
     <li>plotly integration</li>
     <li>zero branding (logo, tagline, presented material)</li>
     </ul>
     </p>

     <p>Small victory today.</p>

     {% highlight python linenos %}
     def build_model(X, X_test, y):
     model = DecisionTreeClassifier()
     samples = sc.parallelize(Bootstrap(y.size))
     vote_tally = samples.map(lambda (index, _):
     model.fit(X[index], y[index]).predict(X_test)
     ).map(vote_increment).fold(zero_matrix(n_test, n_ys), np.add)
     y_estimate_vote = np.argmax(vote_tally, axis = 1)
     return accuracy_score(y_estimate_vote)
     {% endhighlight %}

</div>
