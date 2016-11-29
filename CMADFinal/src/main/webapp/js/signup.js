

$(function() {
	console.log("SignUp JS");
	$(".button").click(function() {
		console.log("Button Pressed");

		var username = $("input#username").val();
		console.log("username: " +username);

		var email = $("input#email").val();
		console.log("email: " +email);

		var password = $("input#password").val();
		console.log("password: " +password);

		var data = {
			"usename" : username,
			"email" : email,
			"password" : btoa(password)
		}

		console.log("data" +data);
		$.ajax({
			type: "POST",
			url: "http://173.36.54.84:8888/CMADFinal/resource/signup", /*TODO: Change to proper URL*/
			data: data,
			success: function(){
				console.log("Form Submission Sucess");
			},
			error:function(){
				console.log("Form Submission Failed");
			}
		});
	});
});