class TICKET_BOOK (object):
    """docstring for User"""
    def __init__(self, Class=None, bdg_pt=None, quota=None,usr=None):
        super(TICKET_BOOK, self).__init__()
        self.Class = Class
        self.bdg_pt = bdg_pt
        self.quota=quota
        self.usr=usr

    def __str__(self):
        return "============================="+\
                "\nuser : "+ str(self.usr)+\
               "\nClass : " + self.Class+\
               "\nbdg_pt: "+ str(self.bdg_pt)+\
               "\nquota : "+ str(self.quota)+\
               "\n============================="+\
               " "

    def display(self):
        print ("=============================")
        print ("USER         : ",self.usr)
        print (" CLASS       : ",self.Class)
        print (" BOARDING PT.: ",self.bdg_pt)
        print (" QUOTA       : ",self.quota)
        print ("=============================")
        print (" ")