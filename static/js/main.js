console.log("I am here!!!")


    // JQuery code to be added in here.


$("#js-clicker").click(function() {

    $.ajax("/birthdays").then (function(birthdays){
$(birthdays).each(function(){
    let b = JSON.stringify(birthdays)
    $("#birfday").append(b)
})
})

})

// TODO: make an http request to ""

// url: "/birthdays"