<head>
<META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE, NO-STORE">
<script src="/static/jquery.js"></script>
<script src="/static/main.js"></script>
<link rel="stylesheet" href="/static/bootstrap.css">
<link rel="stylesheet" href="/static/style.css">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <div id="header">
    <p id="title">Robot controller</p>
  </div>
  <div id="controls">
    <div class="row">
      <div class="col-xs-3">
        <button id="1">Drive Forward</button>
      </div>
      <div class="col-xs-3">
        <button id="2">Drive Backward</button>
      </div>
    </div>
    
    <div class="row">
      <div class="col-xs-2">
        <p>Slider:</p>
      </div>
      <div class="col-xs-1">
        <input type="range" name="slide" id="slide" value="150" min="100" max="200"></input>
      </div>
    </div>
  </div>
</body>