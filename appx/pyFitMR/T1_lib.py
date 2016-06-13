
def T1fit(t_value, y_value):
    """T1 曲線擬合，t_value 為 TI 時間，y_value為信號強度"""
    import  numpy as np
    from scipy.optimize.minpack import curve_fit

    #import pyT1

   
    if t_value and y_value:
        demo_data = 0
    else: #default value for testing
        t_value = "120 220 370 1130 1168 1233 2115 2125 2145 3078 4035"
        y_value = "114 87 56 75 80 89 137 132 128 151 168"
        demo_data = 1

    t_value = np.array( [float(xx) for xx in t_value.split()])
    y_value = np.array([float(xx) for xx in y_value.split()])


    dict_T1fit_result =T1fit_iter(t_value,y_value)

    # prepare HTML_text1 , first block of the result page
    #========================================================================
    if dict_T1fit_result ['error_status']:
        result_dict = {    'HTML_text1': "<div class='alert alert-danger' role='alert'> %s </div> " %    dict_T1fit_result ['error_str']  }
        return result_dict  
  
    HTML_text1 =''
    if demo_data:
        HTML_text1 += "<p><p><div class='alert alert-warning' role='alert'>No input data, using demo data set!</div>"
        
    HTML_text1 +=' <h4>T1 Fitting Model for Inversion Recovery Experiment</h4>'
    HTML_text1 +="<p> $$ S(TI) =  S_0({1 - 2 e^{- \\frac{TI}{T_{1}^*}}})$$ "  #在兩個$$中間包住LATEX表示法的算式
    HTML_text1 += "The obtained T1 model are: S0 = %.2f,  T1 = %.2f ms<p>" % (dict_T1fit_result ['A'] , dict_T1fit_result ['T1'] )
    HTML_text1 += "<p> $$ S(TI) =  %.2f ({ 1 - 2 e^{- \\frac{TI}{%.2f}}})$$" %  (dict_T1fit_result ['A'] , dict_T1fit_result ['T1'] )
    HTML_text1 += "<H4>Calculated T1: %.2f ms</H4><p>" % dict_T1fit_result ['T1'] 
    #========================================================================      
 
# prepare High Chart , Second block of the result page
#========================================================================
    HTML_text2 =  "<p>t values = %s" % t_value 
    HTML_text2 += "<p>y values = %s" % y_value 
    HTML_text2 += "<p> fitting residue = %.2f<p>" % dict_T1fit_result ['residue']
    HTML_text2 += "<H4>Provided by Yi-Fu Tsai & Teng-Yi Huang</H4>"
    
        #print HTML
    import Plotting_lib
    chart_title = 'T1 fitting for Inversion-Recovery Experiment'
    xAxis_label = 'Inversion Time (ms)'
    yAxis_label = 'Signal Intensity (A.U.)'
    result_dict = {            
            'HTML_text1': HTML_text1,
            'HTML_text2': HTML_text2,
            'SVG':Plotting_lib.dynamic_svg(
                dict_T1fit_result ['t_val_org'],dict_T1fit_result ['y_val_org'],
                dict_T1fit_result ['t_val_fit'], dict_T1fit_result ['y_val_fit'],
                xAxis_label,yAxis_label,chart_title),
            'highchart':Plotting_lib.highchart(
                dict_T1fit_result ['t_val_org'],dict_T1fit_result ['y_val_org'],
                dict_T1fit_result ['t_val_fit'], dict_T1fit_result ['y_val_fit'],
                xAxis_label,yAxis_label,chart_title),
               }
    return result_dict




def T1fit_iter(t_value, y_value):
    """T1 曲線擬合，t_value 為 TI 時間，y_value為信號強度
        輸入值為兩個 numpy.ndarray
        t_value: 時間變數
        y_value:信號強度
        以下為參數回傳
        result_dict = {            
            'A': A,
            'B': B,
            'T1_star':t,
            'T1':T1,
            't_val_org':x,
            'y_val_org':y,
            't_val_fit':smoothx,
            'y_val_fit':smoothy,
            'residue':residue,
            'error_status':0,
            'error_str':'OK!',
          }
    
    """
    import numpy as np
    x=t_value
    y=y_value

    # setup initial value for test.
    if  not (len(x) and len(y)):
        dict_T1fit_result = {            
            'error_status':1,
            'error_str':'No input data',}
        return dict_T1fit_result

    if len(x) != len(y):
        dict_T1fit_result = {            
        'error_status':2,
        'error_str':'TI series & SI series is not mach',}
        return dict_T1fit_result

    #將 x做排序

    guessnum = np.array([100, 200, 500, 800, 1000, 1500, 2000, 2500])  #設定T1 起始值之猜測
    errornum = guessnum * 0
    t_order= x.argsort()
    x=x[t_order]
    y=y[t_order]
    
   #   使用不同的起始 T1 值去計算，再找出誤差最小的來使用
    result_list=['',]
    for index in range(len(guessnum)):
    
        guess = [y.max(), guessnum[index]]
        fit_result=T1fit_run(x,y,guess,abs_fit=1)
        errornum[index]  = fit_result['residue']
        if index == 0:
            result_list[0]=[fit_result,]
        else:
            result_list.append(fit_result)
   
    prerun_result=  result_list[np.argmin(errornum)] 
    
    #接下來去找出曲線翻轉  ，以前一次的結果當成初始值  
    index_ylow=np.argmin(y)
    count=-1
    result_list=[0,0,0] # 準備一個大小為3的list
    index_temp=[0,0,0]
    errornum=[0,0,0]
    for index in [index_ylow-1,index_ylow,index_ylow+1]:
        count +=1
        print index
        if index < 0 or index >=len(y):
            errornum[count]=1e8
            fit_result=prerun_result
        else:
            flipped_y=y.copy()
            flipped_y[:index+1]=-1*y[:index+1]
            guess = [prerun_result['A'], prerun_result['T1']]
            fit_result=T1fit_run(x,flipped_y,guess,abs_fit=0)
            errornum[count]  = fit_result['residue'] 
        print errornum[count]
        index_temp[count]=index
        result_list[count]=fit_result
        obtained_result_list=result_list[np.argmin(errornum)]

            


        
    
   # return  guessnum[np.argmin(errornum)]
    return obtained_result_list
    
def T1fit_run(x,y,guess,abs_fit):
    import numpy as np
    from scipy.optimize.minpack import curve_fit
    #t_order= x.argsort()
    #x=x[t_order]
    #y=y[t_order]
    
    #guess_a, guess_b, guess_c = y.max(), 2 * y.max(), T1_guess
    #guess = [guess_a, guess_b, guess_c]
    if abs_fit:
        exp_f = lambda x, A, t:abs((A - (2*A * np.exp(-x / t))))
    else:
        exp_f = lambda x, A, t:((A - (2*A * np.exp(-x / t))))
    params, cov = curve_fit(exp_f, x, y, p0=guess)
    A,  t = params
    #best_fit = lambda x: abs((A - (B * np.exp(-x / t))))
    smoothx = np.linspace(x[0], x[-1], 100)
    smoothy = exp_f(smoothx, A,  t)
    T1 = t            
    yfitting = exp_f(x, A, t)
    #yfitting = abs(A - (B * np.exp(-x / t)))
    residue=np.sum(abs(yfitting - y));
    result_dict = {            
            'A': A,
            'T1':T1,
            't_val_org':x,
            'y_val_org':y,
            't_val_fit':smoothx,
            'y_val_fit':smoothy,
            'residue':residue,
            'error_status':0,
            'error_str':'OK!',
          }
    return result_dict


