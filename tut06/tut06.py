def breakingbad(Season,episode):
    path=r'./correct_srt/Breaking Bad'
    source=r'./wrong_srt/Breaking Bad'
  
    shutil.copytree(source,path)
    for file in os.listdir(path):
      former_file=re.compile(r'\d\d')
	  
      x=former_file.findall(file)
      if type(file)=='.mp4':
          dest='Breaking Bad - Season '+ padding(x[0],Season) +' Episode ' +padding(x[1],episode)+ '.mp4' 
          os.rename('./correct_srt/Breaking Bad/'+file,'./correct_srt/Breaking Bad/'+dest)
      if type(file)=='.srt':
          dest='Breaking Bad - Season '+ padding(x[0],Season) +' Episode ' +padding(x[1],episode)+'.srt'  
          os.rename('./correct_srt/Breaking Bad/'+file,'./correct_srt/Breaking Bad/'+dest)

def regex_renamer():

    # Taking input from the user

    # print("1. Breaking Bad")
    # print("2. Game of Thrones")
    # print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))
    
	#Driver function***********

	if webseries_num==1:
        breakingbad(season_padding,episode_padding)
    elif webseries_num==2:
       gameofthrones(season_padding,episode_padding)
    else:
       lucifer(season_padding,episode_padding)

regex_renamer()