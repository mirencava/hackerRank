select min(city), len
  from (
        select city, length(city) len,
               max(length(city)) over() maxlen,
               min(length(city)) over() minlen
          from station
       )
 where len in(minlen,maxlen)
 group by len;

                   /*el min del select es porque hay que quedarse con la primera de las apareciones de aquellas agrupaciones que tengan la misma longitud*/
/*analytic_function([ arguments ]) OVER (analytic_clause)
                   SELECT empno, deptno, sal, 
       FIRST_VALUE(sal IGNORE NULLS) OVER (PARTITION BY deptno ORDER BY sal ASC NULLS LAST) AS first_val_in_dept
FROM   emp;*/
