$(function() {
  $("button").on("mousedown touchstart", function() {
    $.post('/action',{ command:this.id });
  }).on("mouseup touchend", function() {
    $.post('/action',{ command:0 });
  }); 
  
  $("#slide").change(function() {
    $.post('/action',{ command:$("#slide").val() });
  });
});
