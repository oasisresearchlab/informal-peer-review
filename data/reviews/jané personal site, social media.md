---
created: 2024-09-05T18:23:45 (UTC -04:00)
tags: []
source: https://matthewbjane.com/blog-posts/blog-post-6.html#discussion
author: Matthew B. Jané
---

# A Statistical Interrogation of “The Case for Causality, Part 1” by Rausch and Haidt – Matthew B. Jané

> ## Excerpt
> I don’t know anything about the literature on social media and mental health so my focus on this post is to interrogate the statistical approach taken by the article written by Zach Rausch and Jonathon Haidt (link here) and to some extent the original meta-analysis by Ferguson.

---
[![](A%20Statistical%20Interrogation%20of%20%E2%80%9CThe%20Case%20for%20Causality,%20Part%201%E2%80%9D%20by%20Rausch%20and%20Haidt%20%E2%80%93%20Matthew%20B.%20Jan%C3%A9/.svg)](https://www.buymeacoffee.com/matthewbjane)

## Introduction[](https://matthewbjane.com/blog-posts/blog-post-6.html#introduction)

The article by Rausch and Haidt (R&H) conducts a re-analysis of a meta-analysis by Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)) on RCTs assessing the causal effect (for the sake of this post, I am avoiding any causal inference issues) of social media usage on outcomes related to well-being (e.g., life satisfaction, anxiety). However, the re-analysis conducted by R&H has severe flaws. Generally speaking, if you conduct a re-analysis of any study you should be certain that the re-analysis is of higher methodological quality than the original study. That is not the case here. This blog will get a bit technical, but it is important because meta-analysis isn’t just crunching numbers across studies. There is a formal statistical model that we should adhere to to actually produce coherent and interpretable results.

The original meta-analysis by Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)) is not without a number of flaws, but I think it accomplished what it set out to do. Notably, the meta-analysis was pre-registered, transparent, and had publicly available data. The only problem with the open data is that the statistics used to calculate the effect sizes (reported t-statistics, means, SDs, etc.) are completely missing from the database which makes reproducing it a lot harder.
	#inpeer/how/practices/review/paper/layers/empirical/openness/practices, #inpeer/how/practices/review/paper/layers/empirical/openness/data/needed

Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024))’s meta-analysis has a couple things that stood out to me as I was skimmed through it. It seems that all measures related to mental health and well-being are combined even if they are conceptually quite different (e.g., self-esteem and anxiety). When a study reported multiple different outcome measures, Ferguson decided to pool them together presumably to handle the dependency in effects. This is not an ideal strategy for two reasons, it assumes there is no heterogeneity between outcomes and it also loses specificity in the outcome. It would have been nice to see narrower bins of constructs meta-analyzed separately such as clinical anxiety/depression measures or life satisfaction/subjective well-being measures.
	#inpeer/how/practices/review/paper/layers/ontic/construct/lumped

Also, the results convey a common misinterpretation of the estimate in a random effects meta-analysis. The meta-analytic estimate was communicated as follows:

> As can be seen the overall estimate for d across studies was 0.088, which was nonsignificant and well below the SESOI (r = .10, d = 0.21).

What does an “overall estimate for _d_” actually mean (note: _d_ is the effect size, we will talk about this in the next section)? Is there a true _d_ that we are estimating by averaging the _d_ values from all these studies together? No. A random-effects meta-analysis is estimating the **mean of true effect sizes**. That is, there exists a distribution of true effects and the meta-analytic estimate conveys the central tendency. Therefore, the meta-analytic estimate can _not_ tell you whether the the intervention produces an effect of _d_ = .088 (lets ignore the variability in this estimate for the moment), it only tells you that the effect is _d_ = .088, **_on average_**. Heterogeneity in effect sizes describes how wide the distribution of true effects is. You _could_ have genuine true effects that are very positive (i.e., social media use is detrimental) and very negative (i.e., social media use is beneficial) even if the meta-analytic estimate is zero. There also could be study-level characteristics that could account for this heterogeneity, for instance, studies using a particular type of experimental design or a certain outcome shows a positive effect while others don’t.
	#inpeer/how/practices/review/paper/frames/pedagogical

**A side note**: I also came across this sentence from Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024))’s meta-analysis on page 3:

> Given the high power of meta-analysis, almost all meta-analyses are “statistically significant.”

I have heard this before but it is just not true, in general. In a random effects meta-analysis where you have both within and between study variance can give pretty wide confidence intervals and large p-values. This would be a reasonable statement if you are referring to a fixed effect meta-analysis with a large total sample size or a random effect meta-analysis with a ton of studies. Neither of which are true in this case.
	#inpeer/how/practices/review/paper/layers/empirical/analyses/misconceptionCIsPvals

## Let’s get into it[](https://matthewbjane.com/blog-posts/blog-post-6.html#lets-get-into-it)

The first part of this blog sets up a statistical meta-analysis model called a random-effects model. It is important to keep in mind that a meta-analysis is not throwing a bunch of standardized effects into a calculator and computing a mean. We need a coherent statistical model that allows us to draw meaningful inferences from the data.
	#inpeer/how/practices/review/paper/layers/empirical/analyses/misconceptionCIsPvals 

## Effect Size of Interest[](https://matthewbjane.com/blog-posts/blog-post-6.html#effect-size-of-interest)

First thing we should do is to define the effect size we are using to quantify the effect of social media on well-being related outcomes. The article by Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)) says they used a standardized mean difference known as a Cohen’s _d_ to quantify the difference between the post-test scores in the social media using group and the non-social media using group (or some variation of that). You may think “we should be controlling for baseline differences between treatment and control groups”, well in an RCT subject’s are randomly allocated to each group so their baseline scores should be, on average, the same. We can define a (true) effect size as,

where and is the mean of post-test scores for the social media using group and the non-social media using group (i.e., control group), respectively. The standardizer is the within-group standard deviation and it assumes that both the social media and non-social media group have the same standard deviation (probably a fine assumption 🤷). A sample estimator of the effect size will be denoted as and it represents the effect size we actually observe from the results of a study,

where English letters denote the sample estimators of the corresponding parameters in [Equation 1](https://matthewbjane.com/blog-posts/blog-post-6.html#eq-effect). The standardizer here is the pooled standard deviation. Since we only have access to the standard deviation of each group we have to pool them together to get a more precise estimate of (again, we are assuming the standard deviations within both groups are equal in the population),

I will note here, that there was no correction for small sample bias in the original meta-analysis as far as I could tell so I will not apply any correction here.

## Statistical Model[](https://matthewbjane.com/blog-posts/blog-post-6.html#statistical-model)

Ultimately, the observed effect size is a sample estimate of the true effect size and therefore will contain error. This error is referred to as **sampling error** and is defined as the difference between the observed effect size and the true effect size. For a given study , we can relate the observed effect size and the true effect size by including a sampling error term (),

where is literally defined as . The extent to which sampling errors are obscuring our effect size can be captured by the **sampling variance**. We can assume that sampling errors are normally distributed and evenly distributed around zero such that, where is the sampling variance for study . The sampling variance for a given study is dependent on the sample size with larger samples having more precision and thus less variance. Assuming normally distributed data, the sampling variance of the standardized mean difference ([Equation 2](https://matthewbjane.com/blog-posts/blog-post-6.html#eq-sample-effect)) is calculated with the following formula,

where . However unfortunately, the available dataset from Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)) did not provide the sample sizes within each group so instead we will have to assume they are equal () and use the simplified formula,

Now we might expect that any variation in effect sizes across studies is attributable to variance in random sampling errors, however this is unlikely to be the case. In reality, effect sizes tend to vary across studies above and beyond what we would expect from sampling error alone. This extra variation (known as heterogeneity) in effect sizes could be due to sampling from different populations, utilizing different methodologies, using different measures, etc.

Recall that we modeled an observed effect size as the sum of the true effect size for that study and sampling error . We defined the distribution of sampling errors so now we can also define the distribution of true effect sizes as where is the mean of true effect sizes across studies and is the variance of true effect sizes (i.e., heterogeneity). Ultimately our goal in a meta-analysis is to estimate both and . The common misinterpretation in (random-effect) meta-analyses that I described in the introduction is that a meta-analysis is estimating a single true effect size. If there is heterogeneity () then there is a distribution of true effects that we must consider.

## Parameter estimation[](https://matthewbjane.com/blog-posts/blog-post-6.html#parameter-estimation)

In meta-analysis we are trying to estimate particular parameters (i.e., the mean and variance of true effect sizes) just like any other statistical model. Simply averaging study effect sizes to obtain some “overall” effect size is not a principled statistical approach. This is why we went through the trouble of describing a random effects model in the previous section. We want to estimate the _mean_ of true effect sizes (**not** the “overall effect size” or “the true effect size”). To estimate the mean of true effects we can not just calculate the arithmetic mean of observed effect sizes. Instead we must use appropriate weights that take advantage of differential precision across studies. Particularly, we want to weight each study by the inverse variance,

This will preferentially weight studies with less sampling variance (i.e., larger sample sizes). Also, since is the same for all studies, the larger is relative to then the weights will become more equal across studies. We can then use these weights to estimate the mean true effect size by taking a weighted average of observed effect sizes across studies,

where the little carrot denotes an estimate. We can also compute the 95% confidence interval of (the set of plausible values of the actual mean that are compatible with the data) using the Hartung, Knapp, Sidik and Jonkman method (this adjusts for poor coverage rates in small meta-analyses, which is the case here),

The last two things we want to estimate are the variance in true effects and what is known as a prediction interval. The variance in true effects is estimated a variety of different ways and we won’t go through all of them here. Instead we will exclusively use a restricted maximum likelihood estimator (REML) which is an iterative estimation procedure. Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)) uses a maximum likelihood estimator (ML), however ML tends to under-estimate the heterogeneity. The 95% prediction interval uses the information from to construct an interval that can be interpreted as the interval where 95% of true effect sizes fall.

So just keep in mind that the describes the variability in the estimate of the mean and describes the variability in the true effects.

## Summarizing and reproducing Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024))[](https://matthewbjane.com/blog-posts/blog-post-6.html#summarizing-and-reproducing-ferguson2024)

Okay now that we have set up our model, we can now actually look at the data from the meta-analysis. Let’s load in some R packages and the dataset from the OSF repository referenced in Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)).

```
# load in packages
library(osfr)
library(tidyverse)
library(metafor)
library(readxl)
library(psychmeta)

# download data from OSF repo
invisible(
  osf_retrieve_file("jcha2") %>%
    osf_download(conflicts = "overwrite")
)

# load in dataset and filter out studies without data
dat <- read_excel("Best Practices Coding Experiments.xlsx",
                  sheet = 1) %>%
  filter(!is.na(d))

# display effect size data for first 6 studies
head(dat[c("Citation","n","d")])
```

```
# A tibble: 6 × 3
  Citation                    n      d
  &lt;chr&gt;                   &lt;dbl&gt;  &lt;dbl&gt;
1 Alcott 2020              1661  0.09 
2 Brailovskaia 2020         286  0.154
3 Brailovskaia 2022         322  0    
4 Collins and Edgers 2022   121 -0.138
5 Deters &amp; Mehl 2013         86 -0.207
6 Faulhaber et al., 2023    230  0.484
```

The data only gives us the effect size `d` and the sample size `n` for each study so we need to calculate the sampling variance. Using the `psychmeta` package we can calculate the sampling variance for each study as follows,

```
# A tibble: 6 × 3
  Citation                    n      d
  <chr>                   <dbl>  <dbl>
1 Alcott 2020              1661  0.09 
2 Brailovskaia 2020         286  0.154
3 Brailovskaia 2022         322  0    
4 Collins and Edgers 2022   121 -0.138
5 Deters & Mehl 2013         86 -0.207
6 Faulhaber et al., 2023    230  0.484
```

```
# compute sampling variance
dat <- dat %>% 
  mutate(v = var_error_d(d = d, n1 = n))

# display updated dataset
head(dat[c("Citation","n","d","v")])
```

Now we are set up to fit a random effects model. Using the `metafor` package we can use the REML method for estimating the heterogeneity and the Hartung-Knapp-Sidik-Jonkman method for obtaining the confidence intervals and p-values.

```
# A tibble: 6 × 4
  Citation                    n      d       v
  <chr>                   <dbl>  <dbl>   <dbl>
1 Alcott 2020              1661  0.09  0.00241
2 Brailovskaia 2020         286  0.154 0.0141 
3 Brailovskaia 2022         322  0     0.0125 
4 Collins and Edgers 2022   121 -0.138 0.0337 
5 Deters & Mehl 2013         86 -0.207 0.0479 
6 Faulhaber et al., 2023    230  0.484 0.0181 

```

```
mdl <- rma(yi = d, 
           vi = v, 
           data = dat,
           method = "REML",
           test="knha")
mdl

```

```Random-Effects Model (k = 27; tau^2 estimator: REML)

tau^2 (estimated amount of total heterogeneity): 0.0564 (SE = 0.0230)
tau (square root of estimated tau^2 value):      0.2374
I^2 (total heterogeneity / total variability):   76.62%
H^2 (total variability / sampling variability):  4.28

Test for Heterogeneity:
Q(df = 26) = 91.9083, p-val &lt; .0001

Model Results:

estimate      se    tval  df    pval    ci.lb   ci.ub    
  0.0879  0.0576  1.5249  26  0.1394  -0.0306  0.2063    

---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

We are pretty much able to reproduce the results seen in Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)) with slight differences probably due to having to assume equal sample sizes between groups, using a different heterogeneity estimator and using the Hartung-Knapp-Sidik-Jonkman method for the confidence intervals. Let’s get the 95% prediction interval as well.

``` predict.rma(mdl) ```

```

   pred     se   ci.lb  ci.ub   pi.lb  pi.ub 
 0.0879 0.0576 -0.0306 0.2063 -0.4143 0.5901 
```

So, 95% of true effects fall between -.41 and .59 according to our model.

## R&H’s analysis[](https://matthewbjane.com/blog-posts/blog-post-6.html#rhs-analysis)

R&H conduct a sub-group analysis by chopping up the studies into three bins. First issue here is that this analysis is completely post-hoc and who knows if they created these bins after trying various combinations to reach the conclusion that they desired. R&H separate the 27 studies into three bins (this is verbatim from the article):
	#inpeer/how/practices/review/paper/layers/empirical/rigor/analysis/subGroupAnalysisArbitrary

1.  **Multi-week reduction experiments.** These ten studies examined the impact of reducing social media use for at least two weeks, allowing withdrawal symptoms to dissipate.
    
2.  **Short (one week or less) reduction experiments.** These ten studies examined brief periods of abstinence from social media use, which are likely to pick up withdrawal symptoms from heavy users.
    
3.  **Exposure experiments.** In these seven studies, the ‘treatment’ is typically brief exposure to some kind of social media, such as requiring high school students to look at their Facebook or Instagram page for 10 minutes.
    

The second problem we see is that the first two groups are separated by dichotomizing a naturally continuous variable (length of intervention). Sure it makes the data more digestible, but you simply lose information. This is generally considered bad statistical practice and we will see why a little later.
	#inpeer/how/practices/review/paper/layers/empirical/analyses/decisions/dichotomizedVar

To reproduce R&H’s analysis, we will add a column to the data set that denotes the group membership (1 = Multi-week reduction experiments, 2 = One week reduction experiments, 3 = Less than one week reduction experiments, 4 = Exposure experiments) of each study.

```
dat <- dat %>%
  mutate(subgroup = c(1, # Alcott 2020
                      1, # Brailovskaia 2020
                      1, # Brailovskaia 2022
                      1, # Collins and Edgers 2022
                      4, # Deters & Mehl 2013
                      1, # Faulhaber et al., 2023
                      3, # Gajdics 2022
                      1, # Hall et al. 2021
                      1, # Hunt 2018
                      1, # Hunt 2021
                      2, # Kleefeld dissertation
                      2, # Lambert 2022
                      4, # Lepp 2022
                      2, # Mahalingham 2023
                      3, # Mitev 2021
                      4, # Ozimek 2020
                      3, # Przybylski 2021
                      4, # Sagioglou 2014 study 2"
                      4, # Tartaglia
                      1, # Thai 2021
                      1, # Thai 2023
                      2, # Tromholt 2016
                      2, # Valley2019
                      2, # van wezel 2021
                      3, # Vanman 2018
                      4, # Ward 2017
                      4  # Yuen et al., 2019
                      ))


# display updated dataset
head(dat[c("Citation","n","d","v","subgroup")])
```

```
# A tibble: 6 × 5
  Citation                    n      d       v subgroup
  &lt;chr&gt;                   &lt;dbl&gt;  &lt;dbl&gt;   &lt;dbl&gt;    &lt;dbl&gt;
1 Alcott 2020              1661  0.09  0.00241        1
2 Brailovskaia 2020         286  0.154 0.0141         1
3 Brailovskaia 2022         322  0     0.0125         1
4 Collins and Edgers 2022   121 -0.138 0.0337         1
5 Deters &amp; Mehl 2013         86 -0.207 0.0479         4
6 Faulhaber et al., 2023    230  0.484 0.0181         1
```

Now that we have the subgroup column, we can conduct the sub-group analysis. Here comes the next problem, R&H decide to simply calculates the arithmetic (unweighted) mean of the observed effect sizes within each group. The problem is that they aren’t capitalizing on the fact that different studies have different levels of precision. The only way it would make sense to compute an unweighted average with respect to the statistical model we are employing is if sampling error didn’t exist (it does) or heterogeneity is infinite (its not), so either way its just the wrong approach.

Let’s first reproduce R&H’s results by taking the unweighted average of observed effect sizes.

```
results <- summarize(.data = dat,
                     mean_d = mean(d),
                     k_studies = n(),
                     .by = subgroup)

# reorder the subgroup display
results[c(1,4,3,2),]
```

```
# A tibble: 4 × 3
  subgroup  mean_d k_studies
     <dbl>   <dbl>     <int>
1        1  0.204         10
2        2  0.0868         6
3        3 -0.172          4
4        4  0.0566         7
```

All the values are accurate. We can compare it to the table shown in R&H’s article:

![](A%20Statistical%20Interrogation%20of%20%E2%80%9CThe%20Case%20for%20Causality,%20Part%201%E2%80%9D%20by%20Rausch%20and%20Haidt%20%E2%80%93%20Matthew%20B.%20Jan%C3%A9/table1-2-3_R&H.png)
![[Pasted image 20240905193510.png]]
Okay we see a positive average effect for the multi-week reduction experiments, but lets now use proper inverse-variance weights to calculate the average. This time we will model the groups as dummy predictors and specify the proper contrasts for each group:

```
# construct a meta-analytic model with subgroup
# as a dummy-coded categorical predictor
mdl <- rma(d ~ factor(subgroup,levels = c(1,2,3,4)), 
           vi = v, 
           data = dat,
           test="knha")

# acquire subgroup-level mean estimates
estimates <- as.data.frame(
  predict(mdl, 
          rbind(g1 = c(0,0,0),
                g2 = c(1,0,0),
                g3 = c(0,1,0),
                g4 = c(0,0,1))))

# print results
round(data.frame(group = 1:4, mean_delta = estimates$pred),3)
```

```
  group mean_delta
1     1      0.177
2     2      0.154
3     3     -0.172
4     4      0.082
```

As we can see the estimates are a bit different. Another thing that is completely missing from the R&H analysis is any indication of variability in their mean estimates and their is no indication of heterogeneity. It is conveyed as a fixed quantity, however just because we combine many studies together does not mean that uncertainty ceases to exist.
	#inpeer/how/practices/review/paper/layers/empirical/transparency/variationUnreported

```
round(data.frame(group = 1:4, 
                 mean_delta = estimates$pred,
                 CI_low = estimates$ci.lb,
                 CI_high = estimates$ci.ub,
                 PI_low = estimates$pi.lb,
                 PI_high = estimates$pi.ub),3)
```

```
  group mean_delta CI_low CI_high PI_low PI_high
1     1      0.177 -0.005   0.360 -0.296   0.651
2     2      0.154 -0.098   0.407 -0.350   0.659
3     3     -0.172 -0.443   0.099 -0.686   0.342
4     4      0.082 -0.151   0.315 -0.414   0.577
```

True effects for group 1 (multi-week reduction studies, i.e., the focal group) are quite variable and can range from -0.296 to 0.651. An interesting point to bring up is that Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)) set the smallest effect size of interest (SESOI) to be _d_ = .21 in his pre-registration (equivalent to a Pearson correlation of _r_ = .10). However, that does not help us much here since the upper bound of the confidence interval is well above _d_ = .21 so you can’t really make the claim that that there is no clinically meaningful effect, _on average_. And you definitely can’t make the claim that all/most true effects are not clinically meaningful since the upper bound of the PI is 0.651. Truthfully, the SESOI established in Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024)) does not seem to have any good theoretical or practical justification outside of “seems reasonable” so it is unclear what the utility of this arbitrary boundary is in this case?
	#inpeer/how/practices/review/paper/layers/empirical/analyses/decisions/SESOIUnjustified

## Properly modeling the length of intervention in reduction studies[](https://matthewbjane.com/blog-posts/blog-post-6.html#properly-modeling-the-length-of-intervention-in-reduction-studies)

Instead of binning the length of the intervention into groups I will use the weeks reported in the R&H article to create a continuous moderator for reduction studies only.

```
dat <- dat %>%
  mutate(length_weeks = c(4, # Alcott 2020
                          2, # Brailovskaia 2020
                          2, # Brailovskaia 2022
                          10, # Collins and Edgers 2022
                          NA, # Deters & Mehl 2013
                          2, # Faulhaber et al., 2023
                          1/7, # Gajdics 2022
                          2.5, # Hall et al. 2021
                          1, # Hunt 2018
                          1, # Hunt 2021
                          1, # Kleefeld dissertation
                          1, # Lambert 2022
                          NA, # Lepp 2022
                          1, # Mahalingham 2023
                          1/7, # Mitev 2021
                          NA, # Ozimek 2020
                          1/7, # Przybylski 2021
                          NA, # Sagioglou 2014 study 2"
                          NA, # Tartaglia
                          3, # Thai 2021
                          3, # Thai 2023
                          1, # Tromholt 2016
                          1, # Valley2019
                          1, # van wezel 2021
                          5/7, # Vanman 2018
                          NA, # Ward 2017
                          NA  # Yuen et al., 2019
  ))


# display updated dataset
head(dat[c("Citation","n","d","v","length_weeks")])
```

```
# A tibble: 6 × 5
  Citation                    n      d       v length_weeks
  &lt;chr&gt;                   &lt;dbl&gt;  &lt;dbl&gt;   &lt;dbl&gt;        &lt;dbl&gt;
1 Alcott 2020              1661  0.09  0.00241            4
2 Brailovskaia 2020         286  0.154 0.0141             2
3 Brailovskaia 2022         322  0     0.0125             2
4 Collins and Edgers 2022   121 -0.138 0.0337            10
5 Deters &amp; Mehl 2013         86 -0.207 0.0479            NA
6 Faulhaber et al., 2023    230  0.484 0.0181             2
```

Okay so now we have the moderator we can construct a linear meta-regression model of the form, 
![[Screenshot 2024-09-05 at 19.38.18.png]]
Notice now that true effects how is distributed around the regression line such that the distribution of true effects is now
![[Screenshot 2024-09-05 at 19.38.38.png]]

```
mdl_weeks <- rma(d ~ length_weeks,
                 vi = v,
                 data = dat,
                 method = "REML",
                 test = "knha")</span>
```

```
Warning: 7 studies with NAs omitted from model fitting.
```

```
mdl_weeks

```

Mixed-Effects Model (k = 20; tau^2 estimator: REML)

tau^2 (estimated amount of residual heterogeneity):     0.0647 (SE = 0.0299)
tau (square root of estimated tau^2 value):             $2544
I^2 (residual heterogeneity / unaccounted variability): 79.40%
H^2 (unaccounted variability / sampling variability):   4.85
R^2 (amount of heterogeneity accounted for):            0.00%

Test for Residual Heterogeneity:
QE(df = 18) = ()
Model Results:

              estimate      se    tval  df    pval    ci.lb   ci.ub    
intrcpt         0.0884  0.0922  0.9581  18  0.3507  -0.1054  0.2821    
length_weeks    0.0014  0.0330  0.0423  18  0.9667  -0.0678  0.0706    

---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

```

Okay so as it turns out there appears to be little/no effect of the length of the intervention on the effect size. Let us plot out the data to see what the relationship actually looks like:

![](A%20Statistical%20Interrogation%20of%20%E2%80%9CThe%20Case%20for%20Causality,%20Part%201%E2%80%9D%20by%20Rausch%20and%20Haidt%20%E2%80%93%20Matthew%20B.%20Jan%C3%A9/unnamed-chunk-11-1.png)

The regression line looks almost parallel to the _d_ = 0 line (the grey line). You may notice the outlier at 10 weeks and you may want to remove it from the analysis. I would ask why? The data point does not appear to be a coding error or a mistake? It is a valid data point and piece of evidence that should not be taken out of the analysis post-hoc. Hell, it could be that the the positive effect of not being on social media only lasts a few weeks and then fades out (not an uncommon trend in psychology interventions). Anyways, any reason to remove that “outlier” would seem to me like a post-hoc rationalization.

## Discussion[](https://matthewbjane.com/blog-posts/blog-post-6.html#discussion)

The re-analysis of Ferguson ([2024](https://matthewbjane.com/blog-posts/blog-post-6.html#ref-ferguson2024))’s meta-analysis by R&H does not have adequate statistical rigor to build a “case for causality”. Post-hoc subgroup analyses conducted by R&H did not use a principled statistical model, they did not report any variability in their estimates, the estimates themselves were sub-optimal (unweighted averaging), and they misinterpreted the point-estimates that they calculated. They did not do a proper comparison of their point-estimates and instead they treated them as fixed quantities and simply claimed that these average effect sizes are different without consideration of variability in their estimation procedure. Their conclusion claimed that:

> we still found that his data _supports_ (rather than undermines) the contention by some scholars that “reductions in social media time would improve adolescent mental health,” at least as long as the reductions continue for two weeks or longer.

Based on my re-analysis of R&H’s re-analysis I find that the intervention length when modeled properly as a continuous variable (since it literally is) does not support this claim.

If I did anything incorrectly or if I did not use best practices, I take full responsibility and you can let me know by sending me a DM on twitter or emailing me at matthewbjane@gmail.com.
	#cscw/how/social/OpenToImprovement

## References[](https://matthewbjane.com/blog-posts/blog-post-6.html#references)

Ferguson, Christopher J. 2024. “Do Social Media Experiments Prove a Link with Mental Health: A Methodological and Meta-Analytic Review.” _Psychology of Popular Media_, No Pagination Specified–. [https://doi.org/10.1037/ppm0000541](https://doi.org/10.1037/ppm0000541).
