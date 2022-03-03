$(function () {
  var valueTe = JSON.parse(document.getElementById('nodeTeG').textContent);
  var valTemp = jQuery.parseJSON(valueTe);

  var valueSo = JSON.parse(document.getElementById('nodeSoG').textContent);
  var valSo = jQuery.parseJSON(valueSo);
  // alert(valTemp);
  // var timeT = [];
  var meanT = [];
  // outer loop
  valTemp.forEach((item, i) => {
    //inner loop
    item.forEach((myvar, i) => {
      // timeT.push(new Date(myvar.time).getHours().toString().padStart(2, '0')+ ":"+new Date(myvar.time).getMinutes().toString().padStart(2, '0'));
      meanT.push(myvar.mean);
    });

  });
  feather.replace()

  // var dVal = meanT;
  // alert(meanT);
  var dVal = meanT;
  var newVal = dVal * 1.8 - 45;
  // $(".circle-inner, .gauge-copy").css({
  //   transform: "rotate(" + newVal + "deg)"
  // });
  // $(".gauge-copy").css({
  //   transform: "translate(-50%, -50%) rotate(" + dVal * 1.8 + "deg)"
  // });
  // $(".percentage").text(dVal + " °C");
  $("#c1").css({
    transform:"rotate(" + newVal + "deg)"
  });
  $("#g1").css({
    transform:"translate(-50%, -50%) rotate(" + dVal * 1.8 + "deg)"
  });
  $("#p1").text(parseFloat(dVal).toFixed(2) + " °C");

  // var sVal = 78;
  // var newsVal = sVal * 1.8 - 45;
  // $("#c2").css({
  //   transform:"rotate(" + newsVal + "deg)"
  // });
  // $("#g2").css({
  //   transform:"translate(-50%, -50%) rotate("+ sVal * 1.8 +"deg)"
  // });
  // $("#p2").text(sVal + " %");

  var meanS = [];
  // outer loop
  valSo.forEach((item, i) => {
    //inner loop
    item.forEach((myvar, i) => {
      // timeT.push(new Date(myvar.time).getHours().toString().padStart(2, '0')+ ":"+new Date(myvar.time).getMinutes().toString().padStart(2, '0'));
      meanS.push(myvar.mean);
    });

  });
  feather.replace()

  var sVal = meanS;
  var newsVal = sVal * 1.8 - 45;
  $("#c2").css({
    transform:"rotate(" + newsVal + "deg)"
  });
  $("#g2").css({
    transform:"translate(-50%, -50%) rotate("+ sVal * 1.8 +"deg)"
  });
  $("#p2").text(parseFloat(sVal).toFixed(2) + " %");

});
