
    set term dumb 80 24
    set boxwidth 0.5
    set style fill solid
    set xlabel 'Animal'
    set ylabel 'Estimated Population'
    set title 'Animals by Estimated Population'
    set datafile separator " "
    plot 'data.txt' using 2:xtic(1) with boxes
    pause -1
    