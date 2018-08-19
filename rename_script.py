
#VERSION 1 
import os

os.chdir('F:\Tutorial\python\chorey shafer\python\Flask') # change the dirictory here 
for file in os.listdir():
	
	f_name,f_ext = os.path.splitext(file)
	p_name,p_name_1,v_name_num,v_name,v_id = f_name.split('-')
	video_name,video_num = v_name_num.split('Part')
    
	video_name = video_name.strip()
	video_num = video_num.strip().zfill(2)
	p_name = p_name.strip()
	p_name_1 = p_name_1.strip()
	v_name_num = v_name_num.strip()
	v_name = v_name.strip()
	v_id = v_id.strip()
	
	newFile = '{}-{}.{}'.format(video_num,v_name,f_ext)

	os.rename(file,newFile)

 




