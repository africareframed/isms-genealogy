---
title: Scaling laws
order: 1
ready: true
summary: Regular curves on which an AI model's error falls as its size, data and computing power grow.
image: collage-scale
pageImage: collage-scale-tall
lead: Scaling laws hold that AI models improve along a smooth, predictable curve as they grow and take in more data and computing power.
isms:
  - ism: singularitarianism
    text: Sam Altman builds his forecasts on them. In February 2025 he wrote that a model's intelligence “roughly equals the log of the resources used to train and run it”.
  - ism: effective-altruism
    text: 80,000 Hours reads the curves as a reason for urgency. In 2025 Benjamin Todd wrote that from GPT-2 to GPT-4 the biggest driver of progress was far more computing power for the same techniques. If current trends hold a few more years, he argued, AGI before 2030 is a serious possibility.
  - ism: ai-ethics
    text: AI ethics questions the bigger-is-better path. “On the Dangers of Stochastic Parrots” (2021) asked whether language models can be too big, pointing to their environmental costs and to training data too vast to document.
strands:
  - name: The bitter lesson
    text: Richard Sutton's 2019 essay draws one lesson from seventy years of AI research. General methods that use more computation, such as search and learning, have beaten methods built on human knowledge. He credits the steadily falling cost of computation.
    source: Rich Sutton, “The Bitter Lesson”, incompleteideas.net, 13 March 2019
  - name: Compute-optimal training
    text: In 2022 a DeepMind team found that large language models had been “significantly undertrained”. For a fixed budget, model size and training data should grow together. Their 70-billion-parameter model, Chinchilla, used the same compute as the 280-billion-parameter Gopher and outperformed it.
    source: Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch and others, “Training Compute-Optimal Large Language Models”, arXiv:2203.15556, 29 March 2022
  - name: Test-time scaling
    text: In September 2024 OpenAI reported that its o1 model improved with more training compute and with more time spent thinking. That opened a second curve, which spends more computation on each answer as well as on training.
    source: OpenAI, “Learning to Reason with LLMs”, openai.com, 12 September 2024
words:
  - the bitter lesson
  - power law
  - compute-optimal
  - the scaling hypothesis
  - test-time compute
  - frontier model
  - the age of scaling
disputes: Gary Marcus argued that scaling laws are “mere observations that might not hold forever”, unlike gravity (Nautilus, 2022). Ilya Sutskever, a co-founder of OpenAI, said in November 2025 that the age of scaling was giving way to an age of research. He doubted that a hundred times more scale would transform results, so progress again depends on new ideas (Dwarkesh Podcast).
# Sources for the introduction, rows and disputes (for the checker):
# - Joel Hestness and others (Baidu Research), "Deep Learning Scaling is Predictable, Empirically", arXiv:1712.00409, 1 December 2017
# - Jared Kaplan and others, "Scaling Laws for Neural Language Models", arXiv:2001.08361, 23 January 2020 (abstract: "some trends spanning more than seven orders of magnitude")
# - Sam Altman, "Three Observations", blog.samaltman.com/three-observations, 9 February 2025 (post timestamp)
# - Benjamin Todd, "Will we have AGI by 2030?", 80,000 Hours, first published March 2025, 80000hours.org/agi/guide/when-will-agi-arrive/
# - Ajeya Cotra, "Draft report on AI timelines", LessWrong, 18 September 2020 (forecasters use the curves)
# - Gary Marcus, "Deep Learning Is Hitting a Wall", Nautilus, 10 March 2022
# - Ilya Sutskever, "We're moving from the age of scaling to the age of research", Dwarkesh Podcast, 25 November 2025, dwarkesh.com/p/ilya-sutskever-2
status: checked
---

Scaling laws describe how an AI model improves as it grows. Plot its error against its size, its data or its computing power, and the points fall on a smooth curve. Labs use the curves to decide how to spend a fixed computing budget.

Researchers at Baidu fitted such curves in 2017, for translation, language, images and speech. In January 2020 Jared Kaplan and colleagues at OpenAI published “Scaling Laws for Neural Language Models”. Some of its trends held across more than seven orders of magnitude.

The curves made scale a strategy: bigger models, more data, more chips. Company leaders cite them, and forecasters use them to date the arrival of AGI. Whether they keep holding is the open question.
