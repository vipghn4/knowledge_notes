<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [DJIA index](#djia-index)
  - [DJIA index](#djia-index-1)
  - [Historical milestones](#historical-milestones)
  - [Black Monday](#black-monday)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# DJIA index
## DJIA index
**Blue chip**. A nationally recognized, well-established, and financially sound company
* *Characteristics*. 
    * Blue chips generally sell high-quality, widely accepted products and services
    * Blue-chip companies are known to weather downturns and operate profitably in the face of adverse economic conditions
        
        $\to$ This helps to contribute to their long record of stable and reliable growth

**Dow Jones industrial average (DJIA) or Dow 30**. A stock market index tracking 30 large, publicly-owned blue-chip companies trading on the NYSE and the Nasdaq
* *Purposes*. Designed to serve as a proxy for the health of the broader U.S. economy
    
    >**NOTE**. The DJIA is one of the most-watched stock market indexes in the world
    
    * *Companies considered in Dow*. All can be described as blue-chip companies with consistently stable earnings

**DJIA component companies**.
* *DJIA companies in 1896*. When the index initially launched in

    $\to$ It included only 12 companies
    * *Explain*. Those companies were primarily in the industrial sector, including the railroads, cotton, gas, sugar, tobacco, and oil
* *DJIA companies in early 20th century*. The performance of industrial companies was typically tied to the overall growth rate in the economy

    $\to$ This cemented the relationship between the Dow's performance and that of the overall economy
    
    >**NOTE**. For many investors, a strong-performing Dow equals a strong economy

* *Selection of DJIA companies*. As the economy changes over time, so does the composition of the index
    * A component of the Dow may be dropped when a company becomes less relevant to current trends of the economy
        
        $\to$ This component will be replaced by a new name that better reflects the shift
    * A company losing a large percentage of its market capitalization due to financial distress might be removed from the Dow
* *Weighting DJIA companies*. Stocks with higher share prices are given greater weight in the index

    $\to$ A higher percentage move in a higher-priced component will have a greater impact on the final calculated value

**Calculation of DJIA**. 
* *Initial formulation*. Charles Dow calculated the average by adding the prices of the twelve Dow component stocks and dividing by twelve
    
    $\to$ The end result was a simple average
    * *Drawback*. Over time, there have been additions and subtractions to the index, e.g. mergers, stock splits, etc.
    
        $\to$ A simple mean calculation no longer made sense
* *Dow Divisor and index calculation*.
    * *Dow divisor*. Created to address the simple average issue
        * *Formulation*. The divisor is a predetermined constant used to determine the effect of a one-point move in any of the stocks comprising the Dow
            
            >**NOTE**. There have been instances when the divisor needed to be changed so that the value of the Dow stayed consistent

    * *Calculation of Dow index*. The Dow reflects the sum of the price of one share of stock for all the components, divided by the divisor
    
        $\to$ A one-point move in any of the component stocks will move the index by an identical number of points

        ```sql
        DJIA Price = SUM(Component stock prices) / Dow Divisor
        ```

**Dow index components**. The Dow is often re-evaluated to replace companies that no longer meet the listing criteria with those that do

## Historical milestones
* *March 15, 1933*. The largest one-day percentage gain in the index happened during the 1930s bear market, totaling 15.34%
    
    $\to$ The Dow gained 8.26 points and closed at 62.10.10
* *Oct. 19, 1987*. The largest one-day percentage drop took place on Black Monday, i.e. the index fell 22.61%
    
    >**NOTE**. There was no evident explanation for the crash, although program trading may have been a contributing factor

* *Sept. 17, 2001*. The fourth-largest one-day point drop, and the largest at the time, took place the first day of trading following the 9/11 attacks in New York City
    
    $\to$ The Dow dropped 684.81 points or about 7.1%
    
    >**NOTE**. The index had been dropping before Sept. 11, losing more than 1,000 points between Jan. 2 and Sept. 10
    
    * *Recovery of DJIA index*. The DJIA started to make traction after the attacks and regained all of what it lost, closing above 10,000 for the year
* *May 3, 2013*. The Dow surpassed the 15,000 mark for the first time in history
* *Jan. 25, 2017*. The Dow closed above 20,000 points for the first time
* *Jan. 4, 2018*. The index closed at 25,075.13, the first close above 25,000 points
* *Jan. 17, 2018*. The Dow closed at 26,115.65, the first close above 26,000 points.16
* *Feb. 5, 2018*. The Dow fell a record 1,175.21 points
* *Dec. 26, 2018*. The Dow recorded its largest one-day point gain of 1,086.25
* *July 11, 2019*. The Dow broke above 27,000 for the first time in its history
* *Feb. 12, 2020*. The Dow hits its pre-pandemic high of 29,551.20
* *March 2020*. The Dow Jones crashes with back-to-back record down days amid the global coronavirus pandemic, breaking below 20,000 and falling 3,000 points in a single day amid several 2,000 and 1,500 up and down moves
    
    $\to$ It officially entered bear market territory on March 11, 2020, ending the longest bull market in history that began in March 2009
* *Nov. 16, 2020*. The Dow finally breaks its pre-COVID-19 high, reaching 29,950.44 points
* *Nov. 24, 2020*. The Dow breaks the 30,000 level for the first time, closing at 30,045.84
* *July 2021*. On July 12, 2021, the Dow trades above 35,000 for the first time ever
    
    $\to$ On July 23, 2021, it closes above 35,000 for the first time ever

**Investing on DJIA**. Individuals can invest in the Dow, i.e. gaining exposure to all of the companies listed in it

$\to$ This can be done through exchange-traded funds (ETFs), e.g. the SPDR Dow Jones Industrial Average ETF (DIA)

**Limitations of the DJIA**. 
* Many critics of the Dow argue that it does not significantly represent the state of the U.S. economy
    * *Explain*.
        * DJIA consists of only 30 large-cap U.S. companies
        * They believe the number of companies is too small and it neglects companies of different sizes
    * *Consequence*. Many critics believe the S&P 500 is a better representation of the economy as it includes significantly more companies, 500 versus 30
* Critics believe that factoring only the price of a stock in the calculation does not accurately reflect a company, as much as considering a company's market cap would
    * *Consequence*. A company with a higher stock price but a smaller market cap would have more weight than a company with a smaller stock price but a larger market cap, which would poorly reflect the true size of a company

## Black Monday
**Black Monday**. Occurred on Oct. 19, 1987, when the Dow Jones Industrial Average (DJIA) lost almost 22% in a single day

$\to$ The event marked the beginning of a global stock market decline

>**NOTE**. Black Monday is one of the most notorious days in financial history

* *Cause of problem*. Economists have attributed the crash to 
    * A combination of geopolitical events and
    * The advent of computerized program trading that accelerated the selloff

**Prevention of another Black Monday**.  Since Black Monday, a number of protective mechanisms have been built into the market to prevent panic selling
* *Increment of volatility*. High-frequency trading (HFT) algorithms driven by supercomputers move massive volume in just milliseconds
    
    $\to$ This increases volatility
* *Example*. The 2010 Flash Crash was the result of HFT gone awry, sending the stock market down 10% in a matter of minutes
    
    $\to$ This led to the installation of tighter price bands
    
    >**NOTE**. The stock market has experienced several volatile moments since 2010

**Lessons from Black Monday and other market crashes**. A market crash of any duration is temporary
* *Historical observations*. Many of the steepest market rallies have occurred immediately following a sudden crash
    
    $\to$ However, the market fully recovered and rallied in new or near new highs in the following months
*  *Stick with our strategy*. A well-conceived, long-term investment strategy based on personal investment objectives should provide the confidence for investors to remain steadfast while everyone else is panicking

    $\to$ Investors who lack a strategy tend to let their emotions guide their decision-making
* *Buying opportunities*. Knowing that market crashes are only temporary

    $\to$ These times should be considered an opportunity to buy stocks or funds
    * *Explain*. Market crashes are inevitable
    
        $\to$ Savvy investors have a shopping list prepared for stocks or funds that would be more attractive at lower prices and buy while others are selling
* *Turn off the noise*. Over the long term, market crashes such as Black Monday are a small blip in the performance of a well-structured portfolio, i.e.
    * Short-term market events are impossible to predict, and they are soon forgotten
    * Long-term investors are better served by tuning out the noise of the media and the herd and focusing on their long-term objectives

# Appendix
## Concepts
**Market capitalization**. A method of measuring the value of a company by multiplying the number of shares outstanding by its stock price

