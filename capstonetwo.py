


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

sns.set()

st.header("Capstone Two - Analyzing Spotify's Revenue and Expense")
st.subheader("By Andrei Ramos")
st.subheader("Introduction")
st.write("What is Spotify's financial performance like? As one of the most widely recognized music streaming services, offering not only a vast library of songs but also podcasts to users worldwide, Spotify has always piqued my curiosity in terms of its financial well-being. Now, I have the opportunity to delve into a thorough financial analysis of this industry leader.")
df = pd.read_csv('Spotify Quarterly.csv')
df

df.dropna(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

quarterly_data = df.resample('Q').sum()
start_year = 2017  
end_year = 2022
filtered_data = quarterly_data[(quarterly_data.index.year >= start_year) & (quarterly_data.index.year <= end_year)]
yearly_data = filtered_data.groupby(filtered_data.index.year).sum()

plt.figure(figsize=(10, 6))

colors = ['green', 'black', 'purple', 'orange']

#Yearly Revenue
ax = yearly_data[['Ad Revenue', 'Premium Revenue', 'Total Revenue']].plot(kind='bar', color=colors)
ax.set_xticklabels(yearly_data.index)
plt.xlabel('Year')
plt.ylabel('Revenue (Millions)')
plt.title('Yearly Revenue')
plt.legend()
plt.tight_layout()
st.pyplot(plt.gcf())
revenuetext = st.write("Over the years, Spotify has achieved remarkable growth in its key revenue streams, including ad revenue, premium revenue, and total revenue. Notably, 2022 marks a pivotal year in the company's financial history, with a substantial 200% increase in total revenue compared to 2017. This robust growth trajectory is mirrored by premium revenue, which has also seen a comparable rate of increase over the same period.")
revenuetext2 = st.write("Interestingly, ad revenue represents a relatively small portion, accounting for only around 5% of Spotify's total revenue. While it contributes to the company's overall earnings, it's evident that the subscription-based premium model has been the driving force behind Spotify's impressive financial performance in recent years.")

#Yearly Revenue
ax = yearly_data[['Ad Revenue', 'Premium Revenue', 'Total Revenue']].plot(kind='line', color=colors)
ax.set_xticklabels(yearly_data.index)
plt.xlabel('Year')
plt.ylabel('Revenue (Millions)')
plt.title('Yearly Revenue')
plt.tight_layout()
st.pyplot(plt.gcf())
revenuetext = st.write("Premium revenue has experienced a remarkable surge from 2017 to the present year, 2023. Over this period, it displayed a substantial and consistent growth trajectory. Ad Revenue, on the other hand, exhibits a somewhat fluctuating pattern, with occasional fluctuations that may lead to slight decreases, but overall, it maintains an upward trend.")
revenuetext2 = st.write("Among the years, 2022 stands out as Spotify's most impressive performance to date. During this period, the company achieved exceptional results, highlighting its ability to generate substantial revenue and establish a strong financial foothold. These insights into Spotify's financial performance provide valuable information about the company's progress and the factors contributing to its success.")

#Cost of Revenue Gross Profit
ax = yearly_data[['Ad Cost of revenue', 'Premium Cost Revenue', 'Ad gross Profit', 'Premium Gross Profit']].plot(kind='bar', color=colors)
ax.set_xticklabels(yearly_data.index)
plt.title('Cost of Revenue, Ad Gross Profit, and Premium Gross Profit comparison')
plt.xlabel('Year')
plt.ylabel('Revenue/Profit (Millions)')
plt.tight_layout()
st.pyplot(plt.gcf())
revenuetext = st.write("Our next step is to examine the cost of revenue concerning both ad and premium gross profit to assess Spotify's efficiency in managing its direct costs and maintaining a robust gross profit margin. Upon examination, it becomes evident that the cost of revenue is substantially higher for Premium gross profit. This observation suggests that Spotify may be allocating a significant portion of its resources to the production of goods and services associated with premium revenue, potentially impacting its profitability.")
revenuetext2 = st.write("In contrast, Spotify appears to be exercising greater cost control when it comes to ad-related revenue. This is a strategic decision, acknowledging that ad revenue is not as lucrative as premium revenue. The company's allocation of resources reflects an understanding of the disparity in profitability between these two revenue streams, with an emphasis on maximizing profitability from the premium segment.")

#Total Revenue and Cost of Revenue
ax = yearly_data[['Total Revenue', 'Cost of Revenue']].plot(kind='line', color=colors)
ax.set_xticklabels(yearly_data.index)
plt.xlabel('Year')
plt.ylabel('Users (Millions)')
plt.title('Total Revenue and Cost of Revenue')
plt.tight_layout()
st.pyplot(plt.gcf())
revenuetext = st.write('Moving forward, we can verify that Spotify consistently reports higher total revenue compared to its cost of revenue, and both these metrics exhibit a positive trend as the years progress. The fact that Spotify consistently outperforms its cost of revenue is a strong indicator of its positive financial health and operational efficiency.')

#Average Premium Users Over Time
ax = yearly_data[['Premium MAUs', 'Ad MAUs']].plot(kind='line', color=colors)
ax.set_xticklabels(yearly_data.index)
plt.xlabel('Year')
plt.ylabel('Users (Millions)')
plt.title('Average Premium Users and Ad Monthly Users Trend Over Time')
plt.tight_layout()
st.pyplot(plt.gcf())
revenuetext = st.write("When comparing the trends of average premium users and ad monthly users over time, both user types display a consistent upward trajectory, demonstrating steady growth over the years. Notably, ad monthly average users have consistently outpaced premium users in terms of popularity, and this trend continues to hold true even in the present day.")

#Premium Average Revenue Users
ax = yearly_data[['Premium ARPU']].plot(kind='line', color=colors)
ax.set_xticklabels(yearly_data.index)
plt.xlabel('Year')
plt.ylabel('Users (Millions)')
plt.title('Average Premium Revenue Per Users Over Time')
plt.tight_layout()
st.pyplot(plt.gcf())
revenuetext = st.write("While Spotify's premium revenue has been on a consistent upward trajectory, there has been a notable decline in the average premium revenue per user over time. This decline can be attributed to Spotify's strategic expansion into new markets across various countries. In an effort to penetrate these markets and attract a wider audience, Spotify has introduced discounted plans, which, while successful in expanding their user base, have had a discernible impact on the average premium revenue per user, leading to its reduction.")

#Expense Costs
ax = yearly_data[['Genreal and Adminstraive Cost', 'Research and Development Cost', 'Sales and Marketing Cost']].plot(kind='line', color=colors)
ax.set_xticklabels(yearly_data.index)
plt.xlabel('Year')
plt.ylabel('Costs (Millions)')
plt.title('Expense Costs')
plt.tight_layout()
st.pyplot(plt.gcf())
revenuetext = st.write("In the realm of expense costs, a trend emerges as the years progress, mirroring the upward trajectory seen in Spotify's ad revenue. General and Administrative Costs, Research and Development Costs, and Sales and Marketing Costs have all exhibited consistent growth over time. Notably, a significant portion of these expenses is allocated to Sales and Marketing—a strategic investment by Spotify.")
revenuetext2 = st.write("This emphasis on marketing is a pivotal factor contributing to Spotify's continued success, as it consistently attracts and engages new customers year after year. The company's commitment to marketing underscores its dedication to expanding its user base and maintaining its competitive edge in the dynamic music streaming industry.")

st.subheader("Conclusion")
conclusiontext = st.write('Remarkable Revenue Growth: Spotify has witnessed remarkable growth in key revenue streams, with substantial increases in ad revenue, premium revenue, and total revenue over the years.')
conclusiontext = st.write('Pivotal Year in 2022: 2022 marked a pivotal year for Spotify, with a significant 200% increase in total revenue compared to 2017, indicating a strong growth trajectory.')
conclusiontext = st.write('Dominance of Premium Revenue: Premium revenue has been a driving force in Spotifys financial success, with consistent growth and substantial surges from 2017 to 2023.')
conclusiontext = st.write('Role of Ad Revenue: Ad revenue, while contributing to overall earnings, represents a relatively small portion of Spotifys total revenue, accounting for approximately 5%.')
conclusiontext = st.write('Strategic Emphasis on Marketing: Spotifys investment in Sales and Marketing costs has played a pivotal role in its success, consistently attracting and engaging new customers.')
conclusiontext = st.write('Efficient Cost Management: Spotify appears to be efficiently managing its cost of revenue, with an emphasis on profitability, particularly in the premium segment.')
conclusiontext = st.write('Consistent User Growth: Both average premium users and ad monthly users have displayed consistent upward trends, indicating steady user growth.')
conclusiontext = st.write('Impact of Discounted Plans: The decline in average premium revenue per user can be attributed to Spotifys strategic expansion into new markets and the introduction of discounted plans to attract a broader audience.')

