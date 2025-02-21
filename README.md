# My Forest Fire Analysis Project

### Prerequisite
1. VS Code (download from here: https://code.visualstudio.com/download). 
2. Python & IPython 
3. Git (good to have) (download from https://git-scm.com/downloads)

## Getting started 
1. install the vs code, ipython, and git (if not installed already). Also, please intall the following three extensions for a seamless experience
    - Jupyter
    - Python
    - IPython (incase in your system, IPython isn't installed, don't worry, when you run Jupyter Notebook commands, VSCode will ask you to install 
![Jupyter](https://github.com/user-attachments/assets/f12d69b5-2bec-414f-aa78-9ab99f5ddd43) ![python](https://github.com/user-attachments/assets/e6c42533-1099-4641-926f-5bd941f78266)
![IPykernel](https://github.com/user-attachments/assets/112f89ae-02cb-4b99-a8f3-50bf0e5f8af7)

If python, IPython is already in your system, then the IPython kernel might automatically be ready to work on your device. In case you need a video installation guide to start with the Jupyter Notebook in VSCode, this official video recommended. Please check this video https://youtu.be/suAkMeWJ1yE 

2. In case IPython isn't in the system, it can also be installed from the terminal in VS Code
  Steps: 
    - open VS Code
    - write ```pip install ipython``` and press enter
    - just to be sure, check the version once installed with ```ipython --version```
  
3. Check the python env set for the kernel
    ![python for kernel](https://github.com/user-attachments/assets/a5391f17-3568-40a1-99c8-84c21aa3b687)

2. move to your preferred project working directory (PWD) folder
3. right click and find Open Git Bash here

   ![git bash](https://github.com/user-attachments/assets/098c8cdc-e04f-4a85-8eb0-31fd3e74f6c0)
   
5. on the pop-up window type ```git clone https://github.com/manzim/CA_Fire_Impact_Analysis.git``` and press enter
   ![git clone from repo](https://github.com/user-attachments/assets/7a906807-1689-4395-90f4-38d20192bce9)
   ![should look like this after cloning](https://github.com/user-attachments/assets/94db189f-bd5e-4507-8121-d67d56de662f)

  Travel to the downloaded folder like shown in the screenshot
  
5. Download shouldn't take long, please check "Dataset, Scripts, resources, gitignore, README.md" files are there
6. Skip step 4,5 if you already have the repository, From Download ZIP (seen on step 4 screenshot), download the zipped folder and extract it in your PWD.
7. Ensure once again that you're inside ```CA_Fire_Impact_Analysis``` folder and right click again to select either of them (marked in red rectangle)

![image](https://github.com/user-attachments/assets/62e3c87d-7f8f-476f-a0de-adc195e4f549)

8. write ```code .``` and press enter (then the folder should open in VS code) 
![open with code .](https://github.com/user-attachments/assets/02de1040-34e2-46f9-9145-6b1cca1f1f40)
or Alternatively you can open this from inside the VS Code > Open Folder...
here's the screenshot for inside vs code
![open the pwd folder](https://github.com/user-attachments/assets/e7cda804-4b68-454e-bc14-5318cf5a166d)
9. open the **install_requirement.ipynb** file at first and run the only (python) code cell ```!pip install -r dependencies.txt```
10. To test everything you can run the initialCommit.ipynb file
11. If there is no problem till step 10, then all the scripts should be runnable now.
12. It's recommended to start with the following sequence
  - install_requirement.ipynb
  - initialCommit.ipynb
  - dataset_loader_function.py (no need to run, just open and save the file)
  - dataset_time_series_analysis.ipynb
  - any other remaining files

#### **N.B:** Two things to keep in mind
1. Sometimes the dataset might not load, whenever, a change happens in the ".py" file, then it doesn't automitically update itself. In this case the kernel has to be killed and restart again or close the VS Code and open again
2. For the interactive plot, widgets have been used. Hence, there is a good chance, that these interactive plot codes might not work in another interface or compiler. If it doesn't run on this project scripts too, then please kindly open a python cell and run this code ```pip install ipympl```. 


