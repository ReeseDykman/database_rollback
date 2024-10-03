class Logger:
    def __init__(self):
        self.logs = {}

    def log(self, id, attribute, before, after, status):
        log = {id : {"attribute" : attribute, "before" : before, "after" : after, "status" : status}}
        print("Logging transaction..." + str(log))
        self.logs.update(log)

    def __getitem__(self, key):
        return self.logs[key]

    def print_logs(self):                                     
        for log in self.logs:
            print(log)