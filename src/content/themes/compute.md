---
title: Compute
order: 2
ready: true
summary: The computing power AI runs on, from the chips to the data centres and the electricity that feeds them.
image: collage-power
pageImage: collage-power-tall
lead: "Compute is the computing power that trains and runs AI: states ration it, companies race to build it and laws measure models by it."
isms:
  - ism: singularitarianism
    text: Sam Altman ties what AI can do to how much compute is built. With 10 gigawatts, he wrote in September 2025, AI might work out how to cure cancer. He set OpenAI the aim of a factory producing “a gigawatt of new AI infrastructure every week”.
  - ism: rationalism
    text: Compute is what rationalists would cap. In 2023 Eliezer Yudkowsky called for shutting down large GPU clusters and tracking every GPU sold. The draft treaty on the website of his 2025 book with Nate Soares bans training runs above 10²⁴ FLOP.
  - ism: effective-altruism
    text: Effective altruists have tried to date AI by the compute it would need. Ajeya Cotra's 2020 draft report, written at Open Philanthropy, anchored its estimates on the human brain and on evolution. Its median for transformative AI was about 2050.
  - ism: effective-accelerationism
    text: One of its founders works on the hardware itself. Guillaume Verdon, who posted as Beff Jezos, runs Extropic, which builds chips meant to use far less energy than GPUs. Once it succeeds, it says, “energy constraints will no longer limit AI scaling”.
  - ism: ai-ethics
    text: AI ethics sees compute as a source of corporate power. In 2023 the AI Now Institute called it “profoundly monopolized at key points in the supply chain”, which lets a few firms shape who can build AI.
  - ism: pro-human
    text: The pro-human movement would cap compute and challenge the data centres. Anthony Aguirre's Keep the Future Human (2025) proposes hard limits on the computing power used for AI. In 2026 the conservative group Humans First drove a bus marked “AI Data Center Revolt” through 28 states.
strands:
  - name: Export controls
    text: On 26 August 2022 the US government told Nvidia it needed a licence to export its A100 and H100 chips to China and Russia. That October the Commerce Department added licence rules for advanced chips and chipmaking tools bound for China. It cited national security.
    source: "NVIDIA Corporation, Form 8-K on the notice of 26 August 2022, US Securities and Exchange Commission; Bureau of Industry and Security, US Department of Commerce, “Commerce Implements New Export Controls on Advanced Computing and Semiconductor Manufacturing Items to the People's Republic of China”, 7 October 2022"
  - name: Compute thresholds
    text: Laws now measure models by the compute used to train them. The EU's AI Act presumes high-impact capabilities in a general-purpose model trained with more than 10²⁵ FLOP. A US executive order of October 2023 required reports on models above 10²⁶ operations, until President Trump revoked it on 20 January 2025.
    source: "Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 51, Official Journal of the European Union, 12 July 2024; Executive Order 14110, “Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence”, 30 October 2023, section 4.2(b), Federal Register; Kyle Wiggers, “President Trump repeals Biden's AI executive order”, TechCrunch, 20 January 2025"
  - name: Data centres and power
    text: Compute now means buildings and power lines. In April 2025 the International Energy Agency projected that data centres would use about 945 terawatt-hours by 2030, up from 415 in 2024. That is roughly what Japan uses in a year today, and AI is the main driver.
    source: International Energy Agency, Energy and AI, April 2025, as reported by Sophia Chen, “Data Centers Will Use Twice as Much Energy by 2030—Driven by AI”, Scientific American (from Nature), 10 April 2025
words:
  - FLOP
  - GPU
  - data centre
  - export controls
  - compute threshold
  - gigawatt
  - Moore's law
disputes: Sara Hooker finds compute thresholds a poor guide to risk, as the link between compute and risk is highly uncertain and changing fast (2024). Nvidia's chief executive, Jensen Huang, called US export controls “a failure” in May 2025, saying they spurred Chinese rivals (Fortune). In December 2024 DeepSeek reported training its V3 model on only 2.788 million GPU hours. When its R1 model drew attention in January 2025, Nvidia's shares fell about 17% in a day (Axios).
# Sources for the introduction, rows and disputes (for the checker):
# - Amazon Web Services, "Announcing Amazon Elastic Compute Cloud (Amazon EC2) - beta", 24 August 2006
# - Dario Amodei and Danny Hernandez, "AI and Compute", OpenAI, 16 May 2018
# - Sam Altman, "Abundant Intelligence", blog.samaltman.com/abundant-intelligence, 23 September 2025 (post timestamp; 10 gigawatts and cancer, gigawatt a week)
# - Eliezer Yudkowsky, "Pausing AI Developments Isn't Enough. We Need to Shut it All Down", TIME, 29 March 2023
# - "A Draft of a Treaty, with Annotations", ifanyonebuildsit.com/treaty, Article IV
# - Ajeya Cotra, "Draft report on AI timelines", LessWrong, 18 September 2020
# - Extropic, "Thermodynamic computing from zero to one", extropic.ai; Verdon as Beff Jezos: entry effective-accelerationism/2023-beff-jezos-named
# - Sara Hooker, "On the Limitations of Compute Thresholds as a Governance Strategy", arXiv:2407.05694, July 2024
# - Stuart Dyos, "Jensen Huang blasts U.S. curbs on the sale of Nvidia chips to China", Fortune, 22 May 2025
# - DeepSeek-AI, "DeepSeek-V3 Technical Report", arXiv:2412.19437, 27 December 2024 (2.788M H800 GPU hours); Axios, "Nvidia shares plunge as DeepSeek promises new AI path", 27 January 2025 (down more than 17% at 3:45 pm; the close was about 17%)
status: checked
---

In AI, compute means the computation used to train or run a model, counted in floating-point operations, or FLOP. It comes from specialised chips, such as Nvidia's H100, housed in data centres.

The word comes from computing jargon. In 2006 Amazon launched its Elastic Compute Cloud, renting out “resizable compute capacity”.

In 2018 Dario Amodei and Danny Hernandez of OpenAI measured the compute used in the largest AI training runs. Since 2012 it had doubled every 3.4 months, a rise of more than 300,000 times. Compute became the input to watch, and soon the one to control.
