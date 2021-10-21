
  var player
  // window.onload=()=>{
  //   player=document.getElementById('player')
  //   maintainRatio()

  // }
 var video_list;

  document.onreadystatechange = function () {
    if (document.readyState == 'interactive') {
      player = document.getElementById('player')
      video_list=document.getElementById('video_list')
      // video_list.style.maxHeight
      maintainRatio()
    }
  }
  function maintainRatio() {
    var w = player.clientWidth
    var h = w * 9 / 16
    player.height = h+'px';
    video_list.style.maxHeight=h;

  }
  window.onresize = maintainRatio
