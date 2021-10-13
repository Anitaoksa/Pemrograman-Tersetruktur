#importing the matplotlib library
importing matplotlib.pyplot as plt
#declaring the figure or the plot (y, x) or (weidht, height)
plt.figure(figsize=[14, 10])
# Passing the parameters to the bar function, this is the main function which creates the bar plot
# For creating the horizontal make sure that you append 'h' to the bar function name
plt.barh(['laki-laki'], [100], color = 'b')
plt.barh(['perempuan'], [150], color = 'g')
# Creating the legend of the bars in the plot
plt.legend()
# Namimg the x and y axis
plt.xlabel('jumlah')
plt.ylabel('gender')
# Giving the tilte for the plot
plt.title('Jumlah mahasiswa PTIK UNS')
# Displaying the bar plot
plt.show()
