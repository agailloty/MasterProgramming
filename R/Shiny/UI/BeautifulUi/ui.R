#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)


bootstrapPage(
    tags$nav(
        class="navbar navbar-expand-lg navbar-light bg-light",
        tags$a(class="navbar-brand", "Hello")
        
    )
)