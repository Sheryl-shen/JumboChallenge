

def matchList(user_set):
    
    winning_set = [7, 22, 24, 31, 33, 40]
    match_list = []

    for i in user_set:
        if i in winning_set:
            match_list.append(i)
          
    
    return match_list

def typeOfWinning(user_set):

    match_list = matchList(user_set)
    type=''
    if len(match_list) == 6:
        type = 'Division 1'
    elif len(match_list) == 5:
        type = 'Division 2'
    elif len(match_list) == 4:
        type = 'Division 3'
    elif len(match_list) == 3:
        type = 'Division 4'
    else:
        type = 'None'

    return type


def johnSet():
    Game_1 = [7, 9, 13, 24, 33, 40]
    Game_2 = [16, 19, 22, 29, 31, 39]
    Game_3 = [1, 7, 18, 22, 30, 36]
    Game = [Game_1, Game_2, Game_3]
    
    user_list = ['John', Game]
    return user_list


def marySet():
    Game_1 = [2, 22, 13, 24 ,32, 39]
    Game_2 = [7, 22, 24, 31, 33, 40]
    Game_3 = [3, 7, 18, 21, 37, 38]
    Game = [Game_1, Game_2, Game_3]
        
    user_list = ['Mary', Game]
    return user_list


def user():

    user1_set = []
    user2_set = []
    for i in range(3): 
        user1_set.append([johnSet()[0],i+1, johnSet()[1][i]])
        user2_set.append([marySet()[0],i+1, marySet()[1][i]])   

    user_set = user1_set + user2_set
    return user_set
    

def main():

    count = 0
    for i in user():
        count +=1
        print(i[0] +' wins a ' + typeOfWinning(i[2]) + ' on game #' + str(i[1]) +
        ' with matches '+ str(matchList(i[2])) + ' in game ' + str(i[2]));


if __name__ == "__main__":
    main()







    
