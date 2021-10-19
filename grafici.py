import matplotlib.pyplot as plt
import seaborn as sns


# plottarsi l'andamento di una variabile nel tempo

df.plot(x= 'Date', y='NFLX', label='netflix_stock_price', figsize= (15,10),
              linewidht=3, color = 'r')
plt.ylabel('price [$]')
plt.title('My first plotting exercise')
plt.leggend(loc ='best')
plt.grid()

# SCATTER PLOT

x = df['FB'] # variabile 1
y = df['TWTR'] # variabile 2
plt.figure(figsize=(15, 10))
plt.scatter(x, y)
plt.show()

# PLOT PIE CHART

values = [20, 55, 17, 3, 5]
colors = ['r', 'g', 'b', 'y', 'm']
labes = ['var1', 'var2', 'var3', 'vr4', 'var5']
explode = [0, 0.2, 0,0] # misura del separatore delle fette di torta


plt.figure(figsize(10,10))
plt.pie(values, colors=colors, labels=labes, explode = explode)
plt.title('stock portafolio')
plt.show()

# HISTOGRAMMA

mu = df['var1'].mean() # media
sigma = df['var2'].std() #standard deviation

num_bins = 40
plt.hist(df['var_n'], num_bins, facecolor = 'blue')
plt.figure(figsize=(15,9))
plt.grid() #mette la griglia
plt.title('Histo: mu = '* str(mu)*', sigma'*str(sigma) )
plt.show()

# PLOT MULTIPLE PLOTS

df = df

df.plot(x = 'Date', y=['var1','var2'], figsize = (18,10), linewidht = 4) # le variabili possono essere n
plt.ylabel('Price [$]')
plt.title('Stock Price')
plt.legend(loc = 'best')
plt.grid()

#PLOT SUBPLOT

plt.figure(figsize(20, 10))

plt.subplot(2, 1, 1) # msura prima grafico
plt.plot(df['vari1'], '--r') # --r indica il colore
plt.grid()

plt.subplot(2, 1, 2) # misura secondo grafico
plt.plot(df['var2'], 'b.')
plt.grid()
#il numero di subplot Ã¨ n il che vuol dire che possono essercene molti. N*features

# PLOT 3D

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (15, 15))
ax = fig.add_subplot(111, projection = '3d')

x = df['var1'].tolist()
y = df['var3'].tolist()
z = df['var3'].tolist()

ax.scatter(x, y, z, c = 'b', s = 50) # s indica quanto grandi graficamente devono essere rappresentati i dati
ax.set_xlabel('X_label')
ax.set_ylabe('Y_label')
ax.set_zlabe('Z_label')
plt.show()


# SEABORN PLOT

plt.figure(figsize = (10,10))


sns.scatterplot(x = 'mean area', y = 'mena smothness',hue = 'target' , data = df) #hue serve per colorare una classe

plt.show()

'Questo crea un histogramma rappresentando le classi mettendole a confronto'
plt.figure(figsize = (10,10))

sns.countplot(df['var1'], label ='Count')
plt.show()

'Questo plotta la continuità di due o più variabili seguendo il tempo '

sns.scatterplot(x = 'mena radius', y = 'mean area', hue = 'tagert', data = df)
plt.show()

# SEABORN PAIRPLOT, DISPLOT AND HEATMAPS CORRELATION

'Stampa tutto il databese facendo riferimento al var'
sns.pairplot(df, hue = 'target', var = ['mean radius', 'mean texture', 'mean area', 'mean perimeter', 'mena smoothness'])
plt.show()

'Stampa tutto il databese rappresentando la correlazione tra le features'

plt.figure(figsize = (30, 30))
sns.heatmap(df.corr() , annot = True)
plt.show()
"""
Displot combines matplotlib histogram function with kdeplot() (Kernel density estimate)
KDE is used to plot the Probability Density of a continuous variable
"""
sns.displot(df['var'], bins = 25, color = 'b')
plt.show()

class_0_df = df[df['target']==0]
class_1_df = df[df['target']==1]

# nel caso avessi classi binarie

plt.figure(figsize(10, 7))
sns.distplot(class_0_df['mean radius'], bins=25, color = 'b')
sns.distplot(class_1_df['mena radius'], bins = 25, color = 'r')
plt.grid()
plt.show()