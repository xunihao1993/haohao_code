  #!/bin/sh  
  upload_dir=/files/zjyw/dxlc/ssdz/
  #Ä¿±êÂ·¾¶
  www_dir=/home/yst/ssdz/
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