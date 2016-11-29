$(function() {
	console.log("Login.js");
	$(".button").click(function() {
		console.log("Login Button Clicked");

		var username = $("input#username").val();
		console.log("username: " +username);

		var password = $("input#password").val();
		console.log("password: " +password);

		var data = {
			"usename" : username,
			"password" : btoa(password)
		}

		console.log("data" +data);
		$.ajax({
			type: "POST",
			url: "http://localhost:8080/CMADFinal/resource/signup", /*TODO: Change to proper URL*/
			data: data,
			success: function(){
				console.log("Form Submission Sucess");
			},
			error:function(){
				console.log("Form Submission Failed");
			},
			beforeSend: function (xhr) {
			    xhr.setRequestHeader ("Authorization", "Basic " + btoa(username + ":" + password));
			}
		});


	});

});