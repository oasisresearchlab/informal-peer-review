---
type: appraisal
noteID: b6a737c3-ae13-47e4-b493-c206efac491d
status: complete
url: 
appraiser: "[[Elisabeth Bik]]"
setting: 
source: https://scienceintegritydigest.com/2021/08/30/cassava-sciences-of-posters-and-spaghetti-plots/
permalink: https://archive.is/NpL7Q
---


- [Cassava Sciences: Of Posters and Spaghetti Plots](https://scienceintegritydigest.com/2021/08/30/cassava-sciences-of-posters-and-spaghetti-plots/)
	- 2021-08-30
		- > "here I will review a [conference poster](https://archive.is/NpL7Q) reporting on Phase 2 data obtained by Cassava Sciences."
			- #inpeer/evdInfra/what/studyReports/poster			- {{pdf: https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fmegacoglab%2FyxaT3sZgDt.pdf?alt=media&token=a33cad3e-fe3e-431a-97c9-4700a7cec14d}}
		- potential outlier manipulation: used [[Webplot Digitizer]]
				- #inpeer/evdInfra/what/reviewTools/forensic/stats/dataExtr 
					- This means that the sleuth(s) used a tool to extract data from a scholarly publication (often a table/figure). One example tool is Webplot Digitizer.
			- Data point (outlier) switches experimental conditions between Fig. 4 and Fig. 5
				- > "Looking at the estimated change-percentages, Figure 5’s estimated values appear to line up nicely with the position of the data points in Figure 4. Except, that is, for **the 150% data point, which seems to have jumped from the 100 mg treatment group to the Placebo group**. If this one outlier data point, specifically mentioned in the text of the poster, had been included in the 100 mg treatment group, the average change-from-baseline would change from -17% to around -3%, which is a much less spectacular reduction of plasma P-tau181 levels than claimed by the company."
					- #inpeer/how/practices/review/paper/layers/empirical/rigor/analysis/inconsistentData 
				- Uncertainty about error or data manipulation
					- > "Please note that I am not suggesting here that moving this data point from the treatment group to the placebo group was done on purpose. Mistakes can happen, in particular if there is a rush to publish, and I do not know exactly what has happened here."
						- #inpeer/how/practices/review/paper/frames/advisory 
						- #inpeer/how/practices/review/paper/frames/pedagogical/cautiousCaveats
							- This means that the informal peer reviewer is being cautious and added caveats to their conclusions. They are careful to avoid strong accusations.
				- JP: [[idea: Reporting guidelines for tables and figures would be nice to iterate.]]
			- Sample sizes per condition unreported and inconsistent with total sample size
				- > "The poster states that **64 patients** were included in the study, and randomly assigned to three groups. There are no details given about how many patients were assigned to each group, but we would expect roughly 20 people per group. Yet, Figure 4 only shows 20, 15, and 17 data points for the placebo, 50 mg, and 100 mg Simufilam groups, respectively. This is a total of **52 patients**. What happened to the 12 other patients? If fewer data points from the treatment groups are reported, does this mean that data points from the treatment groups have been left out? It would be nice if Cassava scientists could explain what happened with those 12 patients who appear to have dropped out of the study."
					- #inpeer/how/practices/review/paper/layers/empirical/rigor/analysis/inconsistentData 
				- > "While Figure 4 shows 20/15/17 (**sum=52**) data points for the three groups, Figure 5 appears to show 18/15/18 data points (**sum=51**). The numbers of the placebo and 100 mg treatment groups therefore do not match."
					- #inpeer/how/practices/review/paper/layers/empirical/rigor/analysis/inconsistentData
			- Color scheme changes between Fig. 4 -> Fig. 5
				- > "This is a minor issue, but the **color scheme** confusingly changes from Figure 4 to Figure 5. While the 50 mg Simufilam remains blue, the placebo group switches from red to green and the 100 mg Simufilam group switches from green to red."
					- #inpeer/how/practices/review/paper/values/communicability/clarity/inconsistentColors
						- This means that the color scheme changed between figures in a scholarly report. In some cases, this may be a trivial aesthetic concern, but in others could raise the possibility of fraud/errors.
			- Outlier from Fig. 5 missing in Fig. 4
				- > "The biggest concern is that some of the data points do not seem to match up between the two figures. Of particular note, in Figure 5, the P-tau181 value from a patient in the 100 mg treatment group went up from ~2.1 to ~5.2 pg/ml, which is an increase of 150%. In other words, one of the patients in the 100 mg treatment group showed a large increase of the Alzheimer’s disease biomarker. Yet, this particular data point is missing in the 100 mg treatment group in Figure 4. Instead, **the 150% increase data point is included in the placebo group**."
					- #inpeer/how/practices/review/paper/layers/empirical/analyses/errors/improbableValues 
	- Markdown
		- --
		- created: 2024-10-01T18:10:45 (UTC -04:00)
		- tags: []
		- source: [https://scienceintegritydigest.com/2021/08/30/cassava-sciences-of-posters-and-spaghetti-plots/](https://scienceintegritydigest.com/2021/08/30/cassava-sciences-of-posters-and-spaghetti-plots/)
		- author:
		- --
		- # Cassava Sciences: Of Posters and Spaghetti Plots – Science Integrity Digest
			
		- > ## Excerpt
		- > In a previous blog post, I took a look at Western blots in papers from the lab of Dr. Hoau-Yan Wang at City University of New York (CUNY), mostly related to Cassava Sciences (Nasdaq: $SAVA), i…
		- --
		- In a [previous blog post](https://scienceintegritydigest.com/2021/08/27/cassava-sciences-of-stocks-and-blots/#more-2692), I took a look at Western blots in papers from the lab of [Dr. Hoau-Yan Wang](https://www.ccny.cuny.edu/profiles/hoau-yan-wanghttps://www.ccny.cuny.edu/profiles/hoau-yan-wang) at [City University of New York](https://www.cuny.edu/) (CUNY), mostly related to [Cassava Sciences](https://www.cassavasciences.com/) (Nasdaq: [$SAVA](https://www.nasdaq.com/market-activity/stocks/sava)), its predecessor Pain Therapeutics INC, and its flagship Alzheimer’s Disease drug candidate [Simufilam](https://www.cassavasciences.com/simufilam).
		- While those papers were mainly about the preclinical Simufilam data, here I will review a conference poster reporting on Phase 2 data obtained by Cassava Sciences.
		- ### The AAIC conference poster
			
		- The poster was presented at the Alzheimer’s Association International Conference (AAIC) held in Denver, CO, on July 26, 2021. In several press releases around that time, Cassava announced that Simufilam treatment [reduced biomarkers](https://www.cassavasciences.com/news-releases/news-release-details/cassava-sciences-announces-positive-biomarker-data-simufilam) \[[poster presentation](https://www.cassavasciences.com/static-files/0854aec6-59b3-4e2b-ac20-c32b7c307b08)\] in Alzheimer’s patients while [improving their cognition](https://www.cassavasciences.com/news-releases/news-release-details/cassava-sciences-announces-positive-cognition-data-simufilam) in Phase 2 trials \[[oral presentation](https://www.cassavasciences.com/static-files/13794384-53b3-452c-ae6c-7a09828ad389) held at the same conference\].
		- The AAIC poster is of interest because it represents data from the Phase 2 clinical trial. Some folks commented on social media that one should not criticize old preclinical data if clinical data proves that the candidate drug works (see e.g. discussion [here](https://www.reddit.com/r/SAVA_stock/comments/pdb8zf/a_long_term_sava_bulls_thoughts_on_our_recent/hati0vn/?context=3)). So let’s take a look at the published _clinical_ data in this conference poster.
		- ### P-tau181 as an Alzheimer’s disease biomarker
			
		- The poster reports on **64 Alzheimer’s diseas**e (AD) patients, who were randomized into three treatments groups. One group received a placebo, the second group got 50 mg of oral simufilam, and the third group got 100 mg of oral simufilam, for 28 days.
		- Plasma levels of **P-tau181** were determined on day 1 (start of treatment) and day 28. High P-tau181 plasma levels are correlated with the development of AD dementia, and are considered [a diagnostic and prognostic biomarker](https://www.nature.com/articles/s41591-020-0755-1) of AD.
		- Figure 5 of the Cassava poster shows the day 1 and day 28 plasma P-tau181 levels of the patients in each of the three groups, with a line connecting the two values. Although this is a rather busy figure, one can see that P-tau181 levels went up for some patients (suggestive of worsening AD), while they went down for other patients (suggestive of an improvement of AD). This figure was called a [spaghetti plot](https://en.wikipedia.org/wiki/Spaghetti_plot), because it shows a lot of individual lines that all go in slightly different directions.
		- Figure 4 looks like it is showing the same data in a different way, one that is supposed to be easier to interpret. The Y-axis is labeled as “Percent CFB”, the change-from-baseline. I will assume here it is the percentage of change as explained in this [Wikipedia article](https://en.wikipedia.org/wiki/Percentage#Percentage_increase_and_decrease). Say, a patient’s P-tau181 was 5 units on day 1 and 10 units on day 28, that is an increase of 5 points, so it would count as a 100% increase (+100%). Similarly, if a patient’s measurement was 5 on day 1 and 2.5 on day 28, it went down 2.5 points, which would count as 50% decrease (-50%). If a the value did not change at all, that would be plotted as 0% change.
		- Each colored dot is the difference between day 28 and day 1 for each individual patients, shown for each of the three groups. The small horizontal lines in each group represent the mean increase/decrease for each of the three groups, while the dotted horizontal line highlights the 0% change value.
		- As you can see in Figure 4, the average plasma P-tau181 values in the patients in the placebo group increased a bit after 28 days (_above_ the dotted line), suggesting their disease got a bit worse. In contrast, the two groups of patients who received Simufilam – either 50 mg or 100 mg – ended up with average P-tau181 values a bit _under_ the dotted line, suggesting they improved a bit.
		- ### Concerns about Figures 4 and 5
			
		- Figures 4 and 5 are presumably two figures showing the same data points plotted in two alternative ways. However, there appear to be some unexpected differences between the data points in the two figures. These discrepancies between Figures 4 and 5 have been pointed out in the Labaton Sucharow (LS) [Statement of Concern](https://www.regulations.gov/docket/FDA-2021-P-0930/document) report filed to the FDA on August 18, 2021, and were further analyzed by [Luosheng Peng](https://twitter.com/LuoshengPeng/status/1431376982718095362) on Twitter. I agree with those concerns, and will reword them here, and also look at them in more detail.
		- ### Discrepancies between Figures 4 and 5
			
		- 1. The poster states that **64 patients** were included in the study, and randomly assigned to three groups. There are no details given about how many patients were assigned to each group, but we would expect roughly 20 people per group. Yet, Figure 4 only shows 20, 15, and 17 data points for the placebo, 50 mg, and 100 mg Simufilam groups, respectively. This is a total of **52 patients**. What happened to the 12 other patients? If fewer data points from the treatment groups are reported, does this mean that data points from the treatment groups have been left out? It would be nice if Cassava scientists could explain what happened with those 12 patients who appear to have dropped out of the study.
		- 2. While Figure 4 shows 20/15/17 (**sum=52**) data points for the three groups, Figure 5 appears to show 18/15/18 data points (**sum=51**). The numbers of the placebo and 100 mg treatment groups therefore do not match.
		- 3. This is a minor issue, but the **color scheme** confusingly changes from Figure 4 to Figure 5. While the 50 mg Simufilam remains blue, the placebo group switches from red to green and the 100 mg Simufilam group switches from green to red.
		- 4. The biggest concern is that some of the data points do not seem to match up between the two figures. Of particular note, in Figure 5, the P-tau181 value from a patient in the 100 mg treatment group went up from ~2.1 to ~5.2 pg/ml, which is an increase of 150%. In other words, one of the patients in the 100 mg treatment group showed a large increase of the Alzheimer’s disease biomarker . Yet, this particular data point is missing in the 100 mg treatment group in Figure 4. Instead, **the 150% increase data point is included in the placebo group**.
		- Update: _The [Clinical Trials page belonging to this study](https://clinicaltrials.gov/ct2/show/results/NCT04079803) has more information on the numbers of patients in each of the groups who completed the study: 22/20/21. The patient numbers of CSF P-tau181 were 22/19/18 respectively, but no numbers are provided for the serum P-tau181 levels._
			- #inpeer/how/practices/review/paper/layers/empirical/rigor/intConsistency/preregDev 
		- Update 2: _The LS report stated that the missing data point in the 100 mg group in Figure 4 should have been around 235% – based on an estimated increase from 1.5 to 5 pg/ml. Using WebPlotDigitizer (see below), this estimate appears too high. The LS report did not notice that the placebo group had an additional data point of 150% that does not match Figure 5’s data. Luosheng Peng correctly estimated in a [Twitter thread](https://twitter.com/LuoshengPeng/status/1431376982718095362) that the missing data point should be around 150% and also found it in the placebo group._
		- ### A more precise comparison of Figures 4 and 5
			
		- I did a more precise look at the estimated CFB percentages, by extracting the values in Figure 5 using [WebPlotDigitizer](https://apps.automeris.io/wpd/). Since the spaghetti plot was a bit busy, I did not include all data points, but I focused on the lines that showed the biggest changes between day 1 and day 28, leaving out some lines that were horizontal-ish.
			- #inpeer/evdInfra/what/reviewTools/forensic/stats/dataExtr 
		- Looking at the estimated change-percentages, Figure 5’s estimated values appear to line up nicely with the position of the data points in Figure 4. Except, that is, for **the 150% data point, which seems to have jumped from the 100 mg treatment group to the Placebo group**. If this one outlier data point, specifically mentioned in the text of the poster, had been included in the 100 mg treatment group, the average change-from-baseline would change from -17% to around -3%, which is a much less spectacular reduction of plasma P-tau181 levels than claimed by the company.
		- Please note that I am not suggesting here that moving this data point from the treatment group to the placebo group was done on purpose. Mistakes can happen, in particular if there is a rush to publish, and I do not know exactly what has happened here.
		- I hope Cassava Sciences can show more details and exact measurements of all 64 patients included here
			#inpeer/how/practices/review/paper/frames/pedagogical/cautiousCaveats 
		- ### Disclosures
			
		- I do not own any Cassava Sciences shorts or stock, nor stock from other pharmaceutical companies that might be working on competing drugs
		- I was not involved in the publication of the Labaton Sucharow report, and only heard about this case on August 25, after it was discussed on Twitter [here](https://twitter.com/MSollender/status/1430288115990626307) and [here](https://twitter.com/twhitfill/status/1430296059843170305).
		- I was not paid by any person or organization to investigate these allegations, to analyze these papers, or to write this post.
		- I get donations through Patreon for my ongoing work on science integrity, but no one asked me to work on the analysis in this blog post as a condition for their donation.
		- This post is no accusation of misconduct, just a summary of image problems, some of which could be resolved if the researchers can show the original data.
		- This post is not meant to be financial advice. I am a scientist specializing in photographic scientific figures, and I know almost nothing about the stock market.