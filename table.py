--SELECT * FROM demo;
--create table patientinfo1
--(patientid int,fname varchar2,lname varchar2,city varchar2,phoneno int);
--insert into patientinfo1 values(101,"agal","ya","chennai",9786577030);
--insert into patientinfo1 values(102,"sharmi","rajesh","chennai",89897654);
--select* from patientinfo1;
--select lname,fname,city from patientinfo1;
select lname as last_name,fname as first_name,city from patientinfo1;
