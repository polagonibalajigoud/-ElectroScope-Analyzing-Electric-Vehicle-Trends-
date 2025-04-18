import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Load the dataset
df = pd.read_csv(r"C:\Users\anony\Downloads\python.csv", encoding='ISO-8859-1')

# Clean data (drop rows with NaNs in key numeric columns)
df = df.dropna(subset=['Electric Range', 'Base MSRP', 'Model Year'])

# ---------------------- PIE CHART ----------------------
plt.figure(figsize=(6,6))
df['Make'].value_counts().head(5).plot.pie(autopct='%1.1f%%')
plt.title('Top 5 EV Makes')
plt.ylabel('')
plt.show()

# ---------------------- VIOLIN PLOT ----------------------
plt.figure(figsize=(10,6))
sns.violinplot(data=df, x='Electric Vehicle Type', y='Electric Range')
plt.title('Electric Range by Vehicle Type')
plt.xticks(rotation=45)
plt.show()

# ---------------------- SWARM PLOT ----------------------
plt.figure(figsize=(10,6))
sns.swarmplot(data=df.sample(200), x='Electric Vehicle Type', y='Electric Range')
plt.title('Swarm Plot of Electric Range (Sample of 200)')
plt.xticks(rotation=45)
plt.show()

# ---------------------- LINE PLOT ----------------------
plt.figure(figsize=(10,6))
yearly_avg = df.groupby('Model Year')['Electric Range'].mean()
sns.lineplot(x=yearly_avg.index, y=yearly_avg.values)
plt.title('Average Electric Range by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Avg Electric Range')
plt.show()

# ---------------------- BAR PLOT ----------------------
plt.figure(figsize=(10,6))
make_avg = df.groupby('Make')['Electric Range'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=make_avg.index, y=make_avg.values)
plt.title('Top 10 Makes by Avg Electric Range')
plt.xticks(rotation=45)
plt.ylabel('Average Electric Range')
plt.show()

# ---------------------- STACKED BAR PLOT ----------------------
stacked = df.groupby(['Make', 'Electric Vehicle Type']).size().unstack().fillna(0)
stacked.loc[stacked.sum(axis=1).sort_values(ascending=False).head(5).index].plot(kind='bar', stacked=True)
plt.title('Top 5 Makes by Vehicle Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# ---------------------- DONUT CHART ----------------------
plt.figure(figsize=(6,6))
sizes = df['Electric Vehicle Type'].value_counts()
plt.pie(sizes, labels=sizes.index, autopct='%1.1f%%', wedgeprops=dict(width=0.4))
plt.title('EV Type Distribution (Donut Chart)')
plt.show()

# ---------------------- AREA CHART ----------------------
year_make = df.groupby(['Model Year'])[['Electric Range', 'Base MSRP']].mean()
year_make.plot.area(alpha=0.5)
plt.title('Area Chart: Avg Electric Range & MSRP by Year')
plt.ylabel('Average Values')
plt.xlabel('Model Year')
plt.show()

# ---------------------- SCATTER PLOT ----------------------
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Electric Range', y='Base MSRP', hue='Electric Vehicle Type')
plt.title('Electric Range vs Base MSRP')
plt.show()

# ---------------------- CORRELATION HEATMAP ----------------------
plt.figure(figsize=(8,6))
sns.heatmap(df[['Electric Range', 'Base MSRP', 'Model Year']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
