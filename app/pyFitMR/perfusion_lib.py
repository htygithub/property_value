# -*- coding: utf-8 -*-


#te=np.arange(0,300,20)
#y=np.array([1007,905,877,769,688,512,501,499,400,385,360,287,255,200,199])

def func(x, C0, r, b):
    import numpy
    return C0*(x**r)*numpy.exp(-(x*b))


def perfusionfit(t_value,y_value):
    import numpy as np
    import scipy as sp
    import matplotlib.pyplot as plt
    from scipy import integrate
    from scipy.optimize.minpack import curve_fit
    import StringIO

        
    if t_value and y_value:
            demo_data = 0
    else: #default value for testing
            t_value = "0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14. 15.  16.  17.  18.  19.  20.  21.  22.  23.  24.  25.  26.  27.  28.  29. 30.  31.  32.  33.  34.  35.  36.  37.  38.  39.  40.  41.  42.  43.  44. 45.  46.  47." 
            y_value = "5.   4.   7.   0.   3.   1.   5.   3.   7.   4.  2. 4.   8.   8.  10.  16.  22.  30.  37.  46.  56.  55. 54.  54.  57.  50.  42.  44.  44.  37.  31.  25.  23. 22.  29.  29.  25.  35.  39.  42.  34.  32.  37.  24. 15.  17.  16.  19."
            demo_data = 1
      
    
    te =[float(xx) for xx in t_value.split()]
    y  =[float(xx) for xx in y_value.split()]
    #print te
    #print y

    
    te=np.array(te)
    y=np.array(y)
    #s=lambda s0,te,t2 :s0*np.exp(-te/t2) 
    #rv.getvalue()
    yc=np.array(y)

    

    #baseline
    baseline = np.mean(y[0:5],axis=0)

    i=0
    check=0
    for i in range(48):
        if((yc[i]<(baseline+10)) and (check!=1)):
            first = i
            check=0
            yc[i]= baseline
            
        elif((yc[i]>=(baseline+10)) and (check!=1)):
            first = i
            check=1
            yc[i]= yc[i]
        else:
            yc[i]= yc[i]

    yc=yc-baseline


    
    #濾除second pass
    '''i=0
    for i in range(48):
        if(i>(np.argmax(y)+3)):
            yc[i]=0'''
    endpoint=np.argmax(y)+3        

     


    popt, pcov = curve_fit(func, te[first-1:endpoint]-te[first-1], yc[first-1:endpoint])
    
    a=popt[0]
    b=popt[1]
    c=popt[2]
    smoothx = np.linspace(te[0], te[-1], 100)
    smoothy = func(smoothx, *popt)

    smoothx = smoothx + te[first-1]
    smoothy = smoothy + baseline

    smoothx=np.insert(smoothx,0,0)
    smoothy=np.insert(smoothy,0,baseline)




    #padzeros= np.linspace(0, te[0], 100)


    #rBV    
    GammaF = lambda x: popt[0]*x**popt[1]*np.exp(-x*popt[2])   
       
    rBV = integrate.quad(GammaF, 0, np.inf)[0]

    #print (rBV)

    #MTT    
    GammaF2 = lambda x: x*(popt[0]*x**popt[1]*np.exp(-x*popt[2]))  
    
    rMTT = integrate.quad(GammaF2, 0, np.inf)[0] / rBV

    rBF = rBV/rMTT


    #血流 
    #print (np.max(smoothy))


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
        
    HTML_text1 +=' <h4>Model of Gamma Fitting</h4>'
    HTML_text1 +="<p> $$ S(T) =  {C_0t^re^{-tb}}$$ "  #在兩個$$中間包住LATEX表示法的算式
    HTML_text1 += "The obtained perfusion model are: C0 = %.2f, r = %.2f, b = %.2f <p>" % (a , b , c) 
    HTML_text1 +="<p> $$ S(T) = {%.2f t^{%.2f}e^{-t%.2f}}$$ " % (a , b , c)
    HTML_text1 += "<H4>Calculated rMTT: %.2f </H4><p>" % (rMTT) 
    HTML_text1 += "<H4>Calculated rBV: %.2f </H4><p>" % (rBV) 
    HTML_text1 += "<H4>Calculated rBF: %.2f </H4><p>" % (rBF)
     
    #========================================================================      
 
# prepare High Chart , Second block of the result page
#========================================================================
    HTML_text2 = "<p>T values = %s" % t_value 
    HTML_text2 += "<p>SI values = %s" % y_value 
    HTML_text2 += "<H4>Provided by Yi-Fu Tsai & Teng-Yi Huang</H4>"

    #HTML_text2 +="<p> fitting residue = %.2f<p>" % dict_T1fit_result ['residue']
        #print HTML
    import Plotting_lib 
    chart_title = 'perfusion Fitting '
    xAxis_label = 'T (Sec)'
    yAxis_label = 'Signal Intensity (A.U.)'
    result_dict = {            
            'HTML_text1': HTML_text1,
            'HTML_text2': HTML_text2,
            'SVG':Plotting_lib.dynamic_svg2(te,y,smoothx,smoothy,xAxis_label,yAxis_label,chart_title),
#================================
            'highchart':Plotting_lib.highchart(te,y,smoothx,smoothy,xAxis_label,yAxis_label,chart_title),

               }
    return result_dict


    
    
     
