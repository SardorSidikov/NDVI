import csv
xs = []
ys = []
with open('ee-chart.csv') as f:
   csvreader = csv.reader(f)
   next(csvreader)
   for r in csvreader:
     xs.append(int(r[0]))
     ys.append(float(r[1]))
from matplotlib import pyplot as plt
import datetime
d0 = datetime.date(2017,1,1)
days = [d0 + datetime.timedelta(days=i-1) for i in xs]
import matplotlib.dates
dates = matplotlib.dates.date2num(days)
plt.clf()
plt.plot_date(dates,ys,'-')
plt.savefig('mytable2.png')