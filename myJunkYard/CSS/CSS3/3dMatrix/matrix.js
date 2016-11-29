window.onload = function(){
for (x = 1; x < 5; x++){
	for (y = 1; y < 5; y++){
	var input = document.getElementById(("i" + x) + y);
	input.addEventListener("change", 
	  function(){
		  span = "s" + this.id.substr(1);
		  document.getElementById(span).innerHTML = (this.value*(this.step/100)).toFixed(4);
		  transformer.style.webkitTransform = "matrix3d(" 
		    + s11.innerHTML + "," + s21.innerHTML + "," + s31.innerHTML + "," + s41.innerHTML  + ","
			  + s12.innerHTML + "," + s22.innerHTML + "," + s32.innerHTML + "," + s42.innerHTML + ","
			  + s13.innerHTML + "," + s23.innerHTML + "," + s33.innerHTML + "," + s43.innerHTML + ","
			  + s14.innerHTML + "," + s24.innerHTML + "," + s34.innerHTML + "," + s44.innerHTML
	+	")";
	
	document.getElementById('threeDcss').innerHTML = "-webkit-transform:"+transformer.style.webkitTransform;
	}, false);
	}
}

  iperspective.addEventListener("change", function(){
	sperspective.innerHTML = this.value;
	stager.style.webkitPerspective = this.value;
});

stager.onmousemove = function(e){
	      var offsetX = e.pageX - this.offsetLeft;
	      var offsetY = e.pageY - this.offsetTop;

	      var originStyle = (100 * offsetX / stager.offsetWidth) + '% ' + (100 * offsetY / stager.offsetHeight) + '%';
	      stager.style.webkitPerspectiveOrigin = originStyle;
}




}
