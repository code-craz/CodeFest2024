import pandas as pd

# Read the modified CSV file without sub-category-1
df = pd.read_csv('Cleaned_data_version2_sanath.csv')
print('\n going to print index\n')
print(df.keys())
print('\n printed index above\n')
def suggest_products(category, sub_category):
    # Convert user input to lowercase and remove leading/trailing whitespaces
    category = category.lower().strip()
    sub_category = sub_category.lower().strip()

    print('given category is ', category, '\n')
    print('given sub category is ', sub_category, '\n')
    # Filter the dataframe based on user input (case-insensitive)
    filtered_df = df[(df['category'].str.lower().str.strip() == category) & (df['sub-category-1'].str.lower().str.strip() == sub_category)]

    sortfiltdf = filtered_df.sort_values(["Reviews"],  
                    axis=0, 
                    ascending=[False]) 
    print('first 3 values of filtered_df\n')
    print(filtered_df[0:3])
    print('first 3 values of sortfiltdf\n')
    print(sortfiltdf[0:3])
    
    if not sortfiltdf.empty:
        # Display product names
        numfiltprods = len(sortfiltdf)
        print('\n there were ', numfiltprods, ' products')
        numtodisplay = min(2, numfiltprods)
        print( '\n I am showing ', numtodisplay, ' products \n')
        shortlistfiltdf = sortfiltdf.head(numtodisplay)
        print(f"\nMost popular Products under {category} -> {sub_category}:")
        for i, row in shortlistfiltdf.iterrows():
            print(f"- Common names of products like this are {row['Product_Name']}")

            # Display ingredients
            print("\nCommon ingredients used in these products:")
            print(f"- {row['ingredients']}")

            # Suggested price range
            print("\nSuggested Price Range (per 100g):")
            print(f"- India: INR {row['India priceINR per 100g']:.2f}")
            print(f"- US: $ {row['US price $ per 100g']:.2f}")

    else:
        print(f"No products found under {category} -> {sub_category}.")

# Get user input
print(df)
user_category = input("Enter the category: ")
user_sub_category = input("Enter the sub-category: ")

# Call the function to suggest products, ingredients, and price range
suggest_products(user_category, user_sub_category)
