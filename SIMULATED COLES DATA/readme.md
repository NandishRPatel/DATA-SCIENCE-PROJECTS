

## SIMULATED COLES DATA - UNSUPERVISED KNOWLEDGE DISCOVERY

### Executive Summary

This report provides an analysis of the Simulated Coles data which consists of 58,100 observations and 53 variables. The aim of the analysis is to explore questions about which products customers are buying and what kind of customers are shopping at Coles. The answers to these questions can be used to enhance customer experience and/or to maximize profits which can be achieved by improving store layouts, offering discounts or marketing different products together, and determining the best place to shelf the specific products.

After cleaning and preprocessing the data, Clustering analysis and Market Basket analysis have been applied to the data. Clustering analysis results revealed that there 4 groups of customers based on income, age and spending value. These 4 groups are named Elderly High Spenders, High Spending Youth, All age & Broke and Rich & Wise. These groups are named based on their characteristics of the customers in the groups. Market Basket Analysis results uncovered that there is a high correlation between products like bread, milk & banana and nappies & baby food. Some less obvious product combinations were fish, vegetables & household cleaners and coffee, bread, vegetables, frozen meals & household cleaners. 

This report also offers a detailed explanation of data cleaning and analytical processes, data mining techniques, analysis outcome, and suggestions for future analysis.


### Introduction

Coles is one of the leading supermarkets in Australia, generally dealing with the provision of everyday goods. The emergence of competitors in the market has meant that the competition has become much fiercer and It is crucial for Coles to take strategic actions to beat the competition. One way to do that is to use the data Coles has been collecting from its customers and analyze data to gain a competitive edge. This report aims to use unsupervised knowledge discovery to find hidden patterns in customers’ transactions and to form customer segments. We’ll be seeking a better understanding of two aspects: 
	
* Customer Segments: - What are the different segments or groups and their demographic as well as socio-economic features.
* Products Patterns: - Popularity of the products, what kind of products are being bought together, the likelihood of two or more products being purchased together.

By better understanding these two aspects and finding answers to the questions related to these two aspects, Coles would be able to form sophisticated strategies that would help Coles to lead the competition. A better understanding of the customer segments would help Coles create more effective and successful market campaigns and design eye-catchy catalogs of the products whereas better knowledge of product patterns would allow coles to improve in-store layouts and product placements.



### Conclusion

*	Data Quality – Coles data set raised concerns about data quality – the age, Postcode variable and the sequential invalid entries in other variables like pmethod, nchildren, homeown.

*	Despite the data quality issues, it has provided great insights. The key results and recommendations are:

	*	Coles should put newly marketed products near the shelf of bread, milk, cereal, and banana So that customers are exposed to the new products. Coles should put these products to the end of the aisle So that customers have to walk more in the stores, in turn, they will be tempted to buy other products they see on their way to the most purchased product aisle.
	*	Baby Food should be displayed near the shelves of Napies, Fruit, Chocolate and Olive Oil.
	*	Coles could probably increase sales by advertising/marketing householCleaners,                 coffee, frozenmeal, TomatoSauce with Vegetables(if possible stock them near).
	*	Customers who bought Vegetables & Fish and Fruit and Fish are 2.2 and 2.0 times             more likely to buy householCleaner respectively. Coles should spatially separate fish,                 vegetables, fruit, and householCleaners for greater travel distance so that customers    will be encouraged to purchase other products.
	*	Coles should start marketing campaigns for family or house related products towards young customers(from cluster 3) as the majority of them are home owners and parents. These groups of customers are on a tighter budget and they will respond better to deals and discounts on the branded products that coles has to offer.
	*	On the other hand, luxury products should be targeted to customers(from cluster 1) who do not own a house and are females independent of their income and age. 


### Future Analysis

* Recording customer’s postcode adequately would help identify patterns by states or suburbs.
*	Recording data of as many customers and as many transactions as coles can by using various methods like using a points card like Flybuys. More data and correct data would help coles get meaningful insights from the data.
*	Quantity of items purchased alongside the value would be more helpful in assessing customer’s preferences and spending power.
*	MBA can be carried out on more generalized product categories for less-frequently purchased products, for example, put all the frozen items in one category that would increase the support of the products.
