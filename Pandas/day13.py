import pandas as pd

print(pd.__version__)

# ==========================Series================
# invoice_amount = pd.Series([1500, 4333, 4444, 4444], index=["INV01", "INV02", "INV03","INV04"])

Invoice_data = pd.Series([1500, 4333, 5444, 43232], name="Amount")

# print(invoice_amount["INV01"])

# print(Invoice_data)
# print(Invoice_data.index)
# print(Invoice_data.values)
# print(Invoice_data.dtype)
# print(Invoice_data.name)
print(Invoice_data.size)

# ========================DataFrame====================

data = pd.DataFrame(
    {
        "Invoice Number": ["IN01", "IN02","IN03"],
        "Amount": [12355, 4343, 2312312],
        "Status": ["Accept", "Reject","Pending"],
    }
)
# print(data)
# for index,invoice in data.iterrows():
#     # print(invoice)
#     print(f'Invoice Number : {invoice["Invoice Number"]} Amount :{invoice["Amount"]}')

# for invoice in data.itertuples(index=False):
#     print(f'Invoice Number : {invoice[0]} Amount :{invoice[1]} Status : {invoice[2]}')

print(f'data head{data.head(1)}')
print(f'data tail {data.tail(1)}')
print(data.shape)
print(data.columns)
print(data.info())
print(data.describe())
print(data.values.tolist())
print(data.loc[2,["Invoice Number"]])