# -*- coding: utf-8 -*-


#te=np.arange(0,300,20)
#y=np.array([1007,905,877,769,688,512,501,499,400,385,360,287,255,200,199])

def Plot17(t_value):
    from django.template.loader import render_to_string
    import numpy as np
    #from django.template import RequestContext
    if t_value :
        demo_data = 0
        pass
    else: #default value for testing
        t_value = "120 220 0 125 95 50 10 7 8 69 115 256 97 229 150 13 71.6"
        demo_data = 1
    aha17 =np.array( [float(xx) for xx in t_value.split()])
    #aha17 =np.array(t_value.split())
    AHA17_dict={}
    #return render(request,'aha17.html')
    for ii in range(17):
        AHA17_dict['aha' + str(ii+1)] = rgb_code(aha17[ii],1)

    SVG_jet=render_to_string('app/aha17.html', AHA17_dict)

    #for ii in range(17):
     #   AHA17_dict['aha' + str(ii+1)] = rgb_code(aha17[ii],1)

    #SVG_cool=render_to_string('app/aha17.html', AHA17_dict)
       # context_instance = RequestContext(request, AHA17_dict))
    SVG_cool=dynamic_png(aha17)

    
#============================================================================================================
    HTML_text1 =''
    if demo_data:
        HTML_text1 += "<p><p><div class='alert alert-warning' role='alert'>No input data, using demo data set!</div>"
        
    HTML_text1 +=' <h4>Plotting AHA 17 </h4>'
    #HTML_text1 +="<p> $$ SI =  {S0e^{- \\frac{TE}{T_{2}}}}$$ "  #在兩個$$中間包住LATEX表示法的算式
    #HTML_text1 += "The obtained T2 model are: S0= %.2f, T2 = %.2f ms<p>" % (a , b) 
    #HTML_text1 += "<p> $$ SI =  {%.2f e^{- \\frac{TE}{%.2f}}}$$" %  (a ,b )
    #HTML_text1 += "<H4>LL corrected T2: %.2f ms</H4><p>" % b 
    #========================================================================      
 
# prepare High Chart , Second block of the result page
#========================================================================
    HTML_text2 = "<p>AHA 17 values = %s" % t_value 
    #HTML_text2 += "<p>y values = %s" % y_value 
    HTML_text2 += '<H4>Provided by Chun-Yu Huang  & Teng-Yi Huang</H4>'

    #HTML_text2 +="<p> fitting residue = %.2f<p>" % dict_T1fit_result ['residue']
        #print HTML
    result_dict = {            
            'HTML_text1': HTML_text1,
            'HTML_text2': HTML_text2,
            'SVG':SVG_jet,
#================================
            'highchart':SVG_cool,

               }
    return result_dict


    

    
def  rgb_code(i,cmap):
    '''cmap, 0: jet, 1:cool'''
    import matplotlib.pyplot as plt
    if cmap:
        rgba=plt.cm.cool(int(i))
    else:
        rgba=plt.cm.jet(int(i))
    red = int(rgba[0]*255)
    green = int(rgba[1]*255)
    blue = int(rgba[2]*255)
    return '{r:02x}{g:02x}{b:02x}'.format(r=red,g=green,b=blue)


def dynamic_png(aha17):
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
        # Create the fake data
    #data = np.array(range(17))*10 + 1
    
    
    # Make a figure and axes with dimensions as desired.
    fig=plt.figure(figsize=(9,8), dpi=600)

    #fig, ax = plt.subplots(figsize=(8,12),nrows=1, ncols=1,
    #                       subplot_kw=dict(projection='polar'))
    #fig.canvas.set_window_title('Left Ventricle Bulls Eyes (AHA)')
    
    # Create the axis for the colorbars
    ax = fig.add_axes([0.1, 1-8/9.+0.1, 8./9.*0.7, 1*0.7],projection='polar')
    axl = fig.add_axes([0.76, 0.3, 0.03, 0.5])
    #axl.set_aspect(1)
    #axl2 = fig.add_axes([0.41, 0.15, 0.2, 0.05])
    #axl3 = fig.add_axes([0.69, 0.15, 0.2, 0.05])
    
    
    # Set the colormap and norm to correspond to the data for which
    # the colorbar will be used.
    cmap = mpl.cm.jet
    norm = mpl.colors.Normalize(vmin=0, vmax=255)
    
    # ColorbarBase derives from ScalarMappable and puts a colorbar
    # in a specified axes, so it has everything needed for a
    # standalone colorbar.  There are many more kwargs, but the
    # following gives a basic continuous colorbar with ticks
    # and labels.
    cb1 = mpl.colorbar.ColorbarBase(axl, cmap=cmap, norm=norm,
                                    orientation='vertical')
    #cb1.set_label('A. U.')
    
   
    # Create the 17 segment model
    bullseye_plot(ax, aha17, cmap=cmap, norm=norm)
    #ax.set_title('Bulls Eye (AHA)')

    try:
        import StringIO
        #plt.title("Dynamic PNG")
        #for i in range(5): plt.plot(sorted(np.random.randn(25)))
        rv = StringIO.StringIO()
        plt.savefig(rv,dpi=200, format="png")
        plt.clf()
        return """<img src="data:image/png;base64,%s" style='max-width:100%%;height:auto;'/>""" % rv.getvalue().encode("base64").strip()
    finally:
        plt.clf()
    
    #plt.show()
    #plt.savefig('test.svg')


def bullseye_plot(ax, data, segBold=[], cmap=None, norm=None):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    """
    Bullseye representation for the left ventricle.

    Parameters
    ----------
    ax : axes
    data : list of int and float
        The intensity values for each of the 17 segments
    cmap : ColorMap or None
        Optional argument to set the disaried colormap
    norm : Normalize or None
        Optional argument to normalize data into the [0.0, 1.0] range
    segBold: list of int
        A list with the segments to highlight


    Notes
    -----
    This function create the 17 segment model for the left ventricle according
    to the American Heart Association (AHA) [1]_

    References
    ----------
    .. [1] M. D. Cerqueira, N. J. Weissman, V. Dilsizian, A. K. Jacobs,
        S. Kaul, W. K. Laskey, D. J. Pennell, J. A. Rumberger, T. Ryan,
        and M. S. Verani, "Standardized myocardial segmentation and nomenclature
        for tomographic imaging of the heart", Circulation, vol. 105, no. 4,
        pp. 539-542, 2002.
    """

    linewidth = 2
    data = np.array(data).ravel()

    if cmap is None:
        cmap = plt.cm.jet

    if norm is None:
        norm = mpl.colors.Normalize(vmin=data.min(), vmax=data.max())

    theta = np.linspace(0, 2*np.pi, 768)
    r = np.linspace(0.2, 1, 4)

    # Create the bound for the segment 17
    for i in range(r.shape[0]):
        ax.plot(theta, np.repeat(r[i], theta.shape), '-k', lw=linewidth)

    # Create the bounds for the segments  1-12
    for i in range(6):
        theta_i = i*60*np.pi/180
        ax.plot([theta_i, theta_i], [r[1], 1], '-k', lw=linewidth)

    # Create the bounds for the segmentss 13-16
    for i in range(4):
        theta_i = i*90*np.pi/180 - 45*np.pi/180
        ax.plot([theta_i, theta_i], [r[0], r[1]], '-k', lw=linewidth)

    # Fill the segments 1-6
    r0 = r[2:4]
    r0 = np.repeat(r0[:, np.newaxis], 128, axis=1).T
    for i in range(6):
        # First segment start at 60 degrees
        theta0 = theta[i*128:i*128+128] + 60*np.pi/180
        theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)
        z = np.ones((128, 2))*data[i]
        ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i+1 in segBold:
            ax.plot(theta0, r0, '-k', lw=linewidth+2)
            ax.plot(theta0[0], [r[2], r[3]], '-k', lw=linewidth+1)
            ax.plot(theta0[-1], [r[2], r[3]], '-k', lw=linewidth+1)

    # Fill the segments 7-12
    r0 = r[1:3]
    r0 = np.repeat(r0[:, np.newaxis], 128, axis=1).T
    for i in range(6):
        # First segment start at 60 degrees
        theta0 = theta[i*128:i*128+128] + 60*np.pi/180
        theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)
        z = np.ones((128, 2))*data[i+6]
        ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i+7 in segBold:
            ax.plot(theta0, r0, '-k', lw=linewidth+2)
            ax.plot(theta0[0], [r[1], r[2]], '-k', lw=linewidth+1)
            ax.plot(theta0[-1], [r[1], r[2]], '-k', lw=linewidth+1)

    # Fill the segments 13-16
    r0 = r[0:2]
    r0 = np.repeat(r0[:, np.newaxis], 192, axis=1).T
    for i in range(4):
        # First segment start at 45 degrees
        theta0 = theta[i*192:i*192+192] + 45*np.pi/180
        theta0 = np.repeat(theta0[:, np.newaxis], 2, axis=1)
        z = np.ones((192, 2))*data[i+12]
        ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if i+13 in segBold:
            ax.plot(theta0, r0, '-k', lw=linewidth+2)
            ax.plot(theta0[0], [r[0], r[1]], '-k', lw=linewidth+1)
            ax.plot(theta0[-1], [r[0], r[1]], '-k', lw=linewidth+1)

    #Fill the segments 17
    if data.size == 17:
        r0 = np.array([0, r[0]])
        r0 = np.repeat(r0[:, np.newaxis], theta.size, axis=1).T
        theta0 = np.repeat(theta[:, np.newaxis], 2, axis=1)
        z = np.ones((theta.size, 2))*data[16]
        ax.pcolormesh(theta0, r0, z, cmap=cmap, norm=norm)
        if 17 in segBold:
            ax.plot(theta0, r0, '-k', lw=linewidth+2)

    ax.set_ylim([0, 1])
    ax.set_yticklabels([])
    ax.set_xticklabels([])
