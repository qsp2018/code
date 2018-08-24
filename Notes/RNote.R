# handle time zones
as.POSIXct( format(Sys.time(), tz=time_zone,usetz=FALSE), tz = time_zone)
a = Sys.time(); attr(a, "tzone") = "UTC"

# regex
regexpr( "^booster\\[.*\\]$", bst.str[1] )
look for:
- starting with booster 
- then [ 
- then anything any length 
- end with ]

#error cath
method 1:
    try_time <- 0
    while(  try_time < total_times )
    tryCatch({
      try_time <- try_time + 1
	    f()
        break # break if f() succeeded
        }, 
        error=function(e){
          print(e)
        }
     )

method 2:
	tryE <- try( { f() })
	if( class(tryE) == "try-error") {
		print(tryE)
	}