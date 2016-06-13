# -*- coding: utf-8 -*-


#te=np.arange(0,300,20)
#y=np.array([1007,905,877,769,688,512,501,499,400,385,360,287,255,200,199])

def func(te,s0,t2):
    import numpy as np
    return s0*np.exp(-te/t2)


def T2fit(t_value,y_value):
    import numpy as np
    import scipy as sp
    import matplotlib.pyplot as plt
    from scipy.optimize.minpack import curve_fit
    import StringIO

        
    if t_value and y_value:
            demo_data = 0
    else: #default value for testing
            t_value = "0 10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 " 
            y_value = "1.0 0.72 0.51 0.37 0.26 0.19 0.13 0.09 0.07 0.05 0.03 0.03 0.01 0.01 0.01 0.006 0.004 0.003 0.002 0.001 "
            demo_data = 1
      
    
    te =[float(xx) for xx in t_value.split()]
    y  =[float(xx) for xx in y_value.split()]
    #print te
    #print y

    
    te=np.array(te)
    y=np.array(y)
    #s=lambda s0,te,t2 :s0*np.exp(-te/t2) 
    #rv.getvalue()
    	
    popt, pcov = curve_fit(func, te, y)
    
    a=popt[0]
    b=popt[1]
    smoothx = np.linspace(te[0], te[-1], 100)
    smoothy = func(smoothx, a,  b)
    #fity=func(te,a,b)
    
    #print popt
    
    #plt.figure(1)
    #plt.clf()
    #plt.scatter(te,y, s=65, marker='+',c= 'k',label='Original')
    #plt.plot(te, fity,c= 'k',label='Fitted data')
    #fig = plt.gcf()
    #fig.set_size_inches(10,6)
    #plt.gca().grid(True)
    #plt.plot(te, y, '*',label='original values')
    #plt.plot(te, fity, 'r',label='curve_fit values')
    #rv = StringIO.StringIO()
    #plt.savefig(rv, format="svg")
    
#============================================================================================================
    HTML_text1 =''
    if demo_data:
        HTML_text1 += "<p><p><div class='alert alert-warning' role='alert'>No input data, using demo data set!</div>"
        
    HTML_text1 +=' <h4>T2 Fitting Model </h4>'
    HTML_text1 +="<p> $$ S(TE) =  {S_0e^{- \\frac{TE}{T_{2}}}}$$ "  #在兩個$$中間包住LATEX表示法的算式
    HTML_text1 += "The obtained T2 model are: S0= %.2f, T2 = %.2f ms<p>" % (a , b) 
    HTML_text1 += "<p> $$ S(TE) =  {%.2f e^{- \\frac{TE}{%.2f}}}$$" %  (a ,b )
    HTML_text1 += "<H4>Calculated T2: %.2f ms</H4><p>" % b 
    #========================================================================      
 
# prepare High Chart , Second block of the result page
#========================================================================
    HTML_text2 = "<p>TE values = %s" % t_value 
    HTML_text2 += "<p>SI values = %s" % y_value 
    HTML_text2 += "<H4>Provided by Chun-Yu Huang & Teng-Yi Huang</H4>"

    #HTML_text2 +="<p> fitting residue = %.2f<p>" % dict_T1fit_result ['residue']
        #print HTML
    import Plotting_lib 
    chart_title = 'T2 Fitting '
    xAxis_label = 'TE (ms)'
    yAxis_label = 'Signal Intensity (A.U.)'
    result_dict = {            
            'HTML_text1': HTML_text1,
            'HTML_text2': HTML_text2,
            'SVG':Plotting_lib.dynamic_svg(te,y,smoothx,smoothy,xAxis_label,yAxis_label,chart_title),
#================================
            'highchart':Plotting_lib.highchart(te,y,smoothx,smoothy,xAxis_label,yAxis_label,chart_title),

               }
    return result_dict


    
    
     
