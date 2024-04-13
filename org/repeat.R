repeat {
    input <- readline(prompt = "Enter a number (or 'quit' to exit): ")
    if (tolower(input) == "quit") {
        cat("Exiting loop.\n")
        break
    }
    if (is.na(as.numeric(input))) {
        cat("Not a number. Please try again.\n")
    } else {
        cat("You entered:", as.numeric(input), "\n")
    }
}
