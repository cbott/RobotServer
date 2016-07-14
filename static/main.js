$(function() {
  $(".command-button .command-button-wide").on("mousedown touchstart", function() {
    $.post('/action',{ command:this.id });
  }).on("mouseup touchend", function() {
    $.post('/action',{ command:0 });
  }); 
  
  $("#slide").change(function() {
    $.post('/action',{ command:$("#slide").val() });
  });

  $("#shutdown").click(function() {
    var check = confirm("Are you sure you want to shut down? This action cannot be undone without manually cycling power.");
    if(check){
      $.post('/shutdown');
    }
  });

  
  var c = document.getElementById("canv");
  var rect = c.getBoundingClientRect();
  var ctx = c.getContext("2d");
  
  $("#canv").mousemove(function(e){
	ctx.clearRect(0, 0, c.width, c.height);
	ctx.beginPath();
    ctx.arc(e.pageX-rect.left,e.pageY-rect.top,5,0,2*Math.PI);
    ctx.stroke();
	console.log(e.pageX,e.pageY);
  });

});
