import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr

def calculate_correlation_and_pvalue(exam_dates, nightmare_dates):
    exam_df = pd.DataFrame({'Date': exam_dates})
    nightmare_df = pd.DataFrame({'Date': nightmare_dates})

    combined_df = pd.merge(exam_df, nightmare_df, on='Date', how='outer') 

    combined_df['Exams'] = combined_df['Dates'].isin(exam_dates).astype(int)
    combined_df['Nightmares'] = combined_df['Dates'].isin(nightmare_dates).astype(int)

    correlation, p_value = pearsonr(combined_df['Exams'], combined_df['Nightmares'])

    return combined_df, correlation, p_value

exam_dates = [
    pd.to_datetime('2024-12-01'),
    pd.to_datetime('2024-12-07'),
    pd.to_datetime('2024-12-09'),
    pd.to_datetime('2024-12-14'),
    pd.to_datetime('2025-01-02'),
    pd.to_datetime('2025-01-04'),
    pd.to_datetime('2025-01-06'),
    pd.to_datetime('2025-01-07'),
    pd.to_datetime('2025-01-10')
]
nightmare_dates = [
    pd.to_datetime('2024-12-07'),
    pd.to_datetime('2024-12-27'),
    pd.to_datetime('2024-12-29'),
    pd.to_datetime('2025-01-01'),
    pd.to_datetime('2025-01-07')
]

combined_df, correlation, p_value = calculate_correlation_and_pvalue(exam_dates, nightmare_dates)
print(f"Correlation between exam dates and nightmare dates: {correlation}")
print(f"P-value: {p_value}")

plt.figure(figsize=(10, 6))
plt.scatter(combined_df['Dates'], combined_df['Exams'], label='Exam', color='green', alpha=0.6)
plt.scatter(combined_df['Dates'], combined_df['Nightmares'], label='Nightmare', color='orange', alpha=0.6)
plt.xlabel('Dates')
plt.ylabel('Indicator (1 = Yes, 0 = No)')
plt.title('Scatter Plot of Exam Dates vs Nightmare Dates')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()