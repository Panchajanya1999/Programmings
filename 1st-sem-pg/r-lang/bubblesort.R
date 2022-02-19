#! /usr/bin/env Rscript

set <- c(10, 9, 8,7,6,5,4,3,2,1)

bubblesort <- function(x) {
  n <- length(x)
  for(i in 1:(n-1)) {
    for(j in 1:(n-i)) {
      if (x[j] > x[j+1]){
        temp <- x[j]
        x[j] <- x[j+1]
        x[j+1] <- temp
      }
    }
  }
  return (x)
}

out <- bubblesort(set)

cat("The original dataset was -", set)
cat("\nThe sorted dataset is - ", out)

