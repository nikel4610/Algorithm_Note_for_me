import cx_Oracle

con = cx_Oracle.connect("system/1234@localhost:1521/xe")
print("database version: ", con.version)
print("oracle connect ok ")
print()

class PelicanaDB:
    def __init__(self):
        self.con = cx_Oracle.connect('system/1234@localhost:1521/XE')
        # self.db_init()
    

    def pelicana_crawlingInsert(self,store, sido, gungu, address,phone):
        sql = ''' insert into pelicana                    
                values(pelicana_seq.nextval, :1, :2, :3, :4, :5, CURRENT_TIMESTAMP) '''
        with self.con.cursor() as cursor:
            cursor.execute(sql, (store,sido,gungu,address,phone))
        self.con.commit()

if __name__ == "__main__":
    db = PelicanaDB()
    #db.pelicana_crawlingInsert('토성', '갤럭시', '한강구', '안드로메다', '000111');
    db.pelicana_crawlingInsert('둘리', '미로시', '노원구', '쌍문동', '000222');
    #db.pelicana_crawlingInsert('빅dt', '안동시', '태화강', '박물관', '000789');
    print('데이터 저장 성공했습니다   07-12-화요일 ')
    #select store, address, phone from pelicana ;
