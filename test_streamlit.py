import streamlit as st
import os, glob
from pathlib import Path

st.title("ABSA TOOL")
uploaded_file = st.file_uploader('UPLOAD FILE')
if uploaded_file is not None:
	with open('data/test20/upload_test.txt', 'w+') as txt_uploader:
		txt_uploader.write(str(uploaded_file.read()))
	st.write('File successfully uploaded.')


with open('data/test20/testing.txt', 'w+') as txt_reader:
	string = st.text_input('ENTER TEXT', value='', max_chars=None, key=None, type='default')
	txt_reader.write(string)
	st.write(string)

if st.button('PROCESS'):
	st.write('Process started.')
	os.system("sh work.sh")
	st.write('Process finished.')


#for filename in glob.glob("data/test20/testing.txt"):
#	os.remove(filename)
#
#for filename in glob.glob("data/test20/upload_test.txt"):
#	os.remove(filename)
#
for filename in glob.glob("data/test20/cached*"):
   os.remove(filename)