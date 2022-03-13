class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        self.name = []
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

    def print_tree(self):
        print('     '*self.get_level(),'|--',self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def display_hirarchy(self):
       queue = []
       queue.append(self)
       while len(queue)>0:
            val = queue.pop(0)
            print(val.data,end=', ')
            for child in val.children:
                queue.append(child)

    def search(self,data):
        if self.data == data:
            return self
        queue = []
        queue.append(self)
        while len(queue)>0:
            val = queue.pop(0)
            if val.data == data:
                return val
            for child in val.children:
                queue.append(child)

    def search_role(self,data):
        if data in self.name:
            return self
        queue = []
        queue.append(self)
        while len(queue)>0:
            val = queue.pop(0)
            if data in val.name:
                return val
            for child in val.children:
                queue.append(child)
    
    def delete(self,delete_node_data,transfer_node_data):
        if delete_node_data==transfer_node_data:
            print('No changes made')
            return self
        try:
            new_parent = root.search(transfer_node_data)
            delete_node = root.search(delete_node_data)
        except AttributeError:
            return self
        
        if delete_node==None:
            print('Please enter role present in Hierarchy, so that it can be deleted')
        elif new_parent==None:
            print('Please enter Please enter role present in Hierarchy, so that sub roles can be assigned to it')
        elif delete_node.parent==None:
             print('Root cannot be deleted as of now')
             return self
        else:
            if new_parent in delete_node.children:
                delete_node_parent = root.search_parent(delete_node)
                for child in delete_node.children:
                    delete_node_parent.children.append(child)

                old_parent = root.search_parent(delete_node)
                old_parent.children.remove(delete_node)
                delete_node.parent = None
                return self 

                print('catch')
            for child in delete_node.children:
                new_parent.children.append(child)

            old_parent = root.search_parent(delete_node)
            old_parent.children.remove(delete_node)
            delete_node.parent = None
            return self     

    def search_parent(self,childnode):
        if childnode in self.children:
            return self
        queue = []
        queue.append(self)
        while len(queue)>0:
            val = queue.pop(0)
            if childnode in val.children:
                return val
            for child in val.children:
                queue.append(child)

def print_users():
        for user in users.keys():
            names = []
            queue = []
            urole = root.search_role(user)
            queue.append(urole)
            userSubuser[user] = []
            while len(queue)>0:
                val = queue.pop(0)
                names.append(val.name)
                for child in val.children:
                    queue.append(child)
            names = names[1:]
            print(user,' - ',end=' ')
            for u in names:
                for e in u:
                    print(e,end=' ')
                    userSubuser[user].append(e)

            print()
                 
def add_sub_role(root):
    sub_role = input('Enter sub role name : ')
    if sub_role in sub_role_list:
        print('Role already exists')
        return
    sub_role_list.append(sub_role)
    reporting_name = input('Enter reporting to role name :')
    sub = Node(sub_role)

    if root.data == reporting_name:
        root.add_child(sub)
    else:
        reporting_node = root.search(reporting_name)
        if reporting_node==None:
            print('Please enter role present in Hierarchy, so that it can added in the hierarchy')
        else:
            reporting_node.add_child(sub)
    return root

def getusers(root):
    dic = {}
    revdic = {}
    for user in users:
        dic[user] = []
    
    for k,v in users.items():
        if v in revdic:
            revdic[v].append(k)
        else:
            revdic[v] = list([k])

def delete_user(uname):
    node = root.search_role(uname)
    if node==None:
        print('Please Enter User Name present in Hierarchy')
    else:
        node.name.remove(uname)
        users.pop(uname)

def height(self):
    levels.append(self.get_level())
    if self.children:
        for child in self.children:
            height(child)

def get_common_users():
    for user in users.keys():
        names = []
        queue = []
        urole = root.search_role(user)
        queue.append(urole)
        userSubuser[user] = []
        while len(queue)>0:
            val = queue.pop(0)
            names.append(val.name)
            for child in val.children:
                queue.append(child)
        names = names[1:]
        for u in names:
            for e in u:
                userSubuser[user].append(e)
def menu():
    print('\nOperations :\n1.  Add Sub Role\n2.  Display Roles\n3.  Delete Role\n4.  Add user\n5.  Display User')  
    print('6.  Display Users and Sub Users\n7.  Delete User\n8.  Number of users from top')
    print('9.  Height of role hierarchy\n10. Common boss of users\n') 

####################################### Main Function ##################################################

if __name__ == "__main__":
    users = {}
    root_role = input('Enter root role name: ')
    root = Node(root_role)
    levels = []
    userSubuser = {}
    sub_role_list = []

    while(1):
        menu()            
        val = input('Operation to be performed : ')
        if val=='1':
            root = add_sub_role(root)
        
        elif val=='2':
            root.print_tree()
            print()
            root.display_hirarchy()
            print()
            print()
        
        elif val=='3':
            delete_node_data = input('Enter the role to be deleted: ')
            transfer_node_data = input('Enter the role to be transfered: ')
            root.delete(delete_node_data,transfer_node_data)
        
        elif val=='4':
            uname = input('Enter User Name  :')
            role = input('Enter Role : ')
            node = root.search(role)
            node.name.append(uname)
            users[uname]=role
        
        elif val=='5':
            for k,v in users.items():
                print(k,'-',v)
       
        elif val=='6':
            print_users()
        
        elif val=='7':
            uname = input('Enter username to be deleted : ')
            delete_user(uname)
        
        elif val=='8':
            get_common_users()
            c = 0
            name = input('Enter user name : ')
            for k,v in userSubuser.items():
                if name in v:
                    c+=1
            if name not in users:
                print('Please enter user name present in Hierarchy')
            else:
                print('Number of users from top :',c)

        elif val=='9':
            height(root)
            print('Height -',max(levels)+1)
        
        elif val=='10':
            get_common_users()
            U1 = input('Enter user 1 : ')
            U2 = input('Enter user 2 : ')
            if U1 not in users or U2 not in users:
                print('Please enter user names present in Hierarchy')
            else:
                for k,v in userSubuser.items():
                    
                    if U1 in v and U2 in v:
                        print('Top most common boss :',k)
                        break
                else:
                        print('No common boss ')
        elif val=='0':
            print('Thank You')
            exit()
        else:
            print('Wrong Input')
            
    

