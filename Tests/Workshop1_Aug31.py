# Calculate people's volume!

ro = 985 # average density of a human being in kg/m3

# m = (ro)*V

name1 = 'Hasmik'
mass1 = 60 #kg

name2 = 'Ara'
mass2 = 70 #kg

name3 = 'Lilith'
mass3 = 80 #kg

name4 = 'Levon'
mass4 = 90 #kg

def vol_calculator(name, mass, r):
    volume = mass / r
    # return volume
    print(name + ' ' + 'volume = {}'.format(volume))

vol_calculator(name1, mass1, ro)
vol_calculator(name2, mass2, ro)
vol_calculator(name3, mass3, ro)
vol_calculator(name4, mass4, ro)



# define a function that will return dy/dt

def model(y, t):
    a = 0.3
    dydt = -a*y
    return dydt

# initial condition
y0 = 5

# time vector
t = np.linspace(0, 100, 2000)

# Solve ODE
y = odeint(model, y0, t)

# Plot
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
