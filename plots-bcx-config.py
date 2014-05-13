#!/usr/bin/env python

# **************************************************
# ..................................................
# Barrier plots
# ..................................................
# **************************************************

# DESCRIPTION:
# Generate plots of differen MOPAC configurations
# for one species.

import sys

#---------------------------------------------------
plots = [
           # ------------------------------
           # Plot 1
           [
           'pm6-5.0-09',
           'pm6-5.0-12'
           ],
           # ------------------------------

       ] 
#---------------------------------------------------

if __name__ == "__main__":

    counter    = 0
    config_cnt = 0

    import os
    from os import path

    ls = os.listdir(os.getcwd())

    # Running over screening blocks.
    for plot in plots:

        block_name = "config-%s" % plot

        # Building up generic GNUPlot command string.
        block_gnus  = '' 
        block_gnus += 'set terminal postscript eps "Helvetica" 24\n'
        block_gnus += 'set output \"%s.eps\"\n' % block_name
        block_gnus += 'set key top right\n'
        block_gnus += 'set yrange[-18:34]\n'
        block_gnus += 'set xlabel "Interpolation Frame"\n'
        block_gnus += 'set ylabel "[kcal/mol]"\n'
        #block_gnus += 'plot "0000-WT.dat" title "WT" with linespoints lt 0 lc 0 lw 6 pt 0 ps 2,\\\n'
        block_gnuf = open(block_name + '.gnu', 'w') 
        print block_name

        # Initializing the plot option counter and block length counter to check
        # when to write last semicolon in GNUPlot instruction.
        plot_opt_cnt = 0
        block_len_cnt = 0

        # Running over available files and checking for compatibility.
        for f in ls:
            if len(f.split('-')) > 3:

                # Preparing condition and gnuplot label.
                mut_name = "+".join(["+".join(f.split('-')[1:4]), os.path.splitext(f.split('-')[4])[0]])
                mut_lbl  = "-".join(["-".join(f.split('-')[1:4]), os.path.splitext(f.split('-')[4])[0]])

                # Available plotting options.
                plot_opt = ['title \"%s\" with linespoints lt 1 lc 3 lw 4 pt 1 ps 2' % mut_lbl,
                            'title \"%s\" with linespoints lt 1 lc 2 lw 4 pt 2 ps 2' % mut_lbl,
                            'title \"%s\" with linespoints lt 1 lc 1 lw 4 pt 6 ps 2' % mut_lbl,
                            'title \"%s\" with linespoints lt 1 lc 4 lw 4 pt 4 ps 2' % mut_lbl,
                            'title \"%s\" with linespoints lt 1 lc 5 lw 4 pt 5 ps 2' % mut_lbl,
                            'title \"%s\" with linespoints lt 1 lc 7 lw 4 pt 7 ps 2' % mut_lbl]
                
                # For each mutant in the screening block.
                for mut in block: 
                    
                    # Is the current file equal to the current mutant from the screening block.
                    if mut_name == mut:

                        # Only consider '.dat' files.
                        if os.path.splitext(f)[1] == '.dat':

                            # Sanity check.
                            print mut, f

                            # Build up GNUPlot plot instruction and set next plot option.  
                            # Adding komma and backslash to all but last entry
                            # (abort before reaching last element).
                            if block_len_cnt < len(block)-1:
                                block_gnus += '\"%s\" %s,\\\n' % (f, plot_opt[plot_opt_cnt]) 
                                plot_opt_cnt += 1 
                                block_len_cnt += 1
                            else:
                                block_gnus += '\"%s\" %s;\n' % (f, plot_opt[plot_opt_cnt]) 
                                plot_opt_cnt += 1 

        # Write GNUPlot instruction file and return.
        block_gnuf.write(block_gnus)
        block_gnuf.close()
        counter += 1 
