
import matplotlib.pyplot as plt

years2=[1999,2000,2001,2002,2003,2004,2005,2006,2007,2008]
kohli2=[1000,1500,1350,890,1400,2050,956,1600,1100,1350]
rohit2=[1340,750,1550,1150,1250,950,1110,1200,1340,1450]
sehwag2=[1157,800,1000,1600,1350,1400,900,1100,1500,1645]

plt.plot(years2,kohli2,color="red",linestyle=":",marker="o",label="Virat kohli")
plt.plot(years2,rohit2,color="blue",linestyle="--",marker="*",label="Rohit sharma")
plt.plot(years2,sehwag2,color="green",linestyle="-",marker=">",label="sehwag")

plt.xlabel("Years")
plt.ylabel("Run score")
plt.title("Comparing run score of player , past 10 years")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()