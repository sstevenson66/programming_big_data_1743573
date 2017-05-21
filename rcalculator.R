addfunc <- function(num1, num2) {
     return (num1 + num2)
}

subfunc <- function(num1, num2) {
    return (num1 - num2)
}

divfunc <- function(num1, num2) {
  if (num2 == 0) {
    return (0)
  } else {
    return (num1 / num2)
  }
}

powerfunc <- function(num1, num2) {
  return (num1 ** num2)
}

multi_funct <- function(num1, num2) {
  return (num1 * num2)
}

sqrfunc <- function(num1) {
  return (powerfunc(num1, 2))
}

factfunc <- function(num1) {
  calc = 1
  for (i in num1:2) {
    calc = calc * i
  }
  return(calc)
}

isprimeno <- function(num) {
  if (num <= 2)
  {
    return(FALSE)
  }
  for (i in (3:num -1)) {
     if (num %% i == 0) {
      return(TRUE)
    }
  }
  return(FALSE)
}

calc_avg <- function(...) {
  total = 0
  arguments <- list(...)
  if (length(arguments) == 0){
    return(0)
  }
  for (i in (1:length(arguments))) {
    total = total + as.numeric(arguments[i])
  }
  return(total/ length(arguments))
}

min_num <- function(...) {
  min_num <- NA
  arguments <- list(...)
  for (i in (1:length(arguments))) {
    if (is.na(min_num)) {
      min_num <- as.numeric(arguments[i])
    }
    else if (as.numeric(arguments[i]) < min_num) {
      min_num <- as.numeric(arguments[i])
    }
  }
  return(min_num)
}

print(addfunc(1,3))
print(subfunc(1.4556, 3.46788))
print(divfunc(10,3))
print(divfunc(10,0))
print(sqrfunc(6))
print(powerfunc(2,13))
print(factfunc(4))
print(isprimeno(7))
print(isprimeno(9))
print(calc_avg(1,5,6,7,9,10, 0, 8, 9))
print(calc_avg())
print(multi_funct(9, 11))
print(min_num(9, 10, 4, 7))



