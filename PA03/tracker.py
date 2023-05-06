"""
Uses the transaction class from transaction.py in order to do many functions 
such as add transactions, show transactions, delete transactions, list transactions 
and summerize them by date, month, year  or category
"""
import sys
from datetime import datetime
from transaction import Transaction

def print_usage():
    """
    gives user an explanation as to how to use commands
    """
    print('''usage:
        0. quit                                 
        1. show transactions                   
        2. add transaction   (ex. 2 amount category description)
        3. delete transaction   (ex. 3 transaction#)
        4. summarize transactions by date   (ex. 4 dd)
        5. summarize transactions by month   (ex. 5 mm)
        6. summarize transactions by year   (ex. 6 yyyy)
        7. summarize transactions by category   (ex. 7 category)
        8. print this menu                                        
        '''
        )

def print_transactions(transactions):
    """
    prints a list of transactions
    """
    if len(transactions)==0:
        print('no transactions')
        return
    print('\n')
    print("#\tAmount\tCategory\tDate\t\t\tDescription")
    print('-'*80)

    for item in transactions:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print(f"{values[0]}\t{values[1]}\t{values[2]}\t\t{values[3]}\t{values[4]}")

def process_crud_args(arglist):
    """
    processes the args if user inputs crud operation
    """
    database = Transaction()
    database.show_all()
    if arglist==[]:
        print_usage()

    elif arglist[0]=="1":
        print_transactions(database.show_all())

    elif arglist[0]=="2":
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        transaction = {'amount':arglist[1],'category':arglist[2],
        'date':date,'description':arglist[3]}
        database.add(transaction)

    elif arglist[0]=="3":
        if len(arglist)!= 2:
            print_usage()
        else:
            database.delete(arglist[1])

    else:
        process_summary_args(arglist, database)

def process_summary_args(arglist, database):
    """
    processes the args if the user inputs a summerize command
    """
    if arglist[0]=="4" and len(arglist)== 2:
        print_transactions(database.summarize_by_day(arglist[1]))

    elif arglist[0]=="5" and len(arglist)== 2:
        print_transactions(database.summarize_by_month(arglist[1]))

    elif arglist[0]=="6" and len(arglist)== 2:
        print_transactions(database.summarize_by_year(arglist[1]))

    elif arglist[0]=="7" and len(arglist)== 2:
        print_transactions(database.summarize_by_category(arglist[1]))

    else:
        print_usage()

def toplevel():
    """
    reads the command args in order to process them
    """
    print_usage()
    args = []
    while args!=['']:
        args = input("command> ").split(' ')

        # add
        if args[0]=='0' or args[0]=='quit':
            sys.exit()
        if args[0]=='':
            args[0]='8'
        if args[0]=='2':
            if len(args)<4:
                args[0]='8'
            else:
                args = ['2',args[1],args[2]," ".join(args[3:])]
        process_crud_args(args)
        print('-'*80+'\n'*3)

if __name__ == "__main__":
    toplevel()
