import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Uppgift 1
kommun = ['Malmö', 'Stockholm', 'Uppsala', 'Göteborg']
befolkning = [347949, 975551, 233839, 583056]
df_städer = pd.DataFrame({'Kommun': kommun, 'Befolkning': befolkning})

# a)
print(df_städer['Kommun'])

# b)
df_göteborg = df_städer[df_städer['Kommun'] == 'Göteborg']
print(df_göteborg)

# c)
befolkning_sorterad = df_städer.sort_values(by='Befolkning', ascending=False)
print(befolkning_sorterad)

# d)
top3_befolkning = befolkning_sorterad.iloc[:3]
print(top3_befolkning)

# e)
befolkning_sorterad['Befolkning (%)'] = (befolkning_sorterad['Befolkning'] / 10379295) * 100
print(befolkning_sorterad.round(2))

# Uppgift 2
# a)
df = pd.read_excel(r'Databehandling\Exercises\komtopp50_2020.xlsx', header=6, usecols='A:F', sheet_name='Totalt')
print(df.head())
print(df.info())
print(df.describe())

# b)
df.columns = ['Rang 2020', 'Rang 2019', 'Kommun', 'Folkmängd 2020', 'Folkmängd 2019', 'Förändring (%)']
print(df)

# c)
df = df.sort_values(by='Folkmängd 2020', ascending=False).reset_index()
df.drop('index', axis=1, inplace=True)
print(df)

# d)
df_reversed = df.sort_values(by='Folkmängd 2020', ascending=True).reset_index()
df_reversed.drop('index', axis=1, inplace=True)
bot5_df = df_reversed.iloc[:5]
print(bot5_df)

# e)
pop_19 = int(df['Folkmängd 2019'].sum())
pop_20 = df['Folkmängd 2020'].sum()
print(f'Population of Sweden in 2019: {pop_19}, Population of Swedens in 2020: {pop_20}')

# f)
top5_df = df.iloc[:5]
fig, axes = plt.subplots(1, 2, dpi=120, figsize=(14, 4))
titles = ['Swedens 5 largest cities', 'Swedens 5 smallest cities']
data_frames = [top5_df, bot5_df]
x_column = ['Kommun', 'Kommun']
for i, (data, title) in enumerate(zip(data_frames, titles)):
    sns.barplot(data=data, x=x_column[i], y='Folkmängd 2020', ax=axes[i])
    axes[i].ticklabel_format(style='plain', axis='y')
plt.show()

# Uppgift 3
# a)
df_kvinna = pd.read_excel(r'Databehandling\Exercises\komtopp50_2020.xlsx', header=6, usecols='A:F', sheet_name='Kvinnor')
df_kvinna.columns = ['Rang 2020', 'Rang 2019', 'Kommun', 'Folkmängd 2020', 'Folkmängd 2019', 'Förändring (%)']
df_kvinna['Kön'] = 'Kvinna'
df_man = pd.read_excel(r'Databehandling\Exercises\komtopp50_2020.xlsx', header=6, usecols='A:F', sheet_name='Män')
df_man.columns = ['Rang 2020', 'Rang 2019', 'Kommun', 'Folkmängd 2020', 'Folkmängd 2019', 'Förändring (%)']
df_man['Kön'] = 'Man'
df_kvinna['Förändring (%)'] = pd.to_numeric(df_kvinna['Förändring (%)'], errors='coerce')
df_man['Förändring (%)'] = pd.to_numeric(df_man['Förändring (%)'], errors='coerce')
print(df_kvinna)
print(df_man)

# b)
df_kön = pd.concat([df_kvinna, df_man], ignore_index=True)
df_kön = df_kön.sort_values('Kommun', ascending=True)[['Kommun', 'Folkmängd 2020', 'Folkmängd 2019', 'Förändring (%)', 'Kön']]
print(df_kön)

# c)
merged = pd.merge(df_kvinna, df_man, on='Kommun', suffixes=('_K', '_M'))
merged['Total pop 2020'] = df_kvinna['Folkmängd 2020'] + df_man['Folkmängd 2020']
merged['Total pop 2019'] = df_kvinna['Folkmängd 2019'] + df_man['Folkmängd 2019']
merged['Total förändring (%)'] = (df_kvinna['Förändring (%)'] + df_man['Förändring (%)']) /2
print(merged.dropna()[['Kommun', 'Total pop 2020', 'Total pop 2019', 'Total förändring (%)']])


# d)
merged_full = pd.merge(merged, df_kön, on='Kommun')
print(
    merged_full.sort_values(by='Total pop 2020', ascending=False).head()
    [['Kommun', 'Folkmängd 2020', 'Folkmängd 2019', 'Förändring (%)', 'Kön', 'Total pop 2020', 'Total pop 2019', 'Total förändring (%)']]
    .to_string(index=False)
    )

# e)
top10 = merged_full.sort_values(by='Total pop 2020', ascending=False).iloc[:20]
bot10 = merged_full.sort_values(by='Total pop 2020', ascending=True).iloc[:20]
fig, axes = plt.subplots(1, 2, dpi=100, figsize=(14, 4))
titles = ['Könsdistribution I Sveriges 10 största städer', 'Könsdistribution I Sveriges 10 minsta städer']
data_frames = [top10, bot10]
x_column = ['Kommun', 'Kommun']
for i, (data, title) in enumerate(zip(data_frames, titles)):
    sns.barplot(data=data, x='Folkmängd 2020', y=x_column[i], ax=axes[i], hue='Kön', palette={'Kvinna': 'red', 'Man': 'blue'})
plt.show()

# f)
tot_man = sum(df_man['Folkmängd 2020'])
tot_kvinna = sum(df_kvinna['Folkmängd 2020'])
värden = [tot_man, tot_kvinna]
labels = [f'Män {tot_man}', f'Kvinnor {tot_kvinna}']
plt.pie(värden, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Könsfördelning i Sverige 2020')
plt.axis('equal')
plt.show()

# g)
merged['Gender diff (%)'] = (
    (merged['Folkmängd 2020_K'] - merged['Folkmängd 2020_M']).abs() 
    / merged['Total pop 2020'] 
    * 100
)
top5_diff = merged.sort_values('Gender diff (%)', ascending=False).iloc[:5]
top5_melted = top5_diff.melt(
    id_vars=['Kommun'], 
    value_vars=['Folkmängd 2020_K', 'Folkmängd 2020_M'],
    var_name='Kön', 
    value_name='Folkmängd'
)
top5_melted['Kön'] = top5_melted['Kön'].replace({
    'Folkmängd 2020_K': 'Kvinna', 
    'Folkmängd 2020_M': 'Man'
})
plt.figure(figsize=(10,6))
sns.barplot(data=top5_melted, x='Folkmängd', y='Kommun', hue='Kön', palette={'Kvinna': 'red', 'Man': 'blue'})
plt.title('Top 5 städer med störst skillnad i könsdistribution')
plt.show()

# h)
best5_growth = merged.sort_values(by='Total förändring (%)', ascending=False)[:5]
plt.figure(figsize=(10,6))
sns.barplot(data=best5_growth, x='Total förändring (%)', y='Kommun')
plt.title('Top 5 städer med mest tillväxt')
plt.show()