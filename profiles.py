#!/usr/bin/python

# -> $HOME/scripts_model_generation/analyse.py

# NOTE:
# - Extracts and presents the data from the 'spe.arc' files
# - Generates a profile graph.

# REQUIRES:
# - grep -i "heat" ./*spe-*arc > data.txt

# CALLING SEQUENCE:
# $ python ./profiles data.txt 

import sys
dat=open(sys.argv[1], 'r')
val=dat.readlines()
dat.close()

# **************************************************
# Register the variants.
def register():
    for line in val: 
        name = get_name(line)
        if name not in names:
            names.append(name) 
    # Highest order multiple variants first.
    names.sort(key=len, reverse=True)

def get_name(line):
    # Discarding '1-3-' part.
    name = line.split()[0]
    name = name.split('-')[3:-1]
    name = '-'.join(name) 
    return name 

def get_x_range(name, counter):
    data = open('%04i-' % counter + name + '.dat', 'r')
    valu = data.readlines() 
    e_tmp = get_energy(name)
    return eval(min(e_tmp))-2, eval(max(e_tmp))+2 

def get_energy(name):
    energy = []
    for frame in val:
        if get_name(frame) == name:
            energy.append(frame.split()[5])
    return energy 
# --------------------------------------------------


# **************************************************
def write_dat(name, counter):
    gnu_dat = open('%04i-' % counter + name + '.dat' , 'w')
    energy = get_energy(name)
    e0 = energy[0]
    for e in energy:
        gnu_dat.write(str(eval(e)-eval(e0)) + '\n') 
    gnu_dat.close() 

def write_gnu(name, counter):
    gnus  = 'set terminal postscript eps \"Helvetica\" 24\n'
    gnus += 'set output \'%04i-%s.eps\'\n' % (counter, name)
    gnus += 'set key left top\n'
    gnus += 'set xrange[0:11]\n'
    gnus += 'set yrange[-20:20]\n'
    e0 = get_energy(name)[0]
    x_min, x_max = get_x_range(name, counter)
    #gnus += 'set xrange[%s:%s]\n' % (str(x_min),str(x_max))
    gnus += 'plot \'' + '%04i-' % counter + name + '.dat' + '\' title "%s" with lines lw 4\n'%name
    gnus += 'set output\n'

    gnuf  = open('%04i-' % counter + name + '.gnu', 'w') 
    gnuf.write(gnus)
    gnuf.close()
# --------------------------------------------------


# **************************************************
# LAUNCH PART
if __name__ == '__main__':
    
    # Get the available variants and store them in 'names'.
    names = [] 
    names.sort(key=len)
    register() 
    stop = 3
    
    name_len  = 0.0
    counter = 0
    for n in names:
        print n
        write_dat(n, counter)
        write_gnu(n, counter)
        counter += 1
# --------------------------------------------------
