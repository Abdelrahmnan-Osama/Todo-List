from task import Task

class TodoList:
    '''A to-do list'''

    def __init__(self, incomplete_tasks, complete_tasks):
        '''(TodoList, list of Task, list of Task) -> NoneType
        
        create a TodoList with list of incomplete_tasks and a list of complete_tasks.
        '''
        self.incomplete_tasks = incomplete_tasks
        self.complete_tasks = complete_tasks


    def add_task(self, task):
        '''(Task) -> NoneType

        add new incomplete task to the TodoList
        .
        '''
        self.incomplete_tasks.append(task)


    def mark_as_complete(self, task):
        '''(Task) -> NoneType
        
        mark the task as complete in the  TodoList
        .
        '''
        try:
            # get the index of the task to be removed
            task_index = self.incomplete_tasks.index(task)
            # remove the task
            removed_task = self.incomplete_tasks.pop(task_index)
            # add the task to complete_tasks
            self.complete_tasks.append(removed_task)
        except ValueError:
            print("Task not found!")

    
    def remove_task(self, task):
        '''(Task) -> NoneType
        
        remove a Task from the TodoList
        .
        '''
        # check where is the task and remove it
        if task in self.complete_tasks:
            self.incomplete_tasks.remove(task)
        elif task in self.incomplete_tasks:
            self.incomplete_tasks.remove(task)
        else:
            print('Task not found!')

    def display(self):
        '''(NoneType) -> NoneType
        
        displays the TodoList in a file
        '''
        with open('todo_list.txt', 'w') as file:
            # create headers
            headers = 'Incompleted Tasks | Completed Tasks\n'
            headers_len = len(headers)
            file.write(headers)
            file.write('-' * headers_len + '\n')

            # create a list of rows with a specific format

            # prepare tasks' lists
            complete_copy, incomplete_copy = self.__create_equal_lists(self.complete_tasks, self.incomplete_tasks)
            # determine number of rows to be written
            num_rows = len(incomplete_copy)
            # prepare alignment options
            alignment_len = (headers_len//2) - 1
            # create list
            rows_list = [f"{incomplete_copy[i].name: ^{alignment_len}} | {complete_copy[i].name: ^{alignment_len}}\n" for i in range(num_rows)]

            # write the rows to the file
            file.writelines(rows_list)


    def __create_equal_lists(self, list1, list2):
        '''(list, list) -> (list, list)
        
        make list1 and list2 have same length
        '''
        list3 = list1.copy()
        list4 = list2.copy()
        diff = abs(len(list3) - len(list4))
        if len(list3) > len(list4):
            for i in range(diff):
                list4.append(Task())
        else:
            for i in range(diff):
                list3.append(Task())

        return list3, list4

task1 = Task('Studying')
task2 = Task('Playing')
task3 = Task('Singing')
task4 = Task('Eating')
task5 = Task('Sleeping')
task6 = Task('exercising')
task7 = Task('cleaning')

list3 = TodoList([task1, task2, task7], [task4, task5, task6, task3])
list3.display()