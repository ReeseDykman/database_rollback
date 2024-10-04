from logger import Logger

class Rollback_manager:

    def __init__(self):
        self.logger=Logger()

    def read_csv(self):
        #the data in main memory is a dictionary of dictionaries, the keys are the Unique_ID
        data = {}
        print("Reading database.csv")
        with open('database.csv', 'r') as file:
            #grab all headers, they are the keys of the dictionary for our dictionaries
            headers = file.readline().strip().split(',')
            for line in file.readlines():
                #split the data line by comma
                data_line = line.strip().split(',')

                #create a dictionary with the headers as keys, we skip the id for now
                employee = {}
                for index, header in enumerate(headers):
                    if index == 0:
                        continue
                    employee[header] = data_line[index]

                #the employee dictionary gets added to the data dictionary with the id as key
                data[data_line[0]] = employee
        return data
    
    def write_csv(self):
        header = "Unique_ID,First_name,Last_name,Salary,Department,Civil_status\n"
        with open('database.csv', 'w') as file:
            file.write(header)
            for id, employee in self.data.items():
                line = f"{id},{employee['First_name']},{employee['Last_name']},{employee['Salary']},{employee['Department']},{employee['Civil_status']}\n"
                file.write(line)
            
    
    def query(self, query: list):
        id, field, value = query
        self.data = self.read_csv()
        rollback_needed = False

        #log the transaction with id, field, before and after values and status
        self.logger.log(id, field, self.data[id][field], value, "PENDING")

        #transaction with unique id of five will always fail
        if id == '5' or field not in self.data[id]:
            rollback_needed = True
        
        #update the value in main memory
        self.data[id][field] = value

        print(f"Transaction {id} updated {field} : {self.logger[id]['before']} to {value}")

        #we saved the changes to the in memory data, now we have to check if the transaction is valid
        return rollback_needed, id


    def commit(self, result: bool, transaction_id: str):
        
        #if the result is true, wee need to rollback, else we save to disk
        if result:
            log = self.logger[transaction_id]
            self.data[transaction_id][log['attribute']] = log['before']
            self.logger[transaction_id]['status'] = "ROLLED BACK"
            print("Error on transaction number " + transaction_id + ". Rollback initiated.")
            print("Updating Log..." + str(log))
            self.logger.to_csv()
            print("Rollback successful")
            return False
        else:
            self.logger[transaction_id]['status'] = "COMMITTED"
            log = self.logger[transaction_id]
            print("Updating Log..." + str(log))
            self.logger.to_csv()
            self.write_csv()
            print("Commit successful, changes saved to disk.")
            return True
        
    def print_csv(self):
        with open('database.csv', 'r') as file:
            print(file.read())