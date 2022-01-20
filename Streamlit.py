import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("Analyse sur l'évolution des performances mécanique par continent", anchor=None)

continent = st.selectbox(label = 'Choisi un pays', options = (' Europe.', ' US.', ' Japan.'))

st.subheader(continent)


df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

df_continent = df.loc[df.continent == continent]

st.subheader('Heatmap')

# display heatmap
plt.figure(figsize = (20, 10)) 
viz_correlation = sns.heatmap(df.corr(), center = 0, cmap = "vlag", annot=True, vmin = -1, vmax = 1, mask = np.triu(np.ones_like(df.corr())))

st.pyplot(viz_correlation.figure)

st.markdown("On constate qu'entre 1971 et 1983, il n'y a pas d'évolution significative sur le nombre de cylindre, la cylindré, et la puissance du moteur (hp). En revanche")
