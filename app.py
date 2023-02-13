from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route('/')
def hello_world():
    data = {}
    RawData = pd.read_csv("static/data/superstore_dataset2011-2015.csv", encoding="ISO-8859-1")
    RawData["Order Date"] = pd.to_datetime(RawData["Order Date"])
    RawData["Ship Date"] = pd.to_datetime(RawData["Ship Date"])
    RawData["Order_year"] = RawData["Order Date"].dt.year
    RawData["Order_month"] = RawData["Order Date"].dt.month
    RawData["Order_quarter"] = RawData["Order Date"].dt.to_period("Q")
    Order_year = round(RawData.groupby(by="Order_year").sum()[["Sales", "Quantity", "Profit", "Shipping Cost"]], 2)
    Order_quarter = round(RawData.groupby(by="Order_quarter").sum()[["Sales", "Quantity", "Profit", "Shipping Cost"]], 2)
    Order_month = round(RawData.groupby(by=["Order_year", "Order_month"]).sum()[["Sales", "Quantity", "Profit", "Shipping Cost"]], 2)
    data["Order_year"] = Order_year
    data["Order_year_index"] = list(Order_year.index.values)
    data["Order_year_sales_values"] = list(Order_year["Sales"])
    return render_template("index.html", data=data)


if __name__ == '__main__':
    app.run()
