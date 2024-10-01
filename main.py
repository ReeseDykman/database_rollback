from manager import Rollback_manager

def main():

    transactions = [['1', 'Department', 'Music'],
                    ['5', 'Civil_status', 'Divorced'],
                    ['15', 'Salary', '200000']]
    
    manager = Rollback_manager()
    
    #query all transactions, rollback if commit returns false
    for index in range(len(transactions)):
        transaction = transactions[index]
        print(f"Processing transaction {index + 1}")
        result, trans_id = manager.query(transaction)
        if manager.commit(result, trans_id):
            print("Transaction committed")
        else:
            print(f"Error on transaction number {index + 1}. Changes not committed to database")

    manager.logger.print_logs()


if __name__ == '__main__':
    main()