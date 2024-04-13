function filterOrders() {
  let price = $( "#price" ).val();
  let regexp = new RegExp("\\d+", "g");
  price = Array.from(price.matchAll(regexp));
  let min_price = price[0] ? price[0] : Number($( "#min-price" ).text());
  let max_price = price[1] ? price[1] : Number($( "#max-price" ).text());
  let cities = $( "#cities" ).val();
  let users = $( "#users" ).val();
  let uri = "/" + "?min_price=" + min_price + "&max_price=" + max_price;
  uri += cities != '' ? "&cities=" + cities : "";
  uri += users != '' ? "&users=" + users : "";
  window.location.replace(uri);
}


$( function() {
    let min = Number($( "#min-price" ).text()); 
    let max = Number($( "#max-price" ).text());
    let params = new URLSearchParams(window.location.search);
    let choice_min = min;
    let choice_max = max;
    if (params.has("min_price"))
      choice_min = params.get("min_price")
    if (params.has("max_price"))
      choice_max = params.get("max_price")
    $( "#slider-range" ).slider({
      range: true,
      min: min,
      max: max,
      values: [ choice_min, choice_max ],
      slide: function( event, ui ) {
        $( "#price" ).val( ui.values[ 0 ] + "р." + " - " + ui.values[ 1 ] + "р.");
      }
    });
    $( "#price" ).val($( "#slider-range" ).slider( "values", 0 ) + "р." +
      " - " + $( "#slider-range" ).slider( "values", 1 ) + "р.");
  } );

  
$( "#button-filter" ).on("click", filterOrders);