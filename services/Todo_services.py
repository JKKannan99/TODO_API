#from models.Todo import Todo

todo_list = []
class TodoServices():

    def add_todo(self,td):
        todo_list.append(td)
        return ["Task Added Successfully !",td]

    def show_all(self):
        return todo_list
    
    def get_one_todo(self,id):
        for todo in todo_list:
            if todo.id == id:
                return todo
        return {"error": "Todo not found"}
    

    def update_todo(self,id,new_todo):
        for i in range(len(todo_list)):
            if todo_list[i].id == id:
                todo_list[i] = new_todo
                return new_todo
        return {"error": "Todo not found"}


    def delete_todo(self,id):
        for i in range(len(todo_list)):
            if todo_list[i].id == id:
                deleted = todo_list.pop(i)
                return {"deleted": deleted}
        return {"error": "Todo not found"}