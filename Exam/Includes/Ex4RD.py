<<<<<<< HEAD
\section{Smoothing Data}

Load data \textit{XYShirase\_GPS\_Small.txt}. This datafile was recoreded by a GPS station on an Antarctica Ice shelf. The data structure is as follows:\\

col1: coordinate polar stereographic East (m)\\
col2: coordinate polar stereographic South (m)\\
col3: coordinate longitude (decimal degrees)\\
col4: coordinate latitude (decimal degrees)\\
col5: elevation (m, relative to WGS84)\\
col6: days (relative to an arbitrary date in the past)\\

Visualize the vertical displacement as a function of time. The data are a bit noisy for your liking. Smooth the data with a running mean. This means, write a for loop that goes through the data and for each point in time you average values in its surrounding. This is called a running mean. It is not the best way to smooth data, but a good exercises. Write your own loop, don't use external functions. 
=======
\section{Derivative}

The data given is from one year (2018) of the weather station in Santa Gracia.
There are 24 values per day (1 hour average).

\begin{itemize}
    \item Read in the CSV file \verb|"data4.csv"|. (use \verb|np.loadtxt()|, \verb|delimiter=","| and \verb|usecols=(1,2)|)
    \item Write a function that filters out the invalid values (-9999.0) from the data.
    \item Write a function that calculates the first and second derivative.
    \item Plot the data: first column contains the average wind speed, second column contains the maximum wind speed.
\end{itemize}
>>>>>>> d8276dd13fdaf5a3606101c1a41ce2dfdb879da4
