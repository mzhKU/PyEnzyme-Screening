#!/usr/bin/env python

# **************************************************
# ..................................................
# Screening plots.
# ..................................................
# **************************************************

# DESCRIPTION:
# Generate plots used in screening.

import sys

vars = [
      
           # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
           # FOUR FOLD MUTANTS
           # WT is added in global GNUPlot command string.
           # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

           [
           'G39A+T103G+W104F+A141N',
           'G39A+T103G+W104F+A141Q'
           ],

           [
           'G39A+T103G+W104F+I189A',
           'G39A+T103G+W104F+I189N',
           'G39A+T103G+W104F+I189Y'
           ],

           [
           'G39A+T103G+W104F+L278A',
           'G39A+T103G+W104Q+L278A',
           'G39A+T103G+W104Y+L278A'
           ],

           [
           'G39A+T103G+W104Q+A141N',
           'G39A+T103G+W104Q+A141Q'
           ],

           [
           'G39A+T103G+W104Q+I189A',
           'G39A+T103G+W104Q+I189N',
           'G39A+T103G+W104Q+I189Y'
           ],

           [
           'G39A+T103G+W104Y+A141N',
           'G39A+T103G+W104Y+A141Q'
           ],

           [
           'G39A+T103G+W104Y+I189A',
           'G39A+T103G+W104Y+I189N',
           'G39A+T103G+W104Y+I189Y'
           ],

           [
           'G39A+W104F+A141N+I189A',
           'G39A+W104F+A141N+I189N',
           'G39A+W104F+A141N+I189Q'
           ],

           [
           'G39A+W104F+A141Q+I189A',
           'G39A+W104F+A141Q+I189N',
           'G39A+W104F+A141Q+I189Q'
           ],

           [
           'G39A+W104Q+A141N+I189A',
           'G39A+W104Q+A141N+I189N',
           'G39A+W104Q+A141N+I189Q'
           ],

           [
           'G39A+W104Q+A141Q+I189A',
           'G39A+W104Q+A141Q+I189N',
           'G39A+W104Q+A141Q+I189Q'
           ],

           [
           'G39A+W104Y+A141N+I189A',
           'G39A+W104Y+A141N+I189N',
           'G39A+W104Y+A141N+I189Q'
           ],

           [
           'G39A+W104Y+A141Q+I189A',
           'G39A+W104Y+A141Q+I189N',
           'G39A+W104Y+A141Q+I189Q'
           ],

           [
           'G39A+W104F+A141N+L278A',
           'G39A+W104F+A141Q+L278A'
           ],

           [
           'G39A+W104Q+A141N+L278A',
           'G39A+W104Q+A141Q+L278A'
           ],

           [
           'G39A+W104Y+A141N+L278A',
           'G39A+W104Y+A141Q+L278A'
           ],

           [
           'G39A+A141N+I189A+L278A',
           'G39A+A141N+I189N+L278A',
           'G39A+A141N+I189Q+L278A'
           ],

           [
           'G39A+A141Q+I189A+L278A',
           'G39A+A141Q+I189N+L278A',
           'G39A+A141Q+I189Q+L278A'
           ],
           
           [
           'T103G+W104F+A141N+I189A',
           'T103G+W104F+A141N+I189N',
           'T103G+W104F+A141N+I189Q'
           ],

           [
           'T103G+W104Q+A141N+I189A',
           'T103G+W104Q+A141N+I189N',
           'T103G+W104Q+A141N+I189Q'
           ],

           [
           'T103G+W104Y+A141N+I189A',
           'T103G+W104Y+A141N+I189N',
           'T103G+W104Y+A141N+I189Q'
           ],

           [
           'T103G+W104F+A141Q+I189A',
           'T103G+W104F+A141Q+I189N',
           'T103G+W104F+A141Q+I189Q'
           ],

           [
           'T103G+W104Q+A141Q+I189A',
           'T103G+W104Q+A141Q+I189N',
           'T103G+W104Q+A141Q+I189Q'
           ],

           [
           'T103G+W104Y+A141Q+I189A',
           'T103G+W104Y+A141Q+I189N',
           'T103G+W104Y+A141Q+I189Q'
           ],

           [
           'T103G+A141N+I189A+L278A',
           'T103G+A141N+I189N+L278A',
           'T103G+A141N+I189Q+L278A'
           ],

           [
           'T103G+A141Q+I189A+L278A',
           'T103G+A141Q+I189N+L278A',
           'T103G+A141Q+I189Q+L278A'
           ],

           [
           'W104F+A141N+I189A+L278A',
           'W104F+A141N+I189N+L278A',
           'W104F+A141N+I189Q+L278A'
           ],

           [
           'W104Q+A141N+I189A+L278A',
           'W104Q+A141N+I189N+L278A',
           'W104Q+A141N+I189Q+L278A'
           ],

           [
           'W104Y+A141N+I189A+L278A',
           'W104Y+A141N+I189N+L278A',
           'W104Y+A141N+I189Q+L278A'
           ],

           [
           'W104F+A141Q+I189A+L278A',
           'W104F+A141Q+I189N+L278A',
           'W104F+A141Q+I189Q+L278A'
           ],

           [
           'W104Q+A141Q+I189A+L278A',
           'W104Q+A141Q+I189N+L278A',
           'W104Q+A141Q+I189Q+L278A'
           ],

           [
           'W104Y+A141Q+I189A+L278A',
           'W104Y+A141Q+I189N+L278A',
           'W104Y+A141Q+I189Q+L278A'
           ]
           # ------------------------------

       ] 
#---------------------------------------------------

if __name__ == "__main__":

    counter = 0
    mut_cnt = 0

    import os
    from os import path

    ls = os.listdir(os.getcwd())

    # Running over screening blocks.
    for block in vars: 

        block_name = "block-%02d" % counter 

        # Building up generic GNUPlot command string.
        block_gnus  = '' 
        block_gnus += 'set terminal postscript eps "Helvetica" 24\n'
        block_gnus += 'set output \"%s.eps\"\n' % block_name
        block_gnus += 'set key top right\n'
        block_gnus += 'set yrange[-18:34]\n'
        block_gnus += 'set xlabel "Interpolation Frame"\n'
        block_gnus += 'set ylabel "[kcal/mol]"\n'
        block_gnus += 'plot "0000-WT.dat" title "WT" with linespoints lt 0 lc 0 lw 6 pt 0 ps 2,\\\n'
        block_name = "block-%02d" % counter 
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
