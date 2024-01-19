import pandas as pd

df = pd.read_csv('Cleaned_data_version2_sanath.csv')

print("\n I am going to print the index")
print(df.keys())
print('\n Printed index')

def suggest_products(category, sub_category):
    category = category.lower().strip()
    sub_category = sub_category.lower().strip()
    print("Category is ", {category}, "\n")
    print("Sub Category is ", {sub_category}, "\n")

    filtered_df = df[(df['category'].str.lower().str.strip() == category) & (df['sub-category-1'].str.lower().str.strip() == sub_category)]
    sortfiltdf = filtered_df.sort_values(["Reviews"], axis=0, ascending=[False])
    print('first 3 values of filtered_df\n')
    print(filtered_df[0:3])
    print('first 3 values of sortfiltdf\n')
    print(sortfiltdf[0:3])

    if not sortfiltdf.empty:
        numfiltprods = len(sortfiltdf)
        print("There were ", numfiltprods, "products")
        numtodisplay = min(2, numfiltprods)
        print("I am showing you ", numtodisplay, "products")
        shortlistfiltdf = sortfiltdf.head(numtodisplay)
        print(f"\n Most popular products under {category} -> {sub_category}: ")
        print(f"- Unique names of products like this are \n")

        unique_product_names = set()
        for product_name in sortfiltdf['Product_Name']:
            unique_product_names.add(product_name)
            if len(unique_product_names) >= 2:
                break

        for product_name in unique_product_names:
            print(product_name)

        common_ingredients = shortlistfiltdf['ingredients'].unique()
        if len(common_ingredients) > 0:
            print("\nCommon ingredients used in products like this are ")
            for ingredient in common_ingredients:
                print(f"- {ingredient}")

        print("\nSuggested price range per 100g ")
        inrprice = shortlistfiltdf['India priceINR per 100g'];
        usdprice = shortlistfiltdf['US price $ per 100g'];
        mininr = min(inrprice)
        maxinr = max(inrprice)
        minusd = min(usdprice)
        maxusd = max(usdprice)
        if (maxinr==mininr):
            print('India :  around ', mininr , ' Rupees\n')
        else:
            print(' India : Between ', mininr , ' and ', maxinr, ' Rupees\n')    

        if (maxusd==minusd):
            print('USA :  around ', minusd , ' $\n')
        else:
            print(' USD : Between ', minusd , ' and ', maxusd, ' $\n')    

        #for  row in shortlistfiltdf.iterrows():
        #    print(f"- India(INR): {row['India priceINR per 100g']:.2f}")
        #    print(f"- USA(USD): {row['US price $ per 100g']:.2f}")
    else:
        print(f"No products found under {category} -> {sub_category}.")

user_category = input("Enter the category: ")
user_sub_category = input("Enter the sub category: ")

suggest_products(user_category, user_sub_category)
