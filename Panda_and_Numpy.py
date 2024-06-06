# pandas
import pandas as pd
sales_data=pd.read_csv("sales_data (1).csv")

grouped_sales_data=sales_data.groupby(['product_category','customer_segment']).agg({'sales':'sum','discount':'mean'
}).reset_index()

print(grouped_sales_data)


# question 3:
"""product_detail=pd.DataFrame({
    "product_id":['10','45','90'],
    "product_name":['product A','product B','product C'],
    "product_category":['category A','category B','category C']})
merge_data=pd.merge(sales_data,product_detail,on=('product_id'))
print(merge_data)"""

# Numpy
"""import numpy as np
iris_data=pd.read_csv("Iris.csv")
numerical_features=iris_data.drop(columns=['Species'])
correlation_data=np.corrcoef(numerical_features,rowvar=False)
print(correlation_data)
"""