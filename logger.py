class Logger:
    def __init__(self):
        self.logs = {}

    def log(self, id, attribute, before, after, status):
        """
        adds a log to the logs dictionary
        params:
            id: the unique id of the transaction
            attribute: the attribute that was changed
            before: the value before the change
            after: the value after the change
            status: the status of the transaction
        """
        log = {id : {"attribute" : attribute, "before" : before, "after" : after, "status" : status}}
        print("Logging transaction..." + str(log))
        self.logs.update(log)

    def __getitem__(self, key):
        return self.logs[key]

    def print_logs(self):                                     
        for log in self.logs:
            print(str(log) + ":" + str(self.logs[log]))
    
    def to_csv(self):
        with open('logs.csv', 'w') as file:
            file.write("Transaction_ID,Attribute,Before,After,Status\n")
            for id, log in self.logs.items():
                line = f"{id},{log['attribute']},{log['before']},{log['after']},{log['status']}\n"
                file.write(line)
        print("Logs saved to logs.csv")