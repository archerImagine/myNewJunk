for num in {1..25}; do
	fileName="ReadMe.md"
	dirName=chapter0$num
	subDir="jsSrc"

	if [[ num -gt 9 ]]; then
		dirName=chapter$num
		#echo "DirName: $dirName"
		#echo "fileName: $fileName"		
	fi  
	#indexFile=$dirName$".html"
	mkdir -p $dirName/$subDir
	cp chapter03/SpecRunner.html $dirName/
	#touch $dirName/$fileName  
	#touch $dirName/$indexFile  
done