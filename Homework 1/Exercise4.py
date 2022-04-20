# Exercise4.py
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

def random_walk(steps, self_avoiding=False):
    x = np.zeros(steps)
    y = np.zeros(steps)
    distance = np.zeros(steps)

    loop_stationary = 0 # variable counting loop cycles walker has not moved
    max_stationary = 10

    if self_avoiding:
        i = 1
        #new_x = 0
        #new_y = 0
        while i < steps:
            # if it is stuck set rest to last location
            if loop_stationary >= max_stationary:
                x[i] = x[i-1]
                y[i] = y[i-1]
                i = i + 1

            random_var = rand()
            if random_var < .25:
                new_x = x[i-1]+1
                new_y = y[i-1]
                continue
            if random_var < .5:
                new_x = x[i-1]
                new_y = y[i-1]+1
                continue
            if random_var < .75:
                new_x = x[i-1]-1
                new_y = y[i-1]
                continue
            if random_var >= .75:
                new_x = x[i-1]
                new_y = y[i-1]-1
            # check if walker has been there before
            has_been_there = False
            for j in range(0, i+1):
                if new_x == x[j] and new_y == y[j]:
                    has_been_there = True
                    break
                #endif
            #endfor
            if has_been_there:
                loop_stationary = loop_stationary + 1
                continue
            else:
                x[i] = new_x
                y[i] = new_y
                loop_stationary = 0

            i = i + 1
        #endwhile
        distance = np.sqrt(np.power(x, 2) + np.power(y,2))
        return x,y, distance
    #endif


    for i in range(1,steps):
        random_var = rand()
        if random_var < .25:
            x[i] = x[i-1]+1
            y[i] = y[i-1]
            continue
        if random_var < .5:
            x[i] = x[i-1]
            y[i] = y[i-1]+1
            continue
        if random_var < .75:
            x[i] = x[i-1]-1
            y[i] = y[i-1]
            continue
        x[i] = x[i-1]
        y[i] = y[i-1]-1
        
    distance = np.sqrt(np.power(x, 2) + np.power(y,2))
    return x,y, distance

# plotting many walks
def plot_walks(amount_plots, steps, self_avoiding=False):
    for i in range(0, amount_plots):
        x, y, distance = random_walk(steps, self_avoiding=self_avoiding)
        plt.plot(x,y, alpha=.5)
        
walks = 8
steps = 1000
plot_walks(walks, steps)
plt.tight_layout()
plt.savefig('build/many_walks.pdf')

plt.clf()

def distance_average(walks, steps, self_avoiding=False):
    data = np.zeros((walks, steps))
    for i in range(0, walks):
        x,y, data[i, :] = random_walk(steps, self_avoiding=self_avoiding)
    average = np.mean(data, axis=0)
    return average

walks = 1000
steps = 1000
dist = distance_average(walks, steps)

t = np.arange(1,steps,1)
plt.plot(t, dist[1:], label='Walk distance')
plt.plot(t, np.sqrt(t), label=rf'sqrt(steps)')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('# of steps')
plt.ylabel('Distance / length unit')
#plt.title(f'Distance averaged over {walks} walks')

plt.legend()
plt.tight_layout()

plt.savefig('build/Steps-Distance.pdf')
 
# now self avoiding
walks = 1
steps = 100

plt.clf()
dist = distance_average(walks, steps, self_avoiding=True)

t = np.arange(1,steps,1)
plt.plot(t, dist[1:], label='Walk distance')
plt.plot(t, np.sqrt(t), label=rf'sqrt(steps)')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('# of steps')
plt.ylabel('Distance / length unit')
#plt.title(f'Distance averaged over {walks} walks')

plt.legend()
plt.tight_layout()

plt.savefig('build/Steps-Distance-SAW.pdf')
