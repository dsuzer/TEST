import streamlit as st
import os, glob
import pickle


st.title("ABSA TOOL - DSUZER")
uploaded_file = st.file_uploader('UPLOAD FILE')
if uploaded_file is not None:
	with open('data/test20/upload_test.txt', 'w+') as txt_uploader:
		txt_uploader.write(str(uploaded_file.read()))
	st.write('File successfully uploaded.')


with open('data/test20/test.txt', 'w+') as txt_reader:
	string = st.text_input('ENTER TEXT', value='', max_chars=None, key=None, type='default')
	step1 = string.split()
	step2 = ' '.join([w + '=O' for w in step1])
	final = ''.join(string+'####'+step2)
	txt_reader.write(final)


if st.button('PROCESS'):
	st.header('Process started.')
	os.system("sh work.sh")
	filename = 'output_dict'
	infile = open(filename,'r+')
	output_dict = pickle.load(infile)
	st.write(output_dict)
	infile.close()
	st.header('Process finished.')





#for filename in glob.glob("data/test20/test.txt"):
#	os.remove(filename)

#for filename in glob.glob("data/test20/upload_test.txt"):
#	os.remove(filename)

for filename in glob.glob("data/test20/cached*"):
   os.remove(filename)

