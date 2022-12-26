import cx_Oracle

CN = cx_Oracle.connect('system/1234@localhost:1521/xe')
print('Oracle 접속')

# msg = '''
# insert into pelica values(nextval, :1, :2, :3, :4, :5, CURRENT_TIMESTAMP)
# '''

msg = '''
insert into pelica values(pelicana_seq, 'aa', 'bb', 'cc', 'dd', 'ee', sysdate)
'''

with CN.cursor() as cursor:
    cursor.execute(msg)
CN.commit()

