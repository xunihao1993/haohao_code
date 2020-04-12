  #!/bin/sh  
  upload_dir=/files/wlqz/xfzf/RSP/hzjgdz/
  #Ä¿±êÂ·¾¶
  www_dir=/home/xfzf/RSP/hzjgdz/ 
  backexist() 
  { 
  filelist=`ls $1` 
  for file in $filelist 
  do 
  if [ -f $1$file ] 
  then 
  if [ -f $2$file ] 
  then
  echo "repetition file"
  fi
  else
  backexist $1$file"/"$2$file"/" 
  fi 
  done 
  } 
  backexist $upload_dir $www_dir 
  cp -R $upload_dir"." $www_dir