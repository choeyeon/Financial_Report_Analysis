import pandas as pd
import matplotlib.pyplot as plt

# 1. Loading data
df = pd.read_excel("Financial_Sample.xlsx")

# 2. Check columns (with spaces)
print("Список колонок:", [f"'{col}'" for col in df.columns])

# 3. Removing spaces in column names
df.columns = df.columns.str.strip()

# 4. Analysis by segments
segment_report = df.groupby('Segment').agg({'Sales': ['sum', 'mean']})

# 5. Сreating graphs
segment_report['Sales']['sum'].plot(kind='bar', title='Сумарні продажі по сегментах')
plt.ylabel('Сума ($)')
plt.tight_layout()
plt.savefig('segment_sales.png') 
plt.show()

# 6. Analysis by month (add this block)
df['Date'] = pd.to_datetime(df['Date'])  
df['Month'] = df['Date'].dt.month_name()  
monthly_report = df.groupby('Month')['Sales'].sum().reset_index()

# 7. Export results
output_path = "Sales_Analysis_Report.xlsx"
with pd.ExcelWriter(output_path) as writer:
    segment_report.to_excel(writer, sheet_name="Segment_Analysis")
    monthly_report.to_excel(writer, sheet_name="Monthly_Trends")
    
print(f"Звіт збережено у файлі: {output_path}")