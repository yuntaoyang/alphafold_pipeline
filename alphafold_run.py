#!/usr/bin/env python
# coding: utf-8

# # Run AlphaFold using python script

# set up parameters

# In[16]:


logname = 'logfile_2080ti'
gpu = '0,1'
max_template_date = '2021-07-15'


# set up path

# In[17]:


path_input = '/home/yyang18/project/alphafold_test/fasta/'
path_output = '/home/yyang18/project/alphafold_test/out/'
alphafold = '/home/yyang18/software/alphafold/docker/run_docker.py'


# In[18]:


import subprocess
import os
import logging


# step1: create the output directory of alphafold

# In[19]:


try:
    os.mkdir(path_output)
    logging.basicConfig(level=logging.DEBUG, 
                        filename=logname, 
                        filemode="a",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    logger = logging.getLogger(__name__)
    logger.info("create the output directory of alphafold: "+path_output)
except:
    logging.info("File exists: "+path_output)


# setp2: run alphafold

# In[20]:


files = os.listdir(path_input)


# In[21]:


logger.info("alphafold start!")
for file in files:
    alphafold = 'python'+' '+alphafold+' '                '--fasta_paths'+' '+path_input+file+' '+                '--max_template_date='+max_template_date+' '+                '--gpu_devices'+' '+gpu+' '+                '--output_path='+path_output+' '+                '>'+' '+path_output+file.replace('.fasta','')+'.log'+' '+'2>&1'
    process = subprocess.Popen(alphafold,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    process.communicate()
    logger.info(file+" is done!")


# In[ ]:




