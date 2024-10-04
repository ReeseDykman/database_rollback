from manager import Rollback_manager

def main():

    transactions = [['1', 'Department', 'Music'],
                    ['5', 'Civil_status', 'Divorced'],
                    ['15', 'Salary', '200000']]
    
    manager = Rollback_manager()
    print("\n\nCSV before transactions:\n")
    manager.print_csv()
    
    #query all transactions, call commit to either rollback or commit changes
    for index in range(len(transactions)):
        transaction = transactions[index]
        print(f"\n\nProcessing transaction {index + 1}")
        rollback_required, trans_id = manager.query(transaction)
        if manager.commit(rollback_required, trans_id):
            print("Transaction committed")
        else:
            print(f"Error on transaction number {index + 1}. Changes not committed to database, rollback complete.")

    print("\n\nAll transactions complete. Printing Logs:\n")
    manager.logger.print_logs()
    print("\n\nCSV after transactions:\n\n")
    manager.print_csv()


if __name__ == '__main__':
    main()