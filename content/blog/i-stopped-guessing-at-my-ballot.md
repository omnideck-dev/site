+++
title    = "I stopped guessing at my ballot"
date     = 2026-11-02
draft    = false
tags     = ["Use Cases", "Privacy", "Local AI"]
template = "templates/types/blog.html"

[extra]
description    = "I used AI to walk into the voting booth feeling informed. The setup took one download. The research took one evening. Before you judge, read below."
author         = "Ryan Picchini"
featured_image = "/images/voting-prep.jpg"
+++

## My struggle is probably yours

I have three kids, an amazing wife and a job that's all encompassing. Every election I get a ballot with questions written like this:

> "SHALL THE CITY OF GLENWOOD SPRINGS TAXES BE INCREASED ANNUALLY $3,132,000 IN THE FIRST FULL FISCAL YEAR (2027) BY INCREASING THE CURRENT AD VALOREM TAX RATE BY 7.9 MILLS THROUGH DECEMBER 31, 2046..."

I read it three times, not fully understanding it, and voted based on my limited understanding (or at times worse). That's not voting. It's guessing. I didn't have the capacity to do the research.

## AI seemed like the solution, but I was skeptical

I want to be honest about why this took me so long, because I think my reasons were probably yours too.

I didn't trust that my information would stay mine. If I'm typing my address, my household details, and my voting research into a chat window, what happens to it? Does it train on me? Where does it live? I never got a straight answer I believed.

I assumed it would be too hard to set up. I'm not a developer. Every "just install this" instruction I've followed has ended with a terminal window and me feeling stupid.

And I didn't trust the output. This is the big one. I've watched AI confidently produce wrong answers about things I know well. Why would I trust it about a property tax mill levy?

## So I gave in

Two weeks out from the election and with a packed schedule, I sat down late one evening and asked an AI agent to help me understand all 18 measures I was staring at. Not to tell me how to vote. To explain what each one does. The information isn't hidden, it's just scattered across a 104-page state Blue Book, a county tax notice, the filings behind each measure, and local reporting. Nobody with a Tuesday night to spare is assembling that. So I asked for it assembled.

By the end of the evening I had an 11-page guide written at an eighth-grade reading level, with the exact statutory text in an appendix. It told me which measures were actually mine. I'd assumed a fire district tax applied to me, and it doesn't, because I'm inside city limits. It gave me what each measure changes and the strongest argument on each side, pulled from the arguments the state itself publishes.

Disclosure: the tool I selected was built by one of my best friends, someone I'd trust with my kids. But as you'll see below, it measured up.

Privacy was the first thing I checked. omnideck runs on my own computer. No omnideck account, no telemetry, my work stays in a folder on my machine. If you want to go further, you can run it on a local model so nothing leaves the house. That's not a promise I had to take on faith, it's how the thing is built.

Setup was one download, guided, no terminal. I'm aware of how low that bar sounds. I'm telling you it cleared it.

Trusting the output was the part I expected to break, and it's the one that surprised me. The guide didn't ask me to trust it; it quoted the filed text of the measures so I could check. When I caught an error about my own district, it fixed it. When I said the first draft was too much, it restructured. When it started adding a cover page I didn't want, it took it back out. That back-and-forth is the part I trust most. Less an oracle, more a patient research assistant who doesn't mind being told no.

## The outcome

I've voted in every election since I turned 18. I have never once felt prepared.

I've voted a straight ticket, based on anecdotes or limited information, more times than I'd like to admit. Not because I agreed with everything on it, but because I didn't have the information to do anything else. That's not a partisan confession. It's what most people do, and I think most of us would rather not. This time I walked in knowing what a mill levy was, what it would cost my household, and why someone who cares about the same things I do might still vote the other way. I voted for some things and against others on the same ballot. The effort was one evening. The feeling was new.

## It's your turn

omnideck is open source under Apache 2.0 and free to run on your own machine. Download it at [omnideck.dev/install](/install.html) for macOS, Windows 11, or Linux. No omnideck account. Bring a model key and paste a prompt.

Three that worked for me:

- "Here's my address. Tell me which measures on my November ballot actually apply to me, and which ones I've been told about that don't."
- "Explain each measure in terms an 8th grader could understand. For each: define the jargon first, then what it changes, then the official argument for and against."
- "Pull the actual filed text of this measure from the Secretary of State and quote it exactly. Then explain each clause in plain language."

And it doesn't stop at voting on November 3rd. omnideck helps you with the "next thing" you've been stuck on because of capacity. The meal plan you want to build but it's daunting. The car comparison so you can finally make a choice. The trip that takes too much time to research. Same tool, another evening.
