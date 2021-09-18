<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Skewness](#skewness)
- [Kurtosis](#kurtosis)
<!-- /TOC -->

# Skewness
**Skewness**: measure the asymmetry of the probability distribution of a real-valued random variable about its mean

**Pearson's moment coefficient of skewness**: $\gamma_1 = E[(\frac{X - \mu}{\sigma})^3]$
* Other name: moment coefficient of skewness

**Applications**:
* A descriptive statistic used on conjunction with histogram and normal quantile plot to characterize the data or distribution
* Indicate which direction and a relative magnitude of how far a distribution deviates from normal (i.e. zero skewness)

**Other measures of skewness**:
* Pearson's first skewness coefficient (mode skewness): $\frac{\text{mean} - \text{mode}}{\text{standard deviation}}$
* Pearson's second skewness coefficient (median skewness): $\frac{3 (\text{mean} - \text{median})}{\text{standard deviation}}$
* Quartile-based measures: $\frac{(Q_3 - Q_2) + (Q_1 - Q_2)}{Q_3 - Q_1}$ where $Q_1, Q_2, Q_3$ are $25\%, 50\%$ and $75\%$ percentiles
* Groeneveld & Meeden's coefficient: $\frac{\mu - \nu}{E(|X - \nu|)}$ where $\nu$ is the median

# Kurtosis
**Kurtosis**: measure the "tailedness" of probability distribution of a real-valued random variable 
* "Kurtosis": mean "curved, arching" in Greek

**Pearon's moment definition of kurtosis**: $E[(\frac{X - \mu}{\sigma})^4]$
* Lower bound: $\text{kurtosis} \geq \text{skewness}^2 + 1$ 
* Interpretation: represent tail extremity 
    * Explain: either existing outliers (for sample kurtosis), or propensity to produce outliers (for probability distribution kurtosis)
* Intuition: kurtosis measures outliers only, it measure nothing about the "peak" 
    * Any standardized values which are less than $1$ (i.e. within one standard deviation of the mean), contribute virutally nothing to kurtosis
    * Only data values outside the region of peak (i.e. outliers) contributes significantly to the kurtosis
  
**Applications**: check whether there is a problem with outliers in a dataset