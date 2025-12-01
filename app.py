import streamlit as st
import os

st.set_page_config(page_title="Mini-Pitch", layout="wide")

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

companies = ["Lululemon", "Travelzoo", "Genius Sports", "Root Inc", "Karman Holdings"]


default_texts = {
   "Lululemon": """
**09/09/2025**

**LULUs recent decline of comparable store sales (shown by growth of -4% in Q2 of 2025) reflects its decline in consumer demand- despite its traditional strong hold in the sporting apparel industry. This showcases that the current share price of $205.57 is significantly overvalued, we therefore recommend a short on LULU, predicting a downside of 49.93 percentage points in 5 years if a bear case occurs.**

**Investment Thesis**  
LULUs central revenue streams mainly originate from US and Canada (approximately 70- 75 percent of total revenue is situated here); this ensures that revenue/ share price is dependent on mainly consumer demand from these countries; LULU share volatility mirrors the volatility of US consumer demand (Americas revenue growth was 3% falling short of the 19% international increase). As a result of a plateau of fitness activity interest since Covid-19 (due to lockdown locating everyone indoors, bringing greater focus to health and exercise), the growth tailwind achieved during the pandemic has stabilised. Mirroring this, consumer demand for sports apparel (which LULU provides) would also return to pre-pandemic levels from its current inflated value. This is showed by the comparable sales decreasing by 2% during Q1 2025, emphasising the case of declining US consumer demand. 

LULU also utilises a D2C business model through e-commerce like the “Like New” strategy (around 60% of revenue was collated through e-commerce and owned retail stores). However, because LULU lacks suitable wholesale partners (third parties that sell its products), it does not benefit from a wholesale cushion like some of its competitors. Competitors like Adidas can delegate excess inventory to partners like Footlocker, while LULU must bear the full brunt of this surplus through significant price markdowns and discounts. A lack of wholesale also ensures that reach to an international consumer base is lower due to a less diverse ecosystem; LULU has to expand through its owned stores without any third party assistance- increasing its advertisement and operating costs and reducing profitability (shown in the 50% decrease in share value during the initial quarters of 2025).

**Business Overview**  
LULU is a sporting apparel company that focuses upon brand loyalty through events (e.g. “Like New” resale programme) and product range from technology to streetwear. The company has an international presence with 767 stores and utilisation of e-commerce (its “Like New” scheme allows people from across the globe to buy/sell outdated apparel) to access an international consumer base. However recent financial performance shows an evident decline; during September 2025, it adjusted its EPS from 12.77 dollars to 12.97 dollars. This inflated the PEG ratio alluding to signs of overvaluation of the stock price; this is due to lower expected growth (maybe mirroring the fall in US consumer sports apparel demand).

**Catalysts**  
One of the main catalysts of LULUs stock price depreciation would be added costs (of 200 million dollars) from the removal of the US de minimis exemption; this ensures that imports under $800 million must bear the full weight of tariffs which significantly affects LULU. LULU is extremely dependent on imports. Its dependence on shipments from Vietnam and China (which manufacture 40% of apparel, and 28% of fabrics respectively) leads to these tariffs becoming a  long- term cost (as LULU it would be too complex to switch from outsourcing to domestic development). Cost-push inflation through tariffs would ensure that consumers have less disposable income to spend on luxuries such as LULU apparel and tend to focus upon necessities. LULU has traditionally attempted to offset inflation by manipulating prices (such as with Align leggings from 98 to 118 dollars), but increasing elasticity of LULU could result in lower consumer interest/ demand(as customers trade down to over brands such as Under Armour) and reduce profitability (gross profit was estimated to fall by 240 million dollars, catalysed by tariff activity).

Competitors in this oligopolistic market also constantly compete for LULUs consumer base; this is performed through simple pricing strategy. LULU has a price range of 45 to 68 dollars for its standard tops. NKE releases similar products at 25 to 40 dollars, this is around a 42% pricing advantage NKE has, allowing it to build a stronger market position through creating greater trust and affordability with its consumers. In cases of inflation (US inflation has increased annual by 2.7% in July 2025) consumers have lower purchasing power and so would choose cheaper alternatives over LULU, potentially even seeing its products as an ostentatious good due to its higher price margin. The BEA noted that personal consumption on apparel has a YoY 1.5% fall in Q2 2025, emphasising consumer caution with luxury on a tighter budget. The target audience of LULU products is also those who are younger (such as students on a budget) who do not have large cash reserves and prefer cheaper alternatives (that could be advertised through media such as TikTok Shop). This could lead to excess stock and force LULU to lower price (e.g., 60 percent discount on Define jackets) far below market price which would not benefit its revenue growth or profitability.

**Valuation**  
Using a DCF model, we forecasted that in the bear case LULU share price would fall to 102.92 dollars (a downside of 49.93 percent). The calculated WACC of 6.19% was utilised to reach a terminal value of 1.3026 billion, leading to the calculation of an enterprise value of 12.439 billion and an equity value of 12.334 billion. In the base case, LULU continues to focus upon its D2C e-commerce platform (contributing to the high gross margins of 5.5%) and analyses consumer preferences and data which to allow for LULU to innovate and develop products tailored to specific regions of people (and expand internationally). This could increase free cash lows and lower the WACC to 4 percent, providing a new share price of 208.71, an upside of 1.5%. Trading comps valuation was also conducted, assuming a base case EV/Revenue multiple of 1.87 times; EV/revenue was deemed a suitable indicator due to LULUs D2C  business model that focuses upon heavy reinvestment .The implied enterprise value was calculated at 20.3 billion and implied equity value was 19.7 billion- helping to discover the implied share price of 162.58 dollars, a downside of 20.9 percent in the base case (emphasising the need to short).

**Risks**  
One of the main risks when considering a short on LULU is underestimating LULUs brand image and consumer loyalty as it is a luxurious good (in comparison to its competitors); LULU can benefit from monopoly power and raise the price of products without a detrimental fall in its profit margins. This ensures that LULU is likely to thrive in the sports apparel market in the case of inflationary pressures or a black swan event that mitigates consumer spending. LULU has also focused on growth through an M&A; in 2020, LULU acquired MIRROR (a home fitness company) for 500 million dollars. This allows LULU to expand its ecosystem which directly translates into increased revenue (through a subscription-based model) by providing digital utility to customers (as they take exercise classes from home) which further strengthens LULUs D2C model

LULU would struggle to compete with other firms (despite its brand) image due to the lack of wholesale buffer of surplus stock which ensures that LULU has to face the full brunt of costs through discount schemes. This outweighs the benefit gained from an M&A scheme (that would not have as much advertising benefit as third party wholesalers) which only saw minimal revenue of around 80 million dollars

**Sources**

Lululemon 2024 Annual Report

Modern Retail, 2025

Reuters, 2025

**Written by: Chrishan Kanagalingam** 

**Edited by: Chrishan Kanagalingam**

""", 
    "Travelzoo": """
**04/09/2025**

**TZOO is a capitaliser of a niche sector of the internet industry, with a focus upon capitalising the brand loyalty of its 30 million concurrent customers. Due to the undervaluing of TZOO stock (mainly due to its concentration upon curated deals), we propose a long on TZOO with a 5-year base case target share price of $19.21, predicting a potential upside of 102% by 2030.**

**Investment Thesis**  
Buying shares would be profitable through long term investment in the micro-cap industry that includes smaller startups that tend to operate at a loss to reinvest (explaining the low EBITDA of 6.75% in 2025 despite a constant sticky recurrent revenue stream. Potential for this industry is rare, yet TZOO seems to be the exception by agglomerating profit margins between 83-92% which its larger counterparts (e.g. Booking.com) are yet to acclaim. The bull case being that undervalued entities with a smaller foundation have a potential for exponential growth in profitability/stock price given a suitable catalyst/ investment, especially for companies generating recurring profit when focus should tend towards reinvestment for dynamic efficiency. 

 Debt has also faced a constant decrease (down by 7% since the previous quarter) contributing to its recent net cash positive in 2025; its debt can be covered with its cash surplus which is unique for a company of its size. Net debt to EBITDA ratio in June 2024 was -0.32, which is considerably more liquid than its counterparts (averaging +0.72), showcasing its cash surplus. In the case of a black-swan event or rising interest rates, TZOO cash flow is more likely to be stable than its competitors; the strength of its balance sheet could position TZOO as an option of a M&A candidate.

 The case of a post-pandemic holiday/travel tailwind mirrors the demand for sites like TZOO, especially as COVID-19 led the agglomeration of online consumer culture- highlighting the importance of services concentrated on retaining consumer loyalty in the competitive online space. A second tailwind follows a necessity of curated experiences/services in addition to a bargain price. This is driven by increasing inflation (2.7% in the last 12 months) leading the need of exclusive deals at a cheap price through sites such as TZOO. The 2024 hybrid model (including advertisement and subscriptions) generates recurring revenue through converting consumers into paying members. Partners (such as hotels) offer TZOO a portion of income when booking offers are selected; 95% of members pay a premium to access deals (such as early-access offers). Multiple revenue streams created through elevated travel demand allows TZOO to gain a gross margin of around 85%.

**Business Overview**  
TZOO is a small-scale global travel/ media enterprise that offers curated deals to consumers. Deals are distributed mainly through its email newsletter (generating 30 million monthly subscriptions) in addition to alternate sources of social media. Acquiring a 60% stake in Jack’s Flight Club (JFC) allows for recurring revenue through its hybrid model using subscription-based flight deals. The quantity of TZOOs premium members has a yearly growth of around 15%, adding to its subscription led growth.

**Catalysts**  
The main catalyst of TZOOs expected return on investment is its shift to a paid subscription; membership revenues jumped 118% to 2.4 million in the first quarter of 2025 emphasising its stable high margin recurring revenue stream. The start of the subscription premium in 2024 saw a gross profit of 38 million after 6 months ended, showcasing a 102% increase from the previous 3 months ended data. Expansion of this strategy can increase revenue through premiums as well as payments from advertising. Growth can expand worldwide outside of the US to countries in Europe where there has been an increase in travel-deal related consumer culture online. TZOO could utilise its cash surplus to reinvest into AI to improve efficiency and gain economies of scale leading to a streamlined production process (e.g. through AI recommendations or chatbots).

As TZOO is a relatively small platform that has a well-established niche with loyal consumers, it could become the target of merger & acquisition opportunities from larger firms in the market (such as TripAdvisor). TZOO has a smaller market capitalisation of around 100 million which is affordable to larger giants in the industry. Acquirers could utilise their cash reserves to invest in software to increase technological economies of scale and improve user-engagement which would lead to favourable profit margins and a spike in the price of shares. This ensures that the share price of TZOO is currently undervalued and on a sale for potential investors due to TZOO focusing upon a new hybrid business model (explaining the fall in share price and EBITDA compared to its previous values of 2024).

**Valuation**  
Despite the current dip in share price, there should be a recovery back to 2024 levels- potentially surpassing this in a 5-year window (shown by the upside of 102%). We utilised the DCF model for this to represent TZOOs potential in recurring revenue streams and generating cashflow; data was also mainly collated from 2024 as the current share price of 9.46 is only temporary due to TZOOs focus on reinvestment into the new hybrid business model. The DCF base case suggests that there would be a post 5-year share value of $19.21 assuming there is a 12.08x multiple; the enterprise value was calculated to be 208 million dollars and the equity value was 213 million. We got to these figures through the new terminal value of 174.9 and new free cash flow of 5.5 million. The bull case would lower WACC to 7.5% due to improved investor security if WACC integrates methods such as AI to increase subscription revenue leading to a potential upside of 159%.

**Risks**  
Risks include a lag in profitability from slow expansion of the premium membership model- ensuring that share price may continue to decline in the bear case. The market is also overcrowded with competitors with a larger market share that could utilise competitive pricing (e.g. predatory pricing) on their own subscriptions to gain customers over TZOO. Constant reinvestment into the hybrid business model also puts profitability at risk in the short term; profitability is further affected by travel being dependent on consumer confidence that could deteriorate due to government policies or economic shocks.

TZOOs focus on curated consumer culture mitigates the probability of the risks through creating brand loyalty and generating a recurring revenue stream. This allows for its cash surplus that can be used for further reinvestment internationally for either profitability or surviving an economic shock.

**Sources**  
Tipranks, 2025  

Yahoo Finance, 2025

Travelzoo, 10-K Balance Sheet

**Written by: Chrishan Kanagalingam**   

**Edited By: Johan Sebastian**

**Appendix**
""",
    "Genius Sports": """

**02/09/2025**

**GENI focuses upon business partnerships (through exclusive data agreements with leagues like the NFL) to build defensible moats that aid it to prosper through revenue-led growth. We suspect that GENI is heavily undervalued at $12.77 and propose a long on GENI, predicting a post 5-year upside of 91.31% in the base case.**

**Investment Thesis**  
Investor interest in GENI extends to the fact that its business strategy allows it to have a greater competitive positioning in the market; its partnerships include the NFL (through to 2030) and Serie A (to 2029) for data distribution. Legally, this holds GENI in a higher position through structural barriers to entry as competitors do not benefit from the same exclusive access, as GENI benefits from a regulatory moat. GENIs framework allows for effective revenue and EBITDA growth (20% and 188% in Q1 of 2025 respectively) potentially allowing it to have cash reserves surpassing $135 million, allowing for potential reinvestment into connections with further leagues and broadcasters and strengthening its monopoly power. Partners that are already recognised are also dependent on GENI and reluctant to switch to its competitors due to the dependency services; switching would require high technical costs through the process of removing software and discovering new contract partners.

The sports betting tailwind also increases the desirability of this industry- in the US, sports betting has been expected to grow around 11% CAGR by 2030. GENI participates in in-play/ live gambling, which has gained the most recent traction by mirroring the growth of global media/entertainment. However, GENI has also effectively diversified its market through vertical diversification. In 2021, GENI acquired FAN Hub, providing games (e.g. Trivia) to allow fans of leagues to be further entertained; fan data can also be utilised to help with the advertisement of its league partners. GENI has diversified into the advertisement space through creating loyalty with both partners (by providing advertisement), and users (through enhancing features aside from betting).

 Diversified revenue streams (through leagues, broadcasters, advertisers and users) allow GENI to create a sticky ecosystem to generate further revenue. This enhances its cash surplus (cash flow increased by 5.5x in 2024) and strengthens its balance sheet allowing it to chase a M&A opportunity due to its cash reserves and the stability of its income. A 100 million Share Repurchase was announced to reduce the number of outstanding shares; this enhances the value of remaining shares, benefitting the EPS and shareholder stake, while already in a cash surplus. The showcase of confidence in the firm’s financial stability also makes GENI a target for investors.

**Business Overview**  
GENI is a UK company in the sports betting data industry, operating through partnerships with numerous organisations (following a B2B model). The international sticky ecosystem expands to various countries in North America and Europe through its partnerships through leagues like the NFL and EPL. GENIs geographical diversification and regulatory moats (through exclusive contracts) has contributed to its Q2 2025 revenue of 118 million, a 24% upside of the figure from last year.

**Catalysts**  
One of the main catalysts for GENI would be the expansion of its sticky ecosystem business model, focused upon diversification into advertising through partnerships with companies like PMG to maximise attention from sports fans. This would further maximise its margin expansion (Q2 data shows a YoY increase in EBITDA of 64%, margin +700) and expand its cash reserves- allowing for a M&A strategy through vertical diversification into fan-based platforms (like FAN Hub) and pursue partnerships with more niche emerging sports/ markets such as regional/ national leagues. Expansion of the partnership’s ecosystem allows for cross-selling through exclusive bundles to increase customer utility and increase overall revenue.

GENIs enhanced position to reinvest due to its large free cash flow (which we calculated at 103.33 million for 2024) and cash reserves also serves as a suitable catalyst. Live betting is the fastest growing sector of this industry (estimated to capture around 50% of the total market by 2030); expansion could be met through reinvestment to amplify live betting experience (such as FAN Hub features like prediction games) and shifting focus towards the D2C model, following the growth of this sector.  Many countries (such as Brazil) legalising sports betting also provides a second tail wind for growth due to access to a larger consumer market, which is beneficial for GENI due to its pre-established trust and position of reliability (by being the partner of major leagues such as the NFL).

**Valuation**  
Using a DCF model, we calculated that the post 5-year base case share value would be 24.43 dollars. Using a WACC of 14.76 percent in the base case scenario, the calculated enterprise value was 5.81 billion and equity value was 5.82 billion (as the terminal value was 1.0879 billion). In the bull case, GENI faces exponential growth through diversification (via new partners, countries and revenue streams), enhancing cash reserves and lowering equity risk premium and cost of equity. The WACC would decrease to 10.5 percent and the EBITDA would strengthen to 150 million- ensuring there is a new share price of 33.50 dollars, an upside 147 percent. In the bull case, trading comps valuation analysis dictates an EV/Revenue multiple of 15.70 times (chosen as GENI has high revenue growth of 26 percent but is not profitable with margins of -13.96 percent), leading to: an implied enterprise value of 8 billion, an implied equity value of 8.22 billion and an implied share price of 34.5 dollars. In the bear case (perhaps due to improper reinvestment to focus on a D2C business model or stricter regulations upon gambling in countries in Europe) the multiple is 2.9 times, resulting in: an implied enterprise value of 148 million, an implied equity value of 168 million and an implied share price of 7 dollars (downside of -45.18 percent).

**Risks**  
One of the key risks of GENI investment is that it is a heavily regulated industry and laws upon betting could increase and be more severe over time, limiting GENIs operating capability and profitability. It is also a highly concentrated market, and its counterparts could implement new strategies (such as development of prediction games for sports matches to enhance consumer retention) to create defensible moats and reduce the market power of GENI. There is also the case that GENI is not yet consistently profitable (2025 profit margins being -13.96%), this means its stock is volatile and could lead to quarterly earnings misses which could eventually lead to lower investment confidence and lower EV/EBITDA multiples.

Although, defensible moat strategies built through partnerships with major leagues (such as the NFL) allows GENI to expand its revenue streams and stabilise its income. Its large cash reserves can be utilised to diversify into sectors outside of betting (such as advertisement of leagues) to create financial security.

**Sources**  
Genius Sports Limited, 10k Balnce Sheet

Stock Analysis Genius Sports (GENI) Cash Flow, 2025

**Written by: Chrishan Kanagalingam**

**Edited by: Chrishan Kanagalingam**

**Appendix**
""",
    "Root Inc": """ 
**31/08/2025**

**Root Inc is an auto insurance company that experienced significant growth in 2024 and 2025 (Q4 2024 showed an EPS of 1.42 dollars and revenue growth of 68 percentage points). We predict that at the current growth, the share price will continue to increase from $100.21 and propose a long on Root Inc due to a potential 5-year upside of 32% in the base case.**

**Investment Thesis**  
Root Inc showcased strong financial Q1 performance in 2025, with revenues of 349.4 million dollars that exceeded the forecasted 303.9 million dollars. It turned around the net loss of 7.8 million dollars that was shown in last year’s income statement and has been profitable for consecutive quarters. The Q1 EPS was 1.07 dollars. Compared to the forecasted 0.17, there was a 529 percent upside; Q1 revenue was also higher at 349.4 million dollars compared to the anticipated 303.9 million. The reason for this could be strong partnerships and collaborations with companies such as Experian, helping Root Inc to cover 77% of the US as its consumer base. Impressive revenue growth of 159% in last twelve months could be amounted down to its partnership channel led growth, accounting for 33% of new writings in Q1 2025.

Although post Q1 stock performance has dropped by around 40%, it does not take away from Root Incs potential for revenue-led growth through the diversification of its partnership model. Through expanding its insurance products and focusing on expanding to a younger audience through the digital-first channel (where consumers can avoid the interference of brokers and handle insurance activity online), Root Inc has benefited from positive profit margins. The Customer Acquisition Cost would also be lower than the market (due to the cost-effective method of utilizing digital data to reduce underwriting risk)- leading to customers being paid back at a faster rate. This contributed to its net combined ratio of 95% in 2025, enhancing profitability. Key indicators of the relevancy of Q1 data come from Megan Binkley (CFO) who stated it is advantageous to recognize the benefit from the upwards trend in Q1 as there is less automotive activity in winter compared to the Q1 season. The losses expected after Q1 are short term due to Q2 being a stormy season; the losses align and are taken in account with  a target between 60-65 percent in the bear case. This fall can be mitigated through CEO Alex Timm’s long-term focus outside Q3, showing potential of a bullish stock insight.

**Business Overview**  
Root Inc is a D2C automotive insurance company that utilises telematics data to give prices tailored towards the consumer based on their driving behaviors. In its centre lies its mobile app that removes the need for complicated procedures through brokers and ensures a lower CAC. It is typical of most automotive models to reward dangerous drivers by focusing on factors such as age to allocate premiums; Root Incs utilisation of AI for underwriting insurance policies focuses on actual behaviour rather than these metrics.

**Catalysts**  
Root Incs focus on its partnership strategy could catalyse revenue growth and increase share value from $100. Alex Timm stated that the total number of partners exceeds 20 and in Q2 of 2025 embedded partnerships took a percentage of 44% of new policies. Root Incs partnership with Hyundai Capital America allowed for integration into Hyundais business model through embedded insurance (those that buy a Hyundai vehicle are offered insurance through Root Inc). Association with Hyundai can also create customer loyalty through trust, as Hyundai is another established organization; Hyundai also provides data to Root Inc allowing it to improve its risk assessment and be more efficient. Increased efficiency leads to lower costs and greater profitability and may allow Root Inc to reinvest through an M&A scheme (such as taking over an AI company to help with underwriting).

Another catalyst could be its potential for geographical expansion. Root Inc is currently active in 35 US states (77% coverage) with over 414,000 policies and has filed for approval in states such as Michigan which could widen its reach by potentially millions of drivers. This allows Root Inc to increase the number of policies and increase its GPW (gross premiums written- which is up 66% YoY) and allows Root Inc to expand to a new consumer base of drivers. Increased premium growth allows for Root Inc to gain greater economies of scale and negotiating power with reinsurers or potential partners (that could be accessed through geographical expansion), allowing for a greater potential EBITDA and profitability. 

**Valuation**  
For the valuation, we conducted a DCF model, predicting a new share price (in the base case) of $132 by 2030, assuming an EV/EBITDA multiple of 15.2 times. Using a WACC of 6.61%, the enterprise value was calculated at 1.586 billion dollars and the equity value was 2.032 billion . In the bull case (from successful geographical expansion and access to a new base of partners leading to greater market share and technical economies of scale through reinvestment in new AI software) the WACC falls to 5.2% due to a lower equity premium and ensures there is a new share price of 249 dollars (this showcases a 149% upside).

**Risks**  
One potential risk of Root Inc is tariffs, increasing loss ratio by affecting customer affordability of insurance (in the bear case). Tariffs could increase vehicle financing costs as well as car prices, which could reduce the number of drivers; partners could be affected if sales are affected, ensuring that the effectiveness of embedded insurance decreases. Seasonal factors (Q1 sees most growth due to winter season, Q2 is heavy convective storm season and then Q3 is hurricane season) also allows for volatile performance/ profitability by ensuring that Root Inc always has periods where losses must be faced. Also, requirement for regulatory approvals could cause time delay for expansion plans; insurance is heavily regulated in the US and could affect geographical expansion, preventing the bull case. Small-cap stocks are deemed volatile (a 40% stock price dip occurred in Q1) with a beta value of 2.41 in Q1, which may tarnish investor confidence resulting in downturns 

Root Inc, however, differentiates from other automotive insurance companies through digital first experience (through its central app) and uses embedded partnerships to diversify its revenue streams and build reliability and trust. This is done through constant regulatory engagement (e.g. through constant checks) and strong liquid cash position.

**Sources**

finance.yahoo, 2025

Root Inc 10-K Balance Sheet

ideausher.com, 2025

trading view.com, 2025

investor.wedbush.com, 2025

**Written by: Arman Nahas**

**Edited by: Chrishan Kanagalingam**

**Appendix**
""",
    "Karman Holdings": """
**27/08/2025**

**KRMNs share price sits at 62.22 dollars, which we interpret to be undervalued due to recent financial performance generating a net income of 6.81 million in June 2025, a YOY increase of 47.85%. Net profit margins also show an impressive growth of 9.24 percent and so we recommend a long on KRMN, calculating that post 5-year share value will increase to 135 dollars (an upside of 117.97 percentage points).**

**Investment Thesis**  
KRMNs position as a pure-play, mid-cap organisation allows it to focus directly upon areas that would achieve explosive revenue growth. It operates in three primary crucial defence areas: Hypersonics, Space Launch and Missile Defence Systems; these areas are critical to the US Department of Defence (DOD) and allows for positive revenue margins (2025 revenue growth was recorded at around 30 percent). Increasing DOD involvement has led to the funded backlog revenue of $719.3 million and prospered a tailwind for revenue growth (back log had a 36 percent upside in final year of 2024). In Q2, Missile Defence generated an approximate 40.5 million dollars (a rough elevation of 46%); its strategic vitality in KRMNs portfolio can be accounted to mission-critical systems (including complicated components like aerodynamic stability) which are valued for contractors such as Lockheed. The US boasts the highest market share in the global space launch industry (that has a projected 5-year growth of 8-10 percent CAGR). KRMN specialises in key components to make it a trusted supplier for DOD and so could benefit from spillover effects from the industry (increasing EBITDA by +30%). 

The KRMN NGI project can exponentially increase its share value through the replacement of ground-based interceptors in the GMD system; this program is budgeted at tens of billions of dollars over the next ten decades. Such a profitable industry could lead to greater revenue streams (contributing to the total revenue of 115.1 million (around 35.3% growth increase YoY); this can be used for a M&A strategy to diversify its involvement in the defence industry. One such acquisition was with ISP ($58.7 million) which develops the energetic propulsion energy sector through RATO systems and small rocket motors, potentially increasing EBITDA (through higher technical economies of scale and productive efficiency) from 106 million dollars to 141 million from 2024 to 2025 (margin of 33%).

**Business Overview**  
KRMN specialises in aerospace and defence and utilises its significance to the DOD as a supplier of highly engineered components. Initially, IPO raised $506 million, indicating that KRMNs growth potential had already been undervalued due to the valuation multiplying to 2.6 billion dollars in 2025. In comparison to its peers, the IBD Composite Rating was 97 out of 99 ensuring that recent stock performance is superior to almost all stocks in the US.

**Catalysts**  
One of the main catalysts for a rise in KRMN share value is continued expansion of its partnerships network. Currently, it is involved with 70 contractors and 100 missile/space partners; one key collaboration was with ULA (a Boeing and Lockheed Martin joint venture) which helped to further establish KRMNs involvements in aerospace (particularly in launch vehicles such as the Vulcan Centaur). KRMN had the role to supply highly valued/complex components for rocket boosters (GEM 63L) and this partnership helped raise its business statement and potential consumer base as KRMN can become more trusted for further partnerships. This can further increase revenue (2025 saw a record revenue count of 115 million dollars and a 233 percent increase in the EPS from the previous year). Such financial projection can affect investors and analyst ratings which can further influence share price; Raymond James had listed KRMN as a strong buy (targeting a price of $100) which led to the stock price increasing by 17.1% on the same day.

**Valuation**  
For our valuation, we conducted a DCF model using excel. Assuming an EV/EBITDA multiple of 75.90x , the high assumption can be accounted to KRMNs positive investor speculation as aerospace stock trade at story multiples, emphasised by its IPO expectations. Through the CAPM, we calculated the cost of equity of 15.88% which was utilised to estimate the WACC of 8.52% and a terminal value of 26.2 billion dollars. The enterprise value was calculated to be 17.92 billion dollars, with the equity value being 17.87 billion dollars. The final new share price was $135 in the bull scenario, upside of 117.97 percent. In the base case, the WACC would be 8.7% due to an increase in the cost of equity to 16.32%. This may be due to beta increasing, ensuring that KRMN stock price is more volatile due to failed contracts or distrust within partners- leading to a fall in investment confidence. This would lead to a bull case share price of 92.84, upside of 49%.

**Risks**  
KRMN has many risks for affecting the stability of the value of its shares. Primarily, it formulates a business model around dependency upon US government prime contracts (such as Northrup Grumman). Federal defence budgets fluctuate based upon geo-political circumstances (such as preparation for a war); if Congress decides to reduce Hypersonic funding in a given fiscal year (perhaps due to insufficient components received from KRMN), KRMN may experience slow growth or delayed cash flow; changes in US policy can influence which programs are prioritised and competitors of KMRN may be chosen in its stead, considerably damaging profit margins. For investors, heavy focus on a singular customer segment (due to its pure-pay model and avoidance of diversification) increases exposure to policy budgeting and strategic shifts, meaning earnings are volatile which increases the risk of quarterly revenue fluctuations. Strategic failures (as well as operational failures leading to increased distrust from partners) can also persist. For example, the acquisition of a company (such as ISP) may not go smoothly due to a lack of synergies- initiating falling productive efficiency. More commonly, manufacturing errors may occur as KRMN relies on precise and complex assembly processes which could result in failure due to material shortages or delays.

However, KRMN undergoes various safety procedures (such as the ISO 8 clean room standards emphasising the requirement of ideal conditions for assembly) to avoid any practical mistakes. This ensures that KRMN can continue to gain partnerships through its brand status built upon the trust of its competency leading to further investor anticipation (due to positive profit margins) and a rise in the share price- hence the recommendation of a long on KRMN.

**Sources**

Karman Space and Defence, 2025

Reuters, 2025

Karman Holdings 10-K Balance Sheet

**Written by: Chrishan Kanagalingam, Kobith Kanagalingam**

**Edited by: Patrick Maynard**
""",
    "About": """

    """,
    "Privacy Policy": """
**Last updated: 8 September 2025**

We at Mini-Pitch, consider your privacy to be something of the utmost importance. The details listed down below note how we: collect, use, store, and protect information when you use our website. As transparency is core to our key values, the details of what we do not collect and the measures we take to ensure your data remains safe is also noted below.
By using our website, you agree to the terms of this Privacy Policy.

**1. Policy Purpose**
Our Privacy Policy is designed to:
Provide clear clarity on the data we collect (as well as data that we dont),
Explain how temporary data is dealt with during your session on the site,
Outline your rights as a user under applicable privacy laws,
Demonstrate our commitment to privacy, transparency, and responsible data practices.

**2. Information We Collect**
We strive to minimise the collection of your data as best we possibly can. Currently, Mini-Pitch does not collect personally identifiable information (PII) (your name, email address, phone number, payment details, or location).
Specifically:
There is no need to register or create an account.
No personal identifiers are stored in our databases.
No marketing or tracking data is recorded.
Only the minimal data necessary to maintain the technical/working function of the site is temporarily processed.

**3. Use of Session Data**
To provide a smooth browsing experience, we use Streamlit session state, which is stored temporarily in your browser’s memory. This allows us to:
Remember your current navigation state when you view a specific stock pitch,
Preserve selections as you move between the content of the website,
Enable interactive features without requiring personal data.
Key facts about session data:
It is not stored in cookies.
It is not shared with third parties.
It automatically disappears when you close or refresh the page.

**4. Technical Logs**
Our hosting provider may automatically collect limited technical information, such as error logs or performance metrics, in order to maintain website stability. However:
These logs do not contain personal and identifiable information,
They are used solely for troubleshooting or security monitoring,
They are automatically deleted after a short retention period.
We do not use technical logs to track or profile users.

**5. Use of Cookies and Trackers**
Mini-Pitch does not use:
Browser cookies,
Local storage,
Tracking pixels,
Third-party analytics or advertising networks.
Your activity is not tracked during your site session.

**6. Third-Party Services**
We do not integrate with external services that would collect user data, such as: Google Analytics, Meta (Facebook) Pixel, or advertising platforms.
Should third-party tools ever be introduced in the future (for example, academic analytics to track site usage volume), this Privacy Policy will be updated and any legally required consent will be obtained.

**7. Children’s Privacy**
Mini-Pitch is intended for use by students, researchers, and individuals interested in equity research. It is not directed toward children under 13 years of age (or the equivalent minimum age in other jurisdictions).
Since we do not collect personal data, we do not knowingly collect information from children. If you believe a child has provided information through this platform, please contact us immediately.

**8. Data Retention**
Because we do not collect or store personal information:
No user data is retained beyond the session,
No databases of personal data exist,
Any generated files are deleted once your browser session ends.
This ensures your complete privacy.

**9. Security Measures**
Even though we do not store personal data, we implement the appropriate safeguards to protect the website, including:
Secure hosting infrastructure,
Encrypted communication (HTTPS),
Regular updates and monitoring of dependencies,
Minimal attack surface by avoiding unnecessary data collection.

**10. Your Rights**
Although we do not collect personal information, we recognise your general privacy rights under laws such as GDPR (EU) and CCPA (California). These rights may include:
The right to transparency,
The right to be informed,
The right to privacy and non-tracking.
If our practices change in the future, we will implement the necessary mechanisms to allow you to exercise data access, rectification, and deletion rights.

**11. Policy Updates**
We may revise this Privacy Policy in the future to mirror:
Legal or regulatory changes,
Introduction of new features or services,
Adoption of third-party tools (with consent if required).
All updates will be posted on this page with a revised “Last updated” date.

**12. Contact Us**
If you have questions or concerns about this Privacy Policy or our stock pitches, please reach out to us at chrishan@mini-pitch.co.uk.
 """
}

valuation_images = {
    "Lululemon": ["Images/Google/valuation3/LULU.png", "Images/Google/valuation3/LULU1.png"],
    "Travelzoo": ["Images/Apple/valuation/TZOO.png"],
    "Genius Sports": ["Images/Microsoft/valuation1/GENIa.png", "Images/Microsoft/valuation1/GENIb.png"],
    "Root Inc": ["Images/Amazon/valuation2/RootInc.png"],   
    "Karman Holdings": ["Images/Tesla/valuation4/KRMN.png"]
}

end_images = {
    "Lululemon": ["Images/Google/end3/LULUa.png", "Images/Google/end3/LULUb.png", "Images/Google/end3/LULUc.png"],
    "Travelzoo": ["Images/Apple/end/TZOOa.png", "Images/Apple/end/TZOOb.png", "Images/Apple/end/TZOOc.png", "Images/Apple/end/TZOOd.png", "Images/Apple/end/TZOOe.png"],
    "Genius Sports": ["Images/Microsoft/end1/GENIc.png", "Images/Microsoft/end1/GENId.png", "Images/Microsoft/end1/GENIe.png", "Images/Microsoft/end1/GENIf.png"],
    "Root Inc": ["Images/Amazon/end2/RootInca.png", "Images/Amazon/end2/RootIncb.png", "Images/Amazon/end2/RootIncc.png"],   # replace with real paths
    "Karman Holdings": ["Images/Tesla/end4/KRMNa.png", "Images/Tesla/end4/KRMNb.png", "Images/Tesla/end4/KRMNc.png", "Images/Tesla/end4/KRMNd.png"]
}

def menu():
    st.markdown("## Menu", unsafe_allow_html=True)
    current_page = st.session_state.get("page", "Home")
    page_selection = current_page

   
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] { background-color: #111111; color: white; }
        [data-testid="stSidebar"] > div:first-child { max-height: 90vh; overflow-y: auto; padding-right: 4px; }
        .streamlit-expanderHeader { color: white; font-weight: bold; }
        .streamlit-expanderHeader svg { fill: white !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    def menu_item(label):
        nonlocal page_selection
        active = (current_page == label)
        if st.button(label, key=f"btn_{label}"):
            page_selection = label

        st.markdown(
            f"""
            <style>
            div[data-testid="stButton"][key="btn_{label}"] button {{
                width: 100% !important;
                text-align: left !important;
                background-color: {'#333333' if active else '#222222'} !important;
                color: white !important;
                border-radius: 8px !important;
                border: none !important;
                font-weight: bold !important;
                padding: 10px 16px !important;
                font-size: 16px !important;
                margin: 0px !important;
            }}
            div[data-testid="stButton"][key="btn_{label}"] button[data-testid="baseButton-secondary"]:hover {{
                background-color: #000000 !important;
                color: white !important;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )

    menu_item("Home")


    with st.expander("Stock Pitches", expanded=current_page in companies):
        for pitch in companies:
            menu_item(pitch)

  
    menu_item("About")
    menu_item("Privacy Policy")

    if page_selection != st.session_state.get("page", "Home"):
        st.session_state["page"] = page_selection
        st.rerun()

    return page_selection

def render_page(page):
    if page == "Home":
        st.markdown('<h1 style="color: #40E0D0; font-size:110px;">Mini-Pitch </h1>', unsafe_allow_html=True)
        st.markdown("""
        <h1 style="font-size:40px;">
        Trading<b><i><span 
        style="color:#40E0D0"> Knowledge</span></i></b> into <b><i><span style="color:#40E0D0">Profit</span></i></b>
        </h1>
        """, unsafe_allow_html=True)
        st.markdown("""
        <h1 style="font-size:25px;">
        Pitches that encourage students to:<b><i><span 
        style="color:#40E0D0"> take interest, trade & invest</span></i></b>
        </h1>
        """, unsafe_allow_html=True)
        return

    elif page == "About":
        st.title(page)
        st.markdown('<h1 style="font-size:17px;"> At Mini-Pitch, we aspire to encourage student participation regarding financial interest; our online platform provides a window for students to pitch ideas (reinforced through calculations and relevant research) to others and trade financial insight. This allows avenues to gain increased financial literacy, no matter whether you are a: reader, writer or investor. At Mini-Pitch, we utilise a combination of financial modelling to valuate our pitches, including: Discounted Cash Flow (DCF), Trading Comps Valuation and Capital Asset Pricing (CAPM). This helps us to showcase a hopefully greater reliability with our pitches when offering our recommendations. For any enquiries regarding our pitches (or posting your stock pitches on our page), contact us at chrishan@mini-pitch.co.uk</h1>', unsafe_allow_html=True)
        st.markdown('<h1 style="font-size:45px;">Our Team</h1>', unsafe_allow_html=True)
        st.markdown(f"""
        <h1 style="font-size:20px;">
        Founder/CEO<b><i><span style="color: #40E0D0"> - Chrishan Kanagalingam</span></i></b>
        </h1>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <h1 style="font-size:20px;">
        Co-Editorial Chiefs<b><i><span style="color: #40E0D0"> - Johan Sebastian, Patrick Maynard</span></i></b>
        </h1>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <h1 style="font-size:20px;">
        Co-Developers<b><i><span style="color: #40E0D0"> - Chukwunonso Onyilo, Chrishan Kanagalingam, Prathish Jathesenaikabahu</span></i></b>
        </h1>
        """, unsafe_allow_html=True)

        return


    elif page in ["Privacy Policy"]:
        st.title(page)
        st.markdown(default_texts.get(page, ""), unsafe_allow_html=True)
        return

    stock_page = page
    st.title(f"{stock_page} Stock Pitch")
    text = default_texts.get(stock_page, "")

    if stock_page in valuation_images and "**Valuation**" in text:
        before, after = text.split("**Valuation**", 1)
        st.markdown(before, unsafe_allow_html=True)
        st.markdown("**Valuation**<br>", unsafe_allow_html=True)

        for img in valuation_images[stock_page]:
            if os.path.exists(img):
                st.image(img, width=1000)
                st.markdown("<br>", unsafe_allow_html=True)
            else:
                st.warning(f"Valuation image not found: {img}")

        st.markdown(after, unsafe_allow_html=True)
    else:
        st.markdown(text, unsafe_allow_html=True)

    if stock_page in end_images:    
        for img in end_images[stock_page]:
            if os.path.exists(img):
                st.image(img, width=1000)
                st.markdown("<br>", unsafe_allow_html=True)
            else:
                st.warning(f"End image not found: {img}")

              
with st.sidebar:
    current_page = menu()
render_page(current_page)
