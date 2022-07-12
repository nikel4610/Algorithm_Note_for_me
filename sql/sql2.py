
class Emp:
    name = ''
    gschool = ''
    def __init__(self,school):
        print('생성자 = ', school)
        self.gschool = school
drop sequence pelicana_seq ;
drop table pelicana ;

create sequence pelicana_seq;

create table pelicana (
  idx  number(4) primary key ,
  store varchar2(20) ,
  sido  varchar2(20) ,
  gungu varchar2(20) ,
  address varchar2(30) ,
  phone varchar2(20) ,
  wdate date
);

commit ;
col store for a20 ;
col address for a30 ;
select store, address, phone from pelicana ;
