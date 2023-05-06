"""
this class presents the possible transaction functions that can be done, 
including adding, removing, showing and summerizing
"""

import sqlite3

def to_dict(transactions):
    """
    creates dictionary that represents the transaction as a set of key-value pairs
    """
    t_dict = {'item_num':transactions[0], 'amount':transactions[1],
            'category':transactions[2], 'date':transactions[3], 'description':transactions[4]}
    return t_dict

class Transaction():
    """
    class that manages the functions of transactions
    """
    def __init__(self, db_name = 'transaction.db'):
        """
        intializes the transaction database
        """
        self.db_name = db_name
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
        (amount int, category text, date text, description text)''',())

    def add(self,item):
        """
        adds an item to the database
        """
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],
                            item['category'],item['date'],item['description']))

    def show_all(self):
        """
        shows all items in the databse
        """
        return self.run_query("SELECT rowid,amount,category,date,description FROM transactions",())

    def delete(self,num):
        """
        deletes all items in the database
        """
        return self.run_query("DELETE FROM transactions WHERE rowid = ?",(num,))

    def summarize_by_day(self,day):
        """
        summerizes all items in the database by day
        """
        return self.run_query("SELECT rowid,* FROM transactions WHERE STRFTIME('%d', date) = ?",
                             (day,))

    def summarize_by_month(self,month):
        """
        summerizes all items in the database by month
        """
        return self.run_query("SELECT rowid,* FROM transactions WHERE STRFTIME('%m', date) = ?",
                             (month,))

    def summarize_by_year(self,year):
        """
        summerizes all items in the database by year
        """
        return self.run_query("SELECT rowid,* FROM transactions WHERE STRFTIME('%Y', date) = ?",
                              (year,))

    def summarize_by_category(self,category):
        """
        summerizes all items in the database by category
        """
        return self.run_query("SELECT rowid,* FROM transactions WHERE category = ?", (category,))

    def delete_all(self):
        """
        deletes everything in database
        """
        return self.run_query("DELETE FROM transactions", ())

    def run_query(self, query, tup):
        """
        runs the sql query and returns the results as a database
        """
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute(query, tup)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
