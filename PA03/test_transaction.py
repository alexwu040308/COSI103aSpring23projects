import sqlite3
import os
from transaction import Transaction


class TestTransaction:

    @classmethod
    def setup_class(cls):
        cls.db_file = 'test_transaction.db'
        cls.db = sqlite3.connect(cls.db_file)
        cls.db.execute('CREATE TABLE IF NOT EXISTS transactions (amount int, category text, date text, description text)')

    @classmethod
    def teardown_class(cls):
        cls.db.close()
        os.remove(cls.db_file)

    def setup_method(self):
        self.transaction = Transaction("test_transaction.db")
        self.transaction.delete_all()

    def test_add_transaction(self):
        item = {'amount': 10, 'category': 'food', 'date': '2000-01-01', 'description': 'burger'}
        self.transaction.add(item)
        result = self.transaction.show_all()
        assert result[0]['amount'] == item['amount']
        assert result[0]['amount'] == item['amount']
        assert result[0]['category'] == item['category']
        assert result[0]['date'] == item['date']
        assert result[0]['description'] == item['description']

    def test_delete_transaction(self):
        item = {'amount': 10, 'category': 'food', 'date': '2000-01-01', 'description': 'burger'}
        self.transaction.add(item)
        result = self.transaction.show_all()
        assert len(result) == 1
        num = result[0]['item_num']
        self.transaction.delete(num)
        result = self.transaction.show_all()
        assert len(result) == 0

    def test_summarize_by_day(self):
        item1 = {'amount': 10, 'category': 'food', 'date': '2000-01-01', 'description': 'burger'}
        item2 = {'amount': 20, 'category': 'clothes', 'date': '2000-01-01', 'description': 'jacket'}
        self.transaction.add(item1)
        self.transaction.add(item2)
        result = self.transaction.summarize_by_day('01')
        assert len(result) == 2
        assert result[0]['amount'] == item1['amount']
        assert result[1]['amount'] == item2['amount']

    def test_summarize_by_month(self):
        item1 = {'amount': 10, 'category': 'food', 'date': '2000-01-01', 'description': 'burger'}
        item2 = {'amount': 20, 'category': 'clothes', 'date': '2000-01-01', 'description': 'jacket'}
        self.transaction.add(item1)
        self.transaction.add(item2)
        result = self.transaction.summarize_by_month('01')
        assert len(result) == 2
        assert result[0]['amount'] == item1['amount']
        assert result[1]['amount'] == item2['amount']

    def test_summarize_by_year(self):
        item1 = {'amount': 10, 'category': 'food', 'date': '2000-01-01', 'description': 'burger'}
        item2 = {'amount': 20, 'category': 'clothes', 'date': '2000-01-01', 'description': 'jacket'}
        item3 = {'amount': 30, 'category': 'food', 'date': '2001-01-01', 'description': 'steak'}
        item4 = {'amount': 40, 'category': 'clothes', 'date': '2001-01-01', 'description': 'jeans'}
        self.transaction.add(item1)
        self.transaction.add(item2)
        self.transaction.add(item3)
        self.transaction.add(item4)
        result = self.transaction.summarize_by_year('2001')
        assert len(result) == 2
        assert result[0]['amount'] == item3['amount']
        assert result[1]['amount'] == item4['amount']

    def test_summarize_by_category(self):
        item1 = {'amount': 10, 'category': 'food', 'date': '2000-01-01', 'description': 'burger'}
        item2 = {'amount': 20, 'category': 'clothes', 'date': '2000-01-01', 'description': 'jacket'}
        item3 = {'amount': 30, 'category': 'food', 'date': '2001-01-01', 'description': 'steak'}
        item4 = {'amount': 40, 'category': 'clothes', 'date': '2001-01-01', 'description': 'jeans'}
        self.transaction.add(item1)
        self.transaction.add(item2)
        self.transaction.add(item3)
        self.transaction.add(item4)
        result = self.transaction.summarize_by_category('clothes')
        assert len(result) == 2
        assert result[0]['category'] == item2['category']
        assert result[1]['category'] == item4['category']