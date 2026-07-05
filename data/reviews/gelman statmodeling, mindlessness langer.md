---
type: review
noteID: 718e85be-3e7d-4858-bf59-e182dc9006f6
status: complete
source: https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/
---
_This is a long post, so let me give you the tl;dr right away: Don’t use the word “whom” in your dating profile._

OK, now for the story. Fasten your seat belts, it’s going to be a bumpy night.

It all started with this message from Dmitri with subject line, “Man I hate to do this to you but …”, which continued:

> How could I resist?
> 
> https://www.cnbc.com/2024/02/15/using-this-word-can-make-you-more-influential-harvard-study.html
> 
> I’m sorry, let me try again … I had to send this to you BECAUSE this is the kind of obvious shit you like to write about. I like how they didn’t even do their own crappy study they just resurrected one from the distant past.

OK, ok, you don’t need to shout about it!

Following the link we see this breathless ~press release~ NBC news story:

> Using this 1 word more often can make you 50% more influential, says Harvard study
> 
> Sometimes, it takes a single word — like “because” — to change someone’s mind.
> 
> That’s according to Jonah Berger, a marketing professor at the Wharton School of the University of Pennsylvania who’s compiled a list of “magic words” that can change the way you communicate. Using the word “because” while trying to convince someone to do something has a compelling result, he tells CNBC Make It: More people will listen to you, and do what you want.
> 
> Berger points to a nearly 50-year-old study from Harvard University, wherein researchers sat in a university library and waited for someone to use the copy machine. Then, they walked up and asked to cut in front of the unknowing participant.
> 
> They phrased their request in three different ways:
> 
> “May I use the Xerox machine?”  
> “May I use the Xerox machine because I have to make copies?”  
> “May I use the Xerox machine because I’m in a rush?”  
> Both requests using “because” made the people already making copies more than 50% more likely to comply, researchers found. Even the second phrasing — which could be reinterpreted as “May I step in front of you to do the same exact thing you’re doing?” — was effective, because it indicated that the stranger asking for a favor was at least being considerate about it, the study suggested.
> 
> “Persuasion wasn’t driven by the reason itself,” Berger wrote in a book on the topic, “Magic Words,” which published last year. “It was driven by the power of the word.” . . .

Let’s look into this claim. The first thing I did was [click to the study](https://www.habilidadsocial.com/wp-content/uploads/2015/10/copy-machine-study-ellen-langer.pdf)—full credit to CNBC Make It for providing the link—and here’s the data summary from the experiment:

![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-17.57.15-1024x653.png)

If you look carefully and do some simple calculations, you’ll see that the percentage of participants who complied was 37.5% under treatment 1, 50% under treatment 2, and 62.5% under treatment 3. So, ok, not literally true that both requests using “because” made the people already making copies more than 50% more likely to comply: 0.50/0.375 = 1.33, and increase of 33% is not “more than 50%.” But, sure, it’s a positive result. There were 40 participants in each treatment, so the standard error is approximately 0.5/sqrt(40) = 0.08 for each of those averages. The key difference here is 0.50 – 0.375 = 0.125, that’s the difference between the compliance rates under the treatments “May I use the Xerox machine?” and “May I use the Xerox machine because I have to make copies?”, and this will have a standard error of approximately sqrt(2)\*0.08 = 0.11.

The quick summary from this experiment: an observed difference in compliance rates of 12.5 percentage points, with a standard error of 11 percentage points. I don’t want to say “not statistically significant,” so let me just say that the estimate is highly uncertain, so I have no real reason to believe it will replicate.

But wait, you say: the paper was published. Presumably it has a statistically significant p-value somewhere, no? The answer is, yes, they have some “p < .05" results, just not of that particular comparison. Indeed, if you just look at the top rows of that table (Favor = small), then the difference is 0.93 - 0.60 = 0.33 with a standard error of sqrt(0.6\*0.4/15 + 0.93\*0.07/15) = 0.14, so that particular estimate is just more than two standard errors away from zero. Whew! But now we're getting into forking paths territory: - Noisy data - Small sample - Lots of possible comparisons - Any comparison that's statistically significant will necessarily be huge - Open-ended theoretical structure that could explain just about any result. I'm not saying the researchers were trying to anything wrong. But remember, honesty and transparency [are not enuf](http://www.stat.columbia.edu/~gelman/research/published/ChanceEthics14.pdf). Such a study is just too noisy to be useful.

But, sure, back in the 1970s many psychology researchers [not named Meehl](https://statmodeling.stat.columbia.edu/2016/05/06/needed-an-intellectual-history-of-research-criticism-in-psychology/) weren’t aware of these issues. They seem to have been under the impression that if you gather some data and find something statistically significant for which you could come up with a good story, that you’d discovered a general truth.

What’s less excusable is a journalist writing this in the year 2024. But it’s no surprise, conditional on the headline, “Using this 1 word more often can make you 50% more influential, says Harvard study.”

But what about that book by the University of Pennsylvania marketing professor? I searched online, and, fortunately for us, the bit about the Xerox machine is right there in the first chapter, in the excerpt we can read for free. [Here it is](https://www.amazon.com/Magic-Words-Jonah-Berger/dp/0063204932/ref=sr_1_1?crid=3CFNGVHH768I1&keywords=jonah+berger&qid=1708043000&sprefix=jonah+berger%2Caps%2C82&sr=8-1&asin=0063204932&revisionId=&format=4&depth=1):

> ![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-19.26.18.png)
> 
> ![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-19.27.25-627x1024.png)
> 
> ![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-19.29.06.png)

He got it wrong, just like the journalist did! It’s **not true** that including the meaningless reason increased persuasion just as much as the valid reason did. Look at the data! The outcomes under the three treatment were 37.5%, 50%, and 62.5%. 50% – 37.5% ≠ 62.5% – 37.5%. Ummm, ok, he could’ve said something like, “Among a selected subset of the data with only 15 or 16 people in each treatment, including the meaningless reason increased persuasion just as much as the valid reason did.” But that doesn’t sound so impressive! Even if you add something like, “and it’s possible to come up with a plausible theory to go with this result.”

The book continues:

> ![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-19.30.08.png)

Given the flaws in the description of the copier study, I’m skeptical about these other claims.

But let me say this. If it is indeed true that using the word “whom” in online dating profiles makes you 31% more likely to get a date, then my advice is . . . don’t use the word “whom”! Think of it from a potential-outcomes perspective. Sure, you want to get a date. But do you really want to go on a date with someone who will only go out with you if you use the word “whom”?? That sounds like a really pretentious person, not a fun date at all!

OK, I haven’t read the rest of the book, and it’s possible that somewhere later on the author says something like, “OK, I was exaggerating a bit on page 4 . . .” I doubt it, but I guess it’s possible.

**Replications, anyone?**

To return to the topic at hand: In 1978 a study was conducted with 120 participants in a single location. The study was memorable enough to be featured in a business book nearly fifty years later.

Surely the finding has been replicated?

I’d imagine yes; on the other hand, if it had been replicated, this would’ve been mentioned in the book, right? So it’s hard to know.

I did a search, and the article does seem to have been influential:

![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-20.02.44-1024x226.png)

It’s been cited 1514 times—that’s a lot! Google lists 55 citations in 2023 alone, and in what seem to be legit journals: Human Communication Research, Proceedings of the ACM, Journal of Retailing, Journal of Organizational Behavior, Journal of Applied Psychology, Human Resources Management Review, etc. Not core science journals, exactly, but actual applied fields, with unskeptical mentions such as:

> ![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-20.07.44-1024x190.png)
> 
> ![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-20.08.46-1024x92.png)
> 
> ![](https://statmodeling.stat.columbia.edu/wp-content/uploads/2024/02/Screenshot-2024-02-15-at-20.10.23-1024x139.png)

What about replications? I searched on \*langer blank chanowitz 1978 replication\* and found [this paper](https://psycnet.apa.org/journals/psp/48/3/600.pdf) by Folkes (1985), which reports:

> Four studies examined whether verbal behavior is mindful (cognitive) or mindless (automatic). All studies used the experimental paradigm developed by E. J. Langer et al. In Studies 1–3, experimenters approached Ss at copying machines and asked to use it first. Their requests varied in the amount and kind of information given. Study 1 (82 Ss) found less compliance when experimenters gave a controllable reason (“… because I don’t want to wait”) than an uncontrollable reason (“… because I feel really sick”). In Studies 2 and 3 (42 and 96 Ss, respectively) requests for controllable reasons elicited less compliance than requests used in the Langer et al study. Neither study replicated the results of Langer et al. Furthermore, the controllable condition’s lower compliance supports a cognitive approach to social interaction. In Study 4, 69 undergraduates were given instructions intended to increase cognitive processing of the requests, and the pattern of compliance indicated in-depth processing of the request. Results provide evidence for cognitive processing rather than mindlessness in social interaction.

So this study concludes that the result didn’t replicate at all! On the other hand, it’s only a “partial replication,” and indeed they do not use the same conditions and wording as in the original 1978 paper. I don’t know why not, except maybe that exact replications traditionally get no respect.

Langer et al. responded in that journal, writing:

> We see nothing in her results \[Folkes (1985)\] that would lead us to change our position: People are sometimes mindful and sometimes not.

Here they’re referring to the table from the 1978 study, reproduced at the top of this post, which shows a large effect of the “because I have to make copies” treatment under the “Small Favor” condition but no effect under the “Large Favor” condition. Again, given the huge standard errors here, we can’t take any of this seriously, but if you just look at the percentages without considering the uncertainty, then, sure, that’s what they found. Thus, in their response to the partial replication study that did not reproduce their results, Langer et al. emphasized that their original finding was not a main effect but an interaction: “People are sometimes mindful and sometimes not.”

That’s fine. Psychology studies often measure interactions, as they should: the world is a highly variable place.

But, in that case, everyone’s been misinterpreting that 1978 paper! When I say “everybody,” I mean this recent book by the business school professor and also the continuing references to the paper in the recent literature.

Here’s the deal. The message that everyone seems to have learned, or believed they learned, from the 1978 paper is that meaningless explanations are as good as meaningful explanations. But, according to the authors of that paper when they responded to criticism in 1985, the true message is that this trick works sometimes and sometimes not. That’s a much weaker message.

Indeed the study at hand is too small to draw any reliable conclusions about any possible interaction here. The most direct estimate of the interaction effect from the above table is (0.93 – 0.60) – (0.24 – 0.24) = 0.33, with a standard error of sqrt(0.93\*0.07/15 + 0.60\*0.40/15 + 0.24\*0.76/25 + 0.24\*0.76/25) = 0.19. So, no, I don’t see much support for the claim in this post from Psychology Today:

> So what does this all mean? When the stakes are low people will engage in automatic behavior. If your request is small, follow your request with the word “because” and give a reason—any reason. If the stakes are high, then there could be more resistance, but still not too much.

This happens a lot in unreplicable or unreplicated studies: a result is found under some narrow conditions, and then it is taken to have very general implications. This is just an unusual case where the authors themselves pointed out the issue. As they wrote in their 1985 article:

> The larger concern is to understand how mindlessness works, determine its consequences, and specify better the conditions under which it is and is not likely to occur.

That’s a long way from the claim in that business book that “because” is a “magic word.”

Like a lot of magic, it only works under some conditions, and you can’t necessarily specify those conditions ahead of time. It works when it works.

There might be other replication studies of this copy machine study. I guess you couldn’t really do it now, because people don’t spend much time waiting at the copier. But the office copier was a thing for several decades. So maybe there are even some exact replications out there.

In searching for a replication, I did come across [this post](https://languagelog.ldc.upenn.edu/nll/?p=1396) from 2009 by Mark Liberman that criticized yet another hyping of that 1978 study, this time from a paper by psychologist Daniel Kahenman in the American Economic Review. Kahneman wrote:

> Ellen J. Langer et al. (1978) provided a well-known example of what she called “mindless behavior.” In her experiment, a confederate tried to cut in line at a copying machine, using various preset “excuses.” The conclusion was that statements that had the form of an unqualified request were rejected (e.g., “Excuse me, may I use the Xerox machine?”), but almost any statement that had the general form of an explanation was accepted, including “Excuse me, may I use the Xerox machine because I want to make copies?” The superficiality is striking.

As Liberman writes, this represented a “misunderstanding of the 1978 paper’s results, involving both a different conclusion and a strikingly overgeneralized picture of the observed effects.” Liberman performs an analysis of the data from that study which is similar to what I have done above.

Liberman summarizes:

> The problem with Prof. Kahneman’s interpretation is not that he took the experiment at face value, ignoring possible flaws of design or interpretation. The problem is that he took a difference in the distribution of behaviors between one group of people and another, and turned it into generic statements about the behavior of people in specified circumstances, as if the behavior were uniform and invariant. The resulting generic statements make strikingly incorrect predictions even about the results of the experiment in question, much less about life in general.

**Mindfulness**

The key claim of all this research is that people are often _mindless_: they respond to the form of a request without paying attention to its context, with “because” acting as a “magic word.”

I would argue that this is exactly the sort of mindless behavior being exhibited by the people who are promoting that copying-machine experiment! They are taking various surface aspects of the study and using it to draw large, unsupported conclusions, without being mindful of the details.

In this case, the “magic words” are things like “p < .05," "randomized experiment," "Harvard," "peer review," and "Journal of Personality and Social Psychology" ([this](https://statmodeling.stat.columbia.edu/2019/01/27/jpsp-done-bem-paper-back-2010-click-find-surprisingly-simple-answer/) notwithstanding). The mindlessness comes from not looking into what exactly was in the paper being cited.

**In conclusion . . .**

So, yeah, thanks for nothing, Dmitri! Three hours of my life spent going down a rabbit hole. But, hey, if any readers who are single have read far enough down in the post to see my advice not to use “whom” in your data profile, it will all have been worth it.

Seriously, though, the “mindlessness” aspect of this story is interesting. The point here is not, Hey, a 50-year-old paper has some flaws! Or the no-less-surprising observation: Hey, a pop business book exaggerates! The part that fascinates me is that there’s all this shaky research that’s being taken as strong evidence that consumers are mindless—and the people hyping these claims are themselves demonstrating the point by mindlessly following signals without looking into the evidence.

The ultimate advice that the mindfulness gurus are giving is not necessarily so bad. For example, here’s the conclusion of that online article about the business book:

> Listen to the specific words other people use, and craft a response that speaks their language. Doing so can help drive an agreement, solution or connection.
> 
> “Everything in language we might use over email at the office … \[can\] provide insight into who they are and what they’re going to do in the future,” says Berger.

That sounds ok. Just forget all the blather about the “magic words” and the “superpowers,” and forget the unsupported and implausible claim that “Arguments, requests and presentations aren’t any more or less convincing when they’re based on solid ideas.” As often is the case, I think these Ted-talk style recommendations would be on more solid ground if they were just presented as the product of common sense and accumulated wisdom, rather than leaning on some 50-year-old psychology study that just can’t bear the weight. But maybe you can’t get the airport book and the Ted talk without a claim of scientific backing.

Don’t get me wrong here. I’m not attributing any malign motivations to any of the people involved in this story (except for Dmitri, I guess). I’m guessing they really believe all this. And I’m not using “mindless” as an insult. We’re all mindless sometimes—that’s the point of the Langer et al. (1978) study; it’s what Herbert Simon called “bounded rationality.” The trick is to recognize your areas of mindlessness. If you come to an area where you’re being mindless, don’t write a book about it! Even if you naively think you’ve discovered [a new continent](https://statmodeling.stat.columbia.edu/2021/05/23/thinking-fast-slow-and-not-at-all-system-3-jumps-the-shark/). As Mark Twain apparently never said, it ain’t what you don’t know that gets you into trouble. It’s what you know for sure that just ain’t so.

**The usual disclaimer**

I’m not saying the claims made by Langer et al. (1978) are wrong. Maybe it’s true that, under conditions of mindlessness, all that matters is the “because” and any empty explanation will do; maybe the same results would show up in a preregistered replication. All I’m saying is that the noisy data that have been presented don’t provide any strong evidence in support of such claims, and that’s what bothers me about all those confident citations in the business literature.

**P.S.**

After writing the above post, I sent this response to Dmitri:

> OK, I just spent 3 hours on this. I now have to figure out what to do with this after blogging it, because I think there are some important points here. Still, yeah, you did a bad thing by sending this to me. These are 3 hours I could’ve spent doing real work, or relaxing . . .

He replied:

> I mean, yeah, that’s too bad for you, obviously. But … try to think about it from my point of view. I am more influential, I got you to work on this while I had a nice relaxing post-Valentine’s day sushi meal with my wife (much easier to get reservations on the 15th and the flowers are a lot cheaper), while you were toiling away on what is essentially my project. I’d say the magic words did their job.

Good point! He exploited my mindlessness. I responded:

> Ok, I’ll quote you on that one too! (minus the V-day details).
> 
> I’m still chewing on your comment that you appreciate the Beatles for their innovation as much as for their songs. The idea that there are lots of songs of similar quality but not so much innovation, that’s interesting. The only thing is that I don’t know enough about music, even pop music, to have a mental map of where everything fits in. For example, I recently heard that Coldplay song, and it struck me that it was in the style of U2 . But I don’t really know if U2 was the originator of that soaring sound. I guess Pink Floyd is kinda soaring too, but not quite in the same way . . . etc etc … the whole thing was frustrating to me because I had no sense of whether I was entirely bullshitting or not.
> 
> So if you can spend 3 hours writing a post on the above topic, we’ll be even.

Dmitri replied:

> I am proud of the whole “Valentine’s day on the 15th” trick, so you are welcome to include it. That’s one of our great innovations. After the first 15-20 Valentine’s days, you can just move the date a day later and it is much easier.

And, regarding the music, he wrote:

> U2 definitely invented a sound, with the help of their producer Brian Eno.
> 
> It is a pretty safe bet that every truly successful musician is an innovator—once you know the sound it is easy enough to emulate. Beethoven, Charlie Parker, the Beatles, all the really important guys invented a forceful, effective new way of thinking about music.

U2 is great, but when I listened to an entire U2 song from beginning to end, it seemed so repetitive as to be unlistenable. I don’t feel that way about the Beatles or REM. But just about any music sounds better to me [in the background](https://statmodeling.stat.columbia.edu/2021/05/24/the-revelation-came-while-hearing-a-background-music-version-of-iron-butterflys-in-a-gadda-da-vida-at-a-mr-steak-restaurant-in-colorado/), which I think is a sign of my musical ignorance and tone-deafness (for real, I’m bad at recognizing pitches) more than anything else. I guess the point is that you’re supposed to dance to it, not just sit there and listen.

Anyway, I warned Dmitri about what would happen if I post his Valentine’s Day trick:

> I post this, then it will catch on, and it will no longer work . . . just warning ya! You’ll have to start doing Valentine’s Day on the 16th, then the 17th, . . .

To which Dmitri responded:

> Yeah but if we stick with it, it will roll around and we will get back to February 14 while everyone else is celebrating Valentines Day on these weird wrong days!

I’ll leave him with the last word.

# Comments
-   Roy on [March 6, 2024 10:32 AM at 10:32 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334055) said:
    
    Whom should I believe in your ending discussion with Dmitri
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334055#respond)
    
    -   ![](https://secure.gravatar.com/avatar/42d678f84a13ded268bf0e89b184c35b?s=39&d=identicon&r=g)Dale Lehman on [March 6, 2024 10:34 AM at 10:34 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334056) said:
	
        Believe Andrew because…
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334056#respond)
        
        -   ![](https://secure.gravatar.com/avatar/0dfadb29bc5b59c26d5a2975ae03bd78?s=39&d=identicon&r=g)John N-G on [March 6, 2024 11:06 AM at 11:06 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334066) said:
            
            OK.
            
            [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334066#respond)
            
-   ![](https://secure.gravatar.com/avatar/d7e3e90dc8fbbcc2d51df749fc62495f?s=68&d=identicon&r=g)paul alper on [March 6, 2024 11:11 AM at 11:11 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334068) said:
    
    For a wonderful treatment of the word “whom” and its proper and evolving place in the English language, see this marvelous discussion
    
    [https://qz.com/salesforce-marc-benioff-hawaii-land-1851308756](https://qz.com/salesforce-marc-benioff-hawaii-land-1851308756)  
    ————————  
    “If “whom” miraculously lives, that is fine. If it dies as it likely will now, that’s fine too. Whether it lives or dies will have no effect on anything. Humans care about our language, so it makes anthropological sense that you might be upset at this, but this is not the biggest thing you should put your attention towards.”  
    ————————  
    However, I warn you that the above website is almost as long as Andrew’s posting. Another unfortunate aspect of that website is that it fails to contrast the deserved or undeserved demise of the word, “whom”, with the currently mandatory and ubiquitous word, “like,” which threatens to obliterate the English language and my personal sanity.
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334068#respond)
    
    -   ![](https://secure.gravatar.com/avatar/3896a79aad5664051f1424137c7b64b7?s=39&d=identicon&r=g)John Richters on [March 6, 2024 6:13 PM at 6:13 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334310) said:
        
        Wrong link to discussion about “whom”. Here’s the right one::
        
        [https://qz.com/1517643/should-we-let-the-word-whom-die](https://qz.com/1517643/should-we-let-the-word-whom-die)
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334310#respond)
        
        -   ![](https://secure.gravatar.com/avatar/d7e3e90dc8fbbcc2d51df749fc62495f?s=39&d=identicon&r=g)paul alper on [March 6, 2024 11:07 PM at 11:07 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334379) said:
            
            Thanks for the correction! One wonders how I managed to butcher the link so completely given my effusive praise for the website. However, I did get the first 15 characters correctly.
            
            [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334379#respond)
            
-   ![](https://secure.gravatar.com/avatar/1f18fa8c90f1f65b7761f94f031a97e5?s=68&d=identicon&r=g)Adede on [March 6, 2024 11:34 AM at 11:34 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334077) said:
    
    Exact replications: the Rodney Dangerfield of science!
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334077#respond)
    
    -   ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [March 6, 2024 11:50 AM at 11:50 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334081) said:
        
        Adede:
        
        As so often [seems to be the case](https://statmodeling.stat.columbia.edu/2024/02/26/when-steve-bannon-meets-the-center-for-open-science-bad-science-and-bad-reporting-combine-to-yield-another-ovulation-voting-disaster/), exact replication here would serve more of a sociological than a scientific purpose, in the following sense: A careful reading of that much-cited 1978 paper reveals the shakiness of its claims. But . . . the paper (a) has been much cited, and (b) continues to be misinterpreted even in its own terms (as can be seen from how it was botched in the above-cited business book).
        
        So an exact replication making clear the noisiness of the experiment would be unlikely to add anything to our understanding of the science of communication/persuasion/decisions/etc., but it could be helpful in the sociological sense of communicating the flaws of that study so that future psychology researchers and writers of business books might not have this confusion about the world.
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334081#respond)
        
-   ![](https://secure.gravatar.com/avatar/d7e3e90dc8fbbcc2d51df749fc62495f?s=68&d=identicon&r=g)paul alper on [March 6, 2024 12:09 PM at 12:09 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334091) said:
    
    Today’s blog begins with the deservedly famous quotation
    
    “Fasten your seat belts, it’s going to be a bumpy night.”
    
    from the (even more deservedly in my mind) famous film, “All About Eve.” To my surprise, some people view the above quotation negatively. It receives a value of “5” as seen by shmoop.com  
    ———————————————————————————————————————–  
    [https://www.shmoop.com/quotes/fasten-your-seatbelts-its-going-to-be-a-bumpy-night.html](https://www.shmoop.com/quotes/fasten-your-seatbelts-its-going-to-be-a-bumpy-night.html)
    
    Pretentious Factor
    
    If you were to drop this quote at a dinner party, would you get an in-unison “awww” or would everyone roll their eyes and never invite you back? Here it is, on a scale of 1-10.  
    ————————————————————————————————————  
    As to the word itself, Shmoop, sounds like I ought to have heard it before but, somehow, it rings no bells.
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334091#respond)
    
-   ![](https://secure.gravatar.com/avatar/098e9ed84d1f0d6978cbcf0bf370ee81?s=68&d=identicon&r=g)Richard on [March 6, 2024 7:30 PM at 7:30 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334320) said:
    
    If you have a moment to indulge an elementary question, can you please help me understand some of your computations? Specifically, I’m trying to understand the standard error computations here:
    
    “There were 40 participants in each treatment, so the standard error is approximately 0.5/sqrt(40) = 0.08 for each of those averages. The key difference here is 0.50 – 0.375 = 0.125, that’s the difference between the compliance rates under the treatments “May I use the Xerox machine?” and “May I use the Xerox machine because I have to make copies?”, and this will have a standard error of approximately sqrt(2)\*0.08 = 0.11.”
    
    I think that the numerator in 0.5/sqrt(40) is just the mean response to the placebic info condition (0.93\*15+0.24\*25)/(15+25) — is that correct? I ask because I’m confused in that I was taught that standard error is sample standard deviation/sqrt(sample size), not sample mean/sqrt(sample size). Again, I’m a novice when it comes to statistics so I know I’m the one who’s confused, I just would appreciate any guidance on why the sample means are used in this case.
    
    For the other standard error of sqrt(2)\*0.08, I get that you’re probably using the standard error you had just computed of 0.5/sqrt(40)=0.08, but where does the sqrt(2) numerator come from?
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334320#respond)
    
    -   ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [March 6, 2024 8:41 PM at 8:41 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334353) said:
        
        Richard:
        
        The standard error of a proportion is sqrt(p\*(1-p)/n). For p that’s not close to 0 or 1, that’s approximately 0.5/sqrt(n).
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334353#respond)
        
        -   ![](https://secure.gravatar.com/avatar/098e9ed84d1f0d6978cbcf0bf370ee81?s=39&d=identicon&r=g)Richard on [March 6, 2024 9:09 PM at 9:09 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334360) said:
            
            Thank you!
            
            [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334360#respond)
            
    -   ![](https://secure.gravatar.com/avatar/0e27678900b6d0c17c9f343c85810c17?s=39&d=identicon&r=g)Gadi on [March 12, 2024 3:58 AM at 3:58 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2338637) said:
        
        Richard, I too had problem with the sqrt(2) part, so a bit of a search for the correct terminology led me to a calculation for the Standard Error of the Difference of two Means:  
        SE\_difference = \\sqrt{ (SE\_mean1)^2 + (SE\_mean2)^2 }  
        Since here both SE\_means are the same = 0.08,  
        \\sqrt{ 0.08^2 + 0.08^2 } = \\sqrt{ 2 \* 0.08^2} = \\sqrt{2} \* \\sqrt{0.08^2} = \\sqrt{2}\*0.08
        
        source: [https://www.youtube.com/watch?v=0oX1BqS-Wkg](https://www.youtube.com/watch?v=0oX1BqS-Wkg)
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2338637#respond)
        
-   ![](https://secure.gravatar.com/avatar/0ed444b0a21f4ba2e3f30521ac0dc318?s=68&d=identicon&r=g)[Raghu Parthasarathy](https://eighteenthelephant.com/) on [March 6, 2024 10:11 PM at 10:11 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334371) said:
    
    I remember reading about this in Cialdini’s “Influence: The Psychology of Persuasion,” a book that I’ve found quite useful for thinking about teaching. It’s disappointing to read that the study underlying it is so pathetic. Such tiny numbers of people! And “small” and “big” favors are just copying 5 or 20 pages. I would have thought “small” is photocopying anything, and a big favor would be “Can I have one of your kidneys?”
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334371#respond)
    
    -   ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [March 6, 2024 10:14 PM at 10:14 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334372) said:
        
        An intermediate-style favor would be, “Can I photocopy one of your kidneys?”
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334372#respond)
        
-   ![](https://secure.gravatar.com/avatar/?s=68&d=identicon&r=g)Anonymous on [March 6, 2024 11:33 PM at 11:33 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334384) said:
    
    One more criticism: if we take the results to be real, can we even describe the behavior as mindless? When talking, people often fumble on their own words or generally fail to articulate their thoughts well, esp. when they are in a hurry. Perhaps it is a sufficient signal that they are trying to be considerate. There’s more interpretations of such a request too (this line cutter’s a madman who’ll yap my ear off if I say no), in any case, it’s rather presumptuous to call the response mindless.
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334384#respond)
    
    -   ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [March 7, 2024 6:58 AM at 6:58 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334523) said:
        
        Yes, good point!
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334523#respond)
        
-   ![](https://secure.gravatar.com/avatar/?s=68&d=identicon&r=g)Carlos Ungil on [March 7, 2024 9:46 AM at 9:46 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334722) said:
    
    \> If you look carefully and do some simple calculations, you’ll see that the percentage of participants who complied was 37.5% under treatment 1, 50% under treatment 2, and 62.5% under treatment 3. So, ok, not literally true that both requests using “because” made the people already making copies more than 50% more likely to comply
    
    It seems clear that this was a reference to the “small favor” experiment – where it’s literally true that the observed compliance increased my more that 50% (0.60 to 0.93/0.94).
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334722#respond)
    
    -   ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [March 7, 2024 10:24 AM at 10:24 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334746) said:
        
        Carlos:
        
        Yes, there is a subset of the data for which that claim is correct. But just about any claim can be made correct if you choose the right subset of the data! If someone makes a general statement about an experiment and it turns out that the claim only applies in a selected subset, I’d say that’s a false claim.
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334746#respond)
        
        -   ![](https://secure.gravatar.com/avatar/cbf7434d6ca709804bad6c7935a64048?s=39&d=identicon&r=g)Carlos Ungil on [March 7, 2024 11:05 AM at 11:05 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334769) said:
            
            Sure, it can be misleading. Nevertheless, I’d say that my remark is relevant if you had missed that (even though they failed to mention it) the “false claim” was about “small” favors – and may be even more relevant if you had noticed it but choose not to mention it.
            
            [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334769#respond)
            
            -   ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [March 7, 2024 11:37 AM at 11:37 am](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334795) said:
                
                Carlos:
                
                Yes, I was aware that it was likely that they were referring just to that subset; I didn’t mention it right there in my post because the same issue came up elsewhere.
                
-   ![](https://secure.gravatar.com/avatar/d05d3f9db0b2c399412a66882dfa2f47?s=68&d=identicon&r=g)Dan Riley on [March 7, 2024 12:43 PM at 12:43 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2334827) said:
    
    “Hey baby, can I use the Xerox machine, because I’m from another planet” -ZB
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2334827#respond)
    
-   ![](https://secure.gravatar.com/avatar/a2dad8a01c0a098b19132aeefd96869f?s=68&d=identicon&r=g)Jay Patel on [March 8, 2024 3:43 PM at 3:43 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2335999) said:
    
    Language Log, a group linguistics blog, analyzed the Langer studies years and years ago. They found the claim shaky and also noted the confounding issues of request length.
    
    It’d be great to have an easy way to aggregate these examples of organic peer review like an advanced form of Hypothesis or just automatically depositing ideas in PubPeer through software.
    
    See: [https://languagelog.ldc.upenn.edu/nll/?p=1396](https://languagelog.ldc.upenn.edu/nll/?p=1396)
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/?replytocom=2335999#respond)
    
    -   ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [March 8, 2024 4:08 PM at 4:08 pm](https://statmodeling.stat.columbia.edu/2024/03/06/mindlessness-in-the-interpretation-of-a-study-on-mindlessness/#comment-2336023) said:
        
        Jay:
        
        Yes, I saw that post and linked to it above. My post is pretty long so maybe you didn’t notice it, but it’s there; just search on Liberman.
