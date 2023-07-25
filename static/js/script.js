//email send function
function sendMail(event) { 
    event.preventDefault();
    let name = document.getElementById("name")
    let email = document.getElementById("email")
    let message = document.getElementById("message")
    let params = {
        from_name : name.value,
        email : email.value,
        message : message.value
    }
    console.log("gotparams")
        emailjs.send("service_mjpd28u", "template_v8wvw2w", params)
            .then(function(response){
            alert("Thanks your email has been sent!");
            })
            .then( document.getElementById("contact_form").reset()
            )
}