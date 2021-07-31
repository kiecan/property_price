from matplotlib.colors import ListedColormap


cmap = ListedColormap(['#0343df', '#e50000', '#ffff14', '#929591'])

ax = df.plot.bar(x='year', colormap=cmap)

ax.set_xlabel(None)
ax.set_ylabel('Seats')
ax.set_title('UK election results')

plt.show()