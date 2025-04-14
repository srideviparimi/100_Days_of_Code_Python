class User:
    def __init__(self,id,username,follower=0,following=0):
        self.id=id
        self.username=username
        self.follower=follower
        self.following=following
    def follow(self,user):
        user.follower+=1
        self.following+=1


user_1=User("001","angela")
user_2=User("002","Yu")
user_1.follow(user_2)

print(user_1.following)


