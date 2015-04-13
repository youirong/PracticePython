'''
Created on 2015年4月11日
   
@author: Rong
'''
   
# movies = ["a", "b", "c"]
# print (movies[1])
#    
# movies.insert(1, 1)
# movies.insert(3, 2)
# movies.append(3)
# for movie in movies:
#     print(movie)
#    
# a = 0
# print (isinstance(movies, list))
# print (isinstance(a, list))

movies = ["a", "b", ["c", ["d", "e"]]]

# print (movies)
# 
# for each in movies:
#     print(each)

for eachitem in movies:
    if isinstance(eachitem, list) == False:
        print(eachitem)
    else:
        for a in eachitem:
            if isinstance(a, list) ==False:
                print (a)
            else:
                for b in a:
                    print (b)

                        

    