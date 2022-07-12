drop sequence pelicana_seq ;
drop table pelicana ;

create sequence pelicana_seq;

create table pelicana (
  idx  number(4) primary key ,
  store varchar2(20) ,
  sido  varchar2(20) ,
  gungu varchar2(20) ,
  address varchar2(30) ,
  phone varchar2(10) ,
  wdate date
);

commit ;
col store for a10 ;
col address for a20 ;
col phone for a10 ;
select store, address, phone from pelicana ;

