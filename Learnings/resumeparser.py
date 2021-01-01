from resume_parser import resumeparse
import os
import warnings

warnings.simplefilter('ignore')
path='C:/Users/91884/Desktop/OCR_Resume/OCR_Resume/'
resumes = os.listdir(path)
c=0
try:
    for i in range(8,10):
        print(resumes[i])
        data = resumeparse.read_file(f'{path}{resumes[i]}')
        print(data['skills'])
        c+=1
    
except:
    pass
print(c)
print(len(resumes)+1-9)
#8
