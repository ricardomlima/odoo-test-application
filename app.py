import glob


class Application():
    """ 
    Configurable application that contains connection
    with databasae and delegates tasks using a TaskManager
    """

    def __init__(self, config):
        self.config = config

    def run_from_commandline(self):
        """ 
        Use command line task manager to execute tasks
        """

        task_manager = TaskManager()
        task_manager.run()


class TaskManager():
    """
    Responsible for task mapping, context and execution
    """

    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Walks through task directory and maps
        all available tasks
        """

        tasks = [(task[:-3].replace('/', '.'), 1)
                 for task in glob.glob("tasks/*.py")]

    def run(self, parameters):
        pass
