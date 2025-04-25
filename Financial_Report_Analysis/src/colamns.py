import pandas as pd

# Завантажте файл
df = pd.read_excel(r"C:\Users\vladi\OneDrive\Документи\Portfolio\1_example\Financial_Sample.xlsx")

# Показати всі назви колонок
print("Список колонок у файлі:", df.columns.tolist())

# Показати перші 3 рядки
print("\nПерші рядки даних:")
print(df.head(3))