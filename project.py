
import mysql.connector

def clear():
  for _ in range(65):
     print()


def add_book():
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='system123')
  cursor = conn.cursor()

  book_id = int(input('Enter Book Id : '))
  title = input('Enter Book Title :')
  author = input('Enter Book Author : ')
  publisher = input('Enter Book Publisher : ')
  pages = int(input('Enter Book Pages : '))
  price = int(input('Enter Book Price : '))
  status = 'available'
  val = (book_id,title,author,price,pages,publisher,status)
  
  sql = 'insert into book(b_id,title,author,price,pages,publisher,status) values (%s,%s,%s,%s,%s,%s,%s);'
  cursor.execute(sql,val)
  conn.commit()
  conn.close()
  print('\n\nNew Book added successfully')
  wait = input('\n\n\n Press enter to continue....')


def add_member():
  conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='system123')
  cursor = conn.cursor()

  mem_id = int(input('Enter Member Id : '))
  name = input('Enter Member Name :')
  address = input('Enter Member Address : ')
  phone = int(input('Enter Member Phone  : '))
  email = input('Enter Member Email  : ')
  status = 'available'
  val = (mem_id,name,address,phone,email,status)
 
  sql = 'insert into member(m_id,name,address,phone,email,status) values (%s,%s,%s,%s,%s,%s);'
  
  cursor.execute(sql,val)
  conn.commit()
  conn.close()
  print('\n\nNew Member added successfully')
  wait = input('\n\n\n Press enter to continue....')


def modify_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()
    clear()
    print('Modify BOOK Details Screen ')
    print('-'*120)
    print('\n1. Book Title')
    print('\n2. Book Author')
    print('\n3. Book Publisher')
    print('\n4. Book Pages')
    print('\n5. Book Price')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    book_id = int(input('Enter Book ID :'))
    value = input('Enter new value :')
    val = (value,book_id)
    if choice == 1:
        sql = 'update book set title = %s where b_id = %s;'
    if choice == 2:
        sql = 'update book set author = %s where b_id = %s;'
    if choice == 3:
        sql = 'update book set publisher = %s where b_id = %s;'
    if choice == 4:
        sql = 'update book set pages = %s where b_id = %s;'
    if choice == 5:
        sql = 'update book set price = %s where b_id = %s;'

    cursor.execute(sql,val)
    print('\n\n\nBook details Updated.....')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press enter to continue....')


def modify_member():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()
    clear()
    print('Modify Memeber Information Screen ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Class')
    print('\n3. address')
    print('\n4. Phone')
    print('\n5. Email')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    mem_id =int(input('Enter member ID :'))
    value = input('Enter new value :')
    val = (value, mem_id)
    if choice == 1:
        sql = 'update member set name = %s where m_id = %s;'
    if choice == 2:
        sql = 'update member set class = %s where m_id = %s;'
    if choice ==3:
        sql = 'update member set address = %s where m_id = %s;'
    if choice == 4:
      sql = 'update member set phone = %s where m_id = %s;'
    if choice == 5:
        sql = 'update member set email = %s where m_id = %s;'
    
    #print(sql)
    cursor.execute(sql,val)
    print('Member details Updated.....')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press enter to continue....')

def book_issue(book_id,mem_id):
    conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()
    val3 = ('unavailable',book_id)
    val4 = ('unavailable',mem_id)

    sql3 = "update book set status = %s where b_id = %s;"
    cursor.execute(sql3,val3)
    sql4 = "update member set status = %s where m_id = %s;"
    cursor.execute(sql4,val4)
    conn.commit()
    conn.close()

def book_return(book_id,mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()
    val1 = ('available',book_id)
    val2 = ('availabe',mem_id)
    
    sql1 = 'update book set status = %s where b_id = %s;'
    cursor.execute(sql1, val1)
    sql2 = 'update member set status = %s where m_id = %s;'
    cursor.execute(sql2,val2)
    conn.commit()
    conn.close()

def issue_book():
    conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()

    clear()
    print('\n BOOK ISSUE SCREEN ')
    print('-'*120)
    book_id = int(input('Enter Book  ID : '))
    mem_id  = int(input('Enter Member ID : '))
    val1 = (book_id, 'available')
    val2 = (mem_id, 'available')

    sql1 = "select b_id,title from book where b_id = %s and status = %s;"
    cursor.execute(sql1,val1)
    result1 = cursor.fetchone()

    sql2 = 'select m_id, name from member where m_id = %s and status = %s;'
    cursor.execute(sql2,val2)
    result2 = cursor.fetchone()

    result = result2 + result1
    sql = 'insert into issued(m_id,name,b_id,title) values(%s,%s,%s,%s);'
    cursor.execute(sql,result)
    book_issue(book_id,mem_id)
    print('Book Issued. . . . .')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press enter to continue....')

def return_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()

    clear()
    print('\n BOOK RETURN SCREEN ')
    print('-'*120)
    book_id = int(input('Enter Book  ID : '))
    mem_id = int(input('Enter Member ID :'))
    

    result = (mem_id, book_id)
    sql = 'delete from issued where m_id = %s and b_id = %s;'
    cursor.execute(sql,result)
    book_return(book_id, mem_id)
    print('Book Returned. . . . .')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press enter to continue....')

def search_book(field):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()

    clear()
    print('\n BOOK SEARCH SCREEN ')
    print('-'*120)
    value = input('Enter' +field+ ': ')
    val = (field,value)
    sql ='select * from book where %s = %s;'
    cursor.execute(sql,val)
    records = cursor.fetchall()
    clear()
    print('Search Result for :',field,' :' ,value)
    print('-'*120)
    for record in records:
      print(record)
    conn.close()
    wait = input('\n\n\n Press enter to continue....')

def search_menu():
  conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
  cursor = conn.cursor()
  while True:
      clear()
      print(' S E A R C H   M E N U ')
      print("\n1.  Book Title")
      print('\n2.  Book Author')
      print('\n3.  Publisher')
      print('\n0.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      value = input('Enter value: ')
      val = (value, 'available')
      if choice == 1:
        sql ='select * from book where title = %s and status = %s;'
      if choice == 2:
        sql ='select * from book where author = %s and status = %s;'
      if choice == 3:
        sql ='select * from book where publisher = %s and status = %s;'
      if choice == 0:
        break

      cursor.execute(sql,val)
      records = cursor.fetchall()
      clear()
      print('Search Result:' ,value)
      print('-'*120)
      for record in records:
        print(record)
      conn.close()
      wait = input('\n\n\n Press enter to continue....')


def report_book_list():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES ')
    print('-'*120)
    sql ='select * from book;'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress enter to continue.....')


def report_issued_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES - Issued')
    print('-'*120)
    sql = 'select * from book where status = "unavailable";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress enter to continue.....')


def report_available_books():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - BOOK TITLES - Available')
    print('-'*120)
    sql = 'select * from book where status = "available";'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress enter to continue.....')

def report_member_list():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='system123')
    cursor = conn.cursor()

    clear()
    print('\n REPORT - Members List ')
    print('-'*120)
    sql = 'select * from member'
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
       print(record)
    conn.close()
    wait = input('\n\n\nPress enter to continue.....')


def report_menu():
    while True:
      clear()
      print(' R E P O R T    M E N U ')
      print("\n1.  Book List")
      print('\n2.  Member List')
      print('\n3.  Issued Books')
      print('\n4.  Available Books')
      print('\n0.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        report_book_list()
      if choice == 2:
        report_member_list()
      if choice == 3:
        report_issued_books()
      if choice == 4:
        report_available_books()
      if choice == 0:
        break


def main_menu():
    while True:
      clear()
      print(' L I B R A R Y    M E N U')
      print("\n1.  Add Books")
      print('\n2.  Add Member')
      print('\n3.  Modify Book Information')
      print('\n4.  Modify Student Information')
      print('\n5.  Issue Book')
      print('\n6.  Return Book')
      print('\n7.  Search Meneu')
      print('\n8.  Report Menu')
      print('\n0.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_book()
      if choice == 2:
        add_member()
      if choice == 3:
        modify_book()
      if choice == 4:
        modify_member()
      if choice == 5:
        issue_book()
      if choice == 6:
        return_book()
      if choice == 7:
        search_menu()
      if choice == 8:
        report_menu()
      if choice == 0:
        break

main_menu()
