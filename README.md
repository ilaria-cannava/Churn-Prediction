##### Final Project for the Data Science Bootcamp at The Developer Academy
##### Data Science for Marketing <br/>
### CUSTOMER CHURN PREDICTION <br/>
##### Context <br/>
Numerous research studies have confirmed that for businesses, the cost of acquiring a new customer to achieve the profitability of an existing one can be up to 16 times higher than retention efforts. Moreover, even a modest 5% reduction in the churn rate holds the potential to increase profitability by 25–125%.<br/>

In light of this, the Data Team at a phone and network provider has been tasked with conducting churn data analysis and prediction. The objective is to furnish actionable insights for the customer service, marketing, and product departments, enabling informed decision-making aimed at mitigating customer churn.<br/>

#### Check the file churn_prediction_project.ipynb for full code and content

##### Table of content
1. Import libraries and tools
2. Load data
3. Exploratory Data Analysis, data wrangling and cleaning 
4. Data Visualisation
5. Features choice and features engineering
6. Preparing the data for training the model
7. Training a logistic regression model as baseline
8. Training Random Forest model with the 3 data sets, making predictions and evaluate the models
9. Training SVM with the 3 data sets, making predictions and evaluate the models
10. Training XGBoost with the 3 data sets, making predictions and evaluate the models
11. Performing customer segmentation 
12. Models evaluation recap
13. Conclusions
14. Saving the model
15. Link to streamlit app
    
#### What is CHURN RATE? 
* Churn rate, customer churn or rate of attrition: the rate at which customers stop doing business with an entity.
* "Churning" in a business refers to the number of subscribers that leave a provider or the number of employees that leave a firm in a given period.
* Commonly espressed with a percentage of service subscribers who discontinue their subscriptions within a given time period.<br/>
Can be used also in subscription free services.
* It is also used to identify the rate employers leave their job within a certain period of time.
* Churn rates can be applied to subscription-based businesses as well to the number of employees that leave a firm.
* For a company to expand their clientele must be <br/>
GROWTH RATE (number of new customers)>CHURN RATE<br/>
Growth rate and churn rate are opposite factors
* Each industry will have a different average churn rate that companies can compare themselves with to understand their competitiveness.<br/>
What is considered a good or bad churn rate can vary from industry to industry.
* It's important to pay attention to customer acquisition costs and to note whether a customer churns before you have made back the money spent on acquiring that customer.
* The advantage of calculating a company's churn rate is that it provides clarity on how well the business is retaining customers, <br/>
which is a reflection on the quality of the service the business is providing, as well as its usefulness.
* The churn rate will indicate to a company that it needs to understand why its clients are leaving and where to fix its business. The cost of acquiring new customers is much higher than it is to retain current customers, so as you ensure that the customers you worked hard to attract remain as paying customers, it makes sense to understand the quality of your business.
* One of the limitations of the churn rate is that it does not take into consideration the types of customers that are leaving. Customer decay is primarily seen in the most recently acquired customers. But here is were a segmentation will clear the nature of thes customers.



#### 13. Conclusions
##### Useful insights for marketing to understand what a churned customer means within our business: it is a person who could not find the right plan to fit their usage of calls and internet.

* The churn rate of the company calculated on the base of the given data is 28.6%. This is in line with the telecommunication industry (ranging from 25% to 30%) the company is starting from a decent point, even if we all know that fine tuning a success could be more challenging and draining than improving a slaggish situation. Considering that many studies has proved that th ecost of acquiring new customers could be 15-20 times more expensive than acquiring new ones, a reduction of only 2.6% would be a significant an welcomed success that would bring the company among the leaders of the sector, with increased profits and improved brand strenght. To give a real taste of what this means in terms of retented customers, on this data set would signify to manage to keep with us and extra ~1300 customers.

* Churn rate is mostly omogeneous across the data set, meaning there are no features incredibly effecting it and the distribution of the churn follow the one of the features as we can see from the distribution plots. One thing that we must notice is how skewed are the features on the right. What we decided to do is to investigate those ouliers and find any useful insight.

* Churn is very entangled in the data, making customer segmentation not the most efficient tool to adress it as we can see from the scatter plots. Considering though some of the most relevant feature we can still group customers in order to create specific action. For instance the segmentation using 'Percentage Change Revenues' and 'Percentage Change Minutes' shows a category of valueable customer increasing their spending and minutes. Still there is churn among them, so we may want to run rewards in that group while we may want to run discount rates or incentive in the group that is using the service less and spending less.  

* We did a deep analysis of single features to highlight trends and behaviours among outliers, some of the insights exctracted are:
    1. More than 50% customers their Percentage Change in minutes usage is negative, churn. Survey to be made and understanding the reason behind the reduced usages. Are they paying for wrong plan or added services?
    2. Churn rate among customers using 0 minutes is 60.05% and they are 2.82% of the total churn. Again, why this people are leaving?  Do they need a convenient only data plan?
    3. Churn rate among outliers customers in OverageMinutes (using more hundreds more minutes than the plan they have allows) is 31.55%, above data set average. Churning customers with high overage are 12.85% of the toatl churn. Certainly plans to be reviews and a survey to be made to accomodate the needs of this group. 
    4. Customer who contacted customer service more are also more likely to churn. Customer who were reached by retention calls also are more likely to churn. It means that even when we knew exactly the high risk of churn of the customers, probably expressed directly by them, we could not stop them from churn. Certainly this calls for a deep and strict review of customer service procedures, retention call contents, retention offers. This even before we plan any marketing action or any change in the services provided and value added services.
    5. Handsets and equipment matters. Are we offering an easy and convenient way to upgrade the handsets?
    6. We are missing info about value added service and internet usage. 

* We did create a predictive model deployed as an app, for the retention team to identify customers with high risk of churning.
