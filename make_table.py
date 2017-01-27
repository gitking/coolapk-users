import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


r = mlab.csv2rec('users1.csv')

ind = np.arange(len(r))  

fig = plt.figure()
ax = fig.add_subplot(111)


ax.plot(ind, r['dt'], 'o' ,label='feed',c='b')
ax.set_title("Feed of Coolapk.com    by unnamed5719")
ax.legend(loc='upper right')
plt.savefig("Feed.png")

ind = np.arange(len(r))  

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(ind, r['yy'], 'o' ,label='apk',c='g')
ax.set_title("Apk of Coolapk.com    by unnamed5719")
ax.legend(loc='upper right')
plt.savefig("Apk.png")

ind = np.arange(len(r))  

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(ind, r['fx'], 'o' ,label='faxian',c='r')
ax.set_title("Faxian of Coolapk.com    by unnamed5719")
ax.legend(loc='upper right')
plt.savefig("Faxian.png")

ind = np.arange(len(r))  

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(ind, r['fs'], 'o' ,label='contacts',c='c')
ax.set_title("Contacts of Coolapk.com    by unnamed5719")
ax.legend(loc='upper right')
plt.savefig("Contacts.png")