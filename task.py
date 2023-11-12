class Task:
    '''A Task in a TodoList'''
    def __init__(self, name = '', category = '', priority = 0, due_date = None):
        '''(Task, str, str, int, date) -> NoneType
        
        create a Task with a name, category, priority, and due_date
        '''
        self.name = name
        self.category = category
        self.priority = priority
        self.due_date = due_date