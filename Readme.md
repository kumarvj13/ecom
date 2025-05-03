# Vijay Ecommerce journey with t-5 model

Directory Structure:

ecommerce_project/
│── __init__.py 
├── app.py                  
├── analysis/               
│   ├── __init__.py         
│   ├── session_analysis.py 
│   ├── model.py            
│   └── utils.py           
├── data/                   
│   └── data.json           
└── requirements.txt 

Observation from the data:
==========================

1) I tried to analyize and parse the data through various options and procedures,  taking Gemini, openai, keys, as progressed
noticed that the speed is good with the models , but it costed me , as in the 3 iterations itself, they stoped, also tried
to minimize the cost with by caching and batching, it was costing in both Gemini, openai.

2) tried on Mistral, "EleutherAI/gpt-neo-1.3B" and other models , due to issues on my laptop, it was hard to set up the laptop

3) Decided to go with t5-small or "google/flan-t5-base" , using either of them it worked fine in my env.

4) Noticed adopting some small enhancements their is a possibility of parallel fast retrival and parsing taking chunks of sessions and 
   running them in parallel and aggregating the result before publishing, proper controlled actions should be designed with engines running in parallel.

5) I have not fined tuned the data from the json, taken the pdf and convered it to json on fly and used the json file.

Consideration:
================
Taken the json file from the pdf( did not do any fine tunning), retrived the needed fields, ussed t5 model ,
to capture with enhanced prompt
* AI-Generated Insights:
 * User Experience:
 * Recommendation:

Output:

Read the json data , Process it and collect it in the needed
fields for various analysis ,  Other than this structure, I have tried on Gemini, open AI and developed considering MCP + Agents + streamlit dash board + python 

Taking various analysis on the data, considering the prompts, tried to o/p the results in to 

 * AI-Generated Insights:
 * User Experience:
 * Recommendation:

All the processing is considered taking my laptop position in t0 account.

On GPU, I might have considred other models and work flow, The code shared is considering  my laptop performance in to account


More work that can be considered:
=================================
1) chunk the json file and process them asynchronously
2) add code to handle multiple json files. which can be processed on diffrent engines for analysis and report.
2) create engines and process 3 engines on 2 GPUS for more details report taking the latency and processing time in to account.
3) Process on 3 GPUS (small).
4) On Gemini, I seen it working fast taking the Agents + MCP + Langchain + pytorch in to account, but it costed me 
5) Also tried with langcraph, but it is tool slow .
6) add code to handle multiple json files.
6) The present procees o/p's each session anlysis, but consider a  consolidated report  from all the session, and recommend  where is negative experience was observed, also consider giving points and rewards for long term customers to retain them and pull customers them back to the site for better shopping experence.
7) Add cache techiqunes.


Sample o/p:

* AI-Generated Insights:

. This session represents an abandoned journey, where the user did not complete the purchase. The user added products to the cart but did not complete the purchase. Possible reasons could include: - **Cart Abandonment**: The user may have been distracted or abandoned the checkout process. - **Preferred Payment Option**: The user might have found the prices too high or not worth the purchase.
* User Experience:

The user did not show clear intent to purchase, as no products were added to the cart.
* Recommendation:

Improve product search relevance and provide better product suggestions to align with user needs.
Session ID: s-3ecc81305811
Session ID: s-3ecc81305811

Device: desktop

Country: UK

Referrer: direct

New User: False

Conversion: False

Total Value: $0

* AI-Generated Insights:

: $0 - Activities: They searched for'sofa' and received 0 results. The user viewed 'Modern Makeup B' in the 'beauty/makeup' category, priced at $13.84. The user viewed 'Modern Jackets D' in the 'clothing/jackets' category, priced at $183.02. They added product ID p-1119 to the cart (quantity: 2, value: $27.68
* User Experience:

The user experienced a negative journey, as they added products to the cart but did not complete the purchase. Possible reasons include cart abandonment or price sensitivity.
* Recommendation:

Consider simplifying the checkout process, offering discounts, or sending follow-up reminders to encourage the user to complete their purchase.
Session ID: s-5f0d5a59a18d
Session ID: s-5f0d5a59a18d

Device: mobile

Country: UK

Referrer: instagram

New User: False

Conversion: False

Total Value: $0

* AI-Generated Insights:

, priced at $160.53. This session represents an abandoned journey, where the user did not complete the purchase. The user added products to the cart but did not complete the purchase. Possible reasons could include: - **Cart Abandonment**: The user may have been distracted or abandoned the checkout process. Please analyze the reasons for success or abandonment of the journey, and suggest improvements for abandoned journeys.
* User Experience:

The user did not show clear intent to purchase, as no products were added to the cart.
* Recommendation:

Improve product search relevance and provide better product suggestions to align with user needs.
Session ID: s-ba9107b95c80
Session ID: s-ba9107b95c80

Device: desktop

Country: AU

Referrer: google_ads

New User: False

Conversion: True

Total Value: $504.2

* AI-Generated Insights:

: p-1034 to the cart (quantity: 2, value: $504.2). This session represents a successful journey, where the user completed the purchase. Number of products searched: 0. Number of products added to cart: 1. Please analyze the reasons for success or abandonment of the journey, and suggest improvements for abandoned journeys.
* User Experience:

The user had a positive experience, as they completed the purchase successfully.
* Recommendation:

Since the user made a successful purchase, consider offering personalized recommendations or loyalty rewards to increase engagement and retention.

Running Application:
===================

1) pip install -r requirements.txt

2) streamlit run app.py

Please consider placing the right json, I have not fine tunned the json file or checked
the validity of the file in the analysis.
