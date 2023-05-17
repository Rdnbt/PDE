{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"pygments_lexer":"ipython3","nbconvert_exporter":"python","version":"3.6.4","file_extension":".py","codemirror_mode":{"name":"ipython","version":3},"name":"python","mimetype":"text/x-python"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-08-04T19:48:30.633299Z\",\"iopub.execute_input\":\"2021-08-04T19:48:30.633938Z\",\"iopub.status.idle\":\"2021-08-04T19:48:30.640589Z\",\"shell.execute_reply.started\":\"2021-08-04T19:48:30.633889Z\",\"shell.execute_reply\":\"2021-08-04T19:48:30.639640Z\"}}\nfrom IPython.display import HTML\nfrom base64 import b64encode\n\ndef play(filename):\n    html = ''\n    video = open(filename,'rb').read()\n    src = 'data:video/mp4;base64,' + b64encode(video).decode()\n    html += '<video width=1000 controls autoplay loop><source src=\"%s\" type=\"video/mp4\"></video>' % src \n    return HTML(html)\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-08-04T19:48:30.714357Z\",\"iopub.execute_input\":\"2021-08-04T19:48:30.714930Z\",\"iopub.status.idle\":\"2021-08-04T19:49:38.907036Z\",\"shell.execute_reply.started\":\"2021-08-04T19:48:30.714895Z\",\"shell.execute_reply\":\"2021-08-04T19:49:38.905887Z\"}}\nimport numpy as np\nimport matplotlib.pyplot as plt\n# Initial and given conditions\nd = 0.1\nalpha = 0.7\ndx = 0.1\nlen_x = 10.0\nlen_y = 10.0\ndt = d*(dx**2)/alpha\nend_time = 2.0\n\n\nx = np.arange(0.0, len_x+dx, dx)   # number of grids, different points of x\ny = np.arange(0.0, len_y+dx, dx)   # necessary to creat two dimentional space\n\nX, Y = np.meshgrid(x,y)\n# We will specify location afterwards\n\nT = np.zeros_like(X)  # initially the T is zero\n\nG = 0.0 \n\nT[:,0] = 10.0\nT[:,-1] = 10.0\nT[0,:] = T[0,:] +d*(T[1,:]-4.0*T[0,:]+T[1,:]-2.0*dx*G+np.roll(T[0,:],-1,axis=0)+np.roll(T[0,:],1,axis=0))\nT[-1,:] = 20.0\nT[10:20,45:50] = 60.0\n\n\nplt.figure(figsize=(20,20)) \nicounter = -1\nfor it in np.arange(0.0,end_time+dt, dt):\n    #if it ==0.0:\n    \n    icounter = icounter + 1\n    if np.mod(icounter,15)==0:\n        ax = plt.axes(projection='3d')\n        p = ax.scatter(X,Y,T, c=T, cmap='plasma', vmin = 0.0, vmax = 60.0)\n        ax.set_xlabel('X',fontsize = 20)\n        ax.set_ylabel('Y',fontsize = 20)\n        ax.set_zlim([0.0,60.0])\n        plt.colorbar(p)\n        plt.title('Time=%.6f'%(it),fontsize = 20)\n        plt.savefig('%06.6d.jpg'%(icounter))\n        plt.cla()\n        plt.clf()\n        \n    # T needs to be adjusted since it is not cyclic anymore. \n    # This is to prevent the cycling inside itself\n    # The reason not use roll function for the other axis is \n    # because the Neumann boundary condition is no longer connected to the other side. \n    # Hence we cannot use the roll function in the direction we implement Neumann boundary condition.\n    T[1:-1,:] = T[1:-1,:] + d*(np.roll(T[1:-1,:],-1,axis=1)+np.roll(T[1:-1,:],1,axis=1)+T[2:,:]+T[0:-2,:] - 4.0*T[1:-1,:])\n    T[:,0] = 10.0\n    T[:,-1] = 10.0\n    T[0,:] = T[0,:] +d*(T[1,:]-4.0*T[0,:]+T[1,:]-2.0*dx*G+np.roll(T[0,:],-1,axis=0)+np.roll(T[0,:],1,axis=0))\n    T[-1,:] = 20.0 \n    T[10:20,45:50] = 60.0\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-08-04T19:49:38.908361Z\",\"iopub.execute_input\":\"2021-08-04T19:49:38.908652Z\",\"iopub.status.idle\":\"2021-08-04T19:49:44.058292Z\",\"shell.execute_reply.started\":\"2021-08-04T19:49:38.908626Z\",\"shell.execute_reply\":\"2021-08-04T19:49:44.057124Z\"}}\n!rm *.mp4\n!ffmpeg -r 15 -pattern_type glob -i '/kaggle/working/*.jpg' -vf \"scale=trunc(iw/2)*2:trunc(ih/2)*2\" -vcodec libx264 -pix_fmt yuv420p Neumann.mp4\n!rm *.jpg\n\n# %% [code] {\"execution\":{\"iopub.status.busy\":\"2021-08-04T19:49:44.060395Z\",\"iopub.execute_input\":\"2021-08-04T19:49:44.060699Z\",\"iopub.status.idle\":\"2021-08-04T19:49:44.111370Z\",\"shell.execute_reply.started\":\"2021-08-04T19:49:44.060669Z\",\"shell.execute_reply\":\"2021-08-04T19:49:44.110025Z\"}}\nplay('/kaggle/working/Neumann.mp4')","metadata":{"_uuid":"29a3a3ba-d2dc-4b12-95f5-8accc25c478a","_cell_guid":"8fb4398b-9a95-4fc3-9661-02a9ff0b0a86","collapsed":false,"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]}]}