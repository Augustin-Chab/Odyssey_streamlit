import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("Analyse sur l'évolution des performances mécanique par continent", anchor=None)

continent = st.selectbox('Choisi un pays', (' Europe.', ' US.', ' Japan.'))

st.write('You selected:', option)

st.subheader(continent)


df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

df_continent = df.loc[df.continent == continent]

st.subheader('Heatmap')

# display heatmap
plt.figure(figsize = (20, 10)) 
viz_correlation = sns.heatmap(df.corr(), center = 0, cmap = "vlag", annot=True, vmin = -1, vmax = 1, mask = np.triu(np.ones_like(df.corr())))

st.pyplot(viz_correlation.figure)

st.markdown("On constate qu'entre 1971 et 1983, il n'y a pas d'évolution significative sur le nombre de cylindre, la cylindré, et la puissance du moteur (hp). En revanche")

# pivot table for mean by hp evolution
pt = pd.pivot_table(df, index = 'year', values = 'hp', aggfunc = 'mean')
pt['year'] = pt.index

# Evolution de la puissance moyenne du moteur
sns.set()
plt.figure(figsize = (20, 10))
plt.title('Evolution de la puissance moyenne du moteur', size = 20)
viz = sns.barplot(data = pt, x = pt.year, y = pt.hp, color ="blue")

st.pyplot(viz.figure)

# pivot table for mean by cubicinches evolution
pt_1 = pd.pivot_table(df, index = 'year', values = 'cubicinches', aggfunc = 'mean')
pt_1['year'] = pt.index

# Evolution de la cylindré moyenne 
sns.set()
plt.figure(figsize = (20, 10))
plt.title('Evolution de la cylindré moyenne', size = 20)
viz_1 = sns.barplot(data = pt_1, x = pt.year, y = pt_1.cubicinches, color ="blue")

st.pyplot(viz_1.figure)

# pivot table for mean by weightlbs evolution
pt_2 = pd.pivot_table(df, index = 'year', values = 'weightlbs', aggfunc = 'mean')
pt_2['year'] = pt.index

# Evolution du poids moyen
sns.set()
plt.figure(figsize = (20, 10))
plt.title('Evolution du poids moyen', size = 20)
viz_2 = sns.barplot(data = pt_2, x = pt.year, y = pt_2.weightlbs, color ="blue")

st.pyplot(viz_2.figure)

# pivot table for mean by time-to-60 evolution
pt_3 = pd.pivot_table(df, index = 'year', values = 'time-to-60', aggfunc = 'mean')
pt_3['year'] = pt.index

# Evolution du time to 60 moyen
sns.set()
plt.figure(figsize = (20, 10))
plt.title('Evolution du time to 60 moyen', size = 20)
viz_3 = sns.barplot(data = pt_3, x = pt.year, y = pt_3['time-to-60'], color ="blue")

st.pyplot(viz_3.figure)
