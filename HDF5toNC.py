import glob
import subprocess
import os


outputfolder="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/Sample/IMERG-Comprehensive-V6/"
outpufiles=glob.glob(outputfolder+"*.HDF5")
outpufiles.sort() 

for file in outpufiles:
    Script='nccopy '+file+' '+file[:-5]+'.nc'
    subprocess.getstatusoutput(Script)
    os.remove(file)
    