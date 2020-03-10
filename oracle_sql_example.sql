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
/*analytic_function([ arguments ]) OVER (analytic_clause)*/
