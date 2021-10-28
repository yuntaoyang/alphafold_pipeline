#!/usr/bin/env python
# coding: utf-8

# # Run AlphaFold using python script

# set up parameters

# In[16]:


logname = 'logfile_2080ti'
gpu = '8'
max_template_date = '2021-07-15'


# set up path

# In[17]:


path_input = '/home/yyang18/pipeline/alphafold/fasta/'
path_output = '/home/yyang18/pipeline/alphafold/out/'
path_log = '/home/yyang18/pipeline/alphafold/log/'
alphafold = '/home/yyang18/software/alphafold/docker/run_docker.py'


# In[18]:


import subprocess
import os
import logging


# step1: create the directory of log files and output

# In[19]:


os.mkdir(path_log)
os.mkdir(path_output)

# setp1: run alphafold

# In[20]:


files = os.listdir(path_input)


# In[21]:
logging.basicConfig(level=logging.DEBUG, 
                        filename=logname, 
                        filemode="a",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)
logging.info("alphafold start!")
for file in files:
    alphafold_run = 'python'+' '+alphafold+' '                '--fasta_paths'+' '+path_input+file+' '+                '--max_template_date='+max_template_date+' '+                '--gpu_devices'+' '+gpu+' '+                '--output_path='+path_output+' '+                '>'+' '+path_log+file.replace('.fasta','')+'.log'+' '+'2>&1'
    process = subprocess.Popen(alphafold_run,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    process.communicate()
    logging.info(file+" is done!")


# In[ ]:




