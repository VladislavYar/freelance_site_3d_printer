const old_cities = $("#cities").val();
const old_users = $("#users").val();
let params = new URLSearchParams(window.location.search);
let old_choice_min = Number($("#min-price").text()); 
let old_choice_max = Number($("#max-price").text());
if (params.has("min_price"))
  old_choice_min = params.get("min_price");
if (params.has("max_price"))
  old_choice_max = params.get("max_price");
let new_choice_min = old_choice_min;
let new_choice_max = old_choice_max;


function filterOrders() {
  let price = $("#price").val();
  let regexp = new RegExp("\\d+", "g");
  price = Array.from(price.matchAll(regexp));
  let min_price = price[0] ? price[0] : Number($( "#min-price" ).text());
  let max_price = price[1] ? price[1] : Number($( "#max-price" ).text());
  let cities = $("#cities").val();
  let users = $("#users").val();
  let uri = "/" + "?min_price=" + min_price + "&max_price=" + max_price;
  uri += cities != '' ? "&cities=" + cities : "";
  uri += users != '' ? "&users=" + users : "";
  uri += $(".show").attr("id") == "orders" ? "&customer_tab=1" : "&customer_tab=0";
  window.location.replace(uri);
}


function activateButtonFilter(
  old_cities, old_users
) {
  if (
    old_cities.toString() != $("#cities").val().toString() ||
    old_users.toString() != $("#users").val().toString() ||
    old_choice_min != new_choice_min ||
    old_choice_max != new_choice_max
  )
    $("#button-filter").attr("disabled", false);
  else
    $("#button-filter").attr("disabled", true);
}


$( function() {
    $("#slider-range").slider({
      range: true,
      min: Number($("#min-price").text()),
      max: Number($("#max-price").text()),
      values: [old_choice_min, old_choice_max],
      slide: function(event, ui) {
        new_choice_min = ui.values[0];
        new_choice_max = ui.values[1];
        activateButtonFilter(
          old_cities, old_users
        )
        $("#price").val(ui.values[0] + "р." + " - " + ui.values[1] + "р.");
      }
    });
    $("#price").val($("#slider-range").slider("values", 0) + "р." +
      " - " + $("#slider-range").slider("values", 1) + "р.");
  } );
$("#button-filter").on("click", filterOrders);
$("#cities").change(function(){
  activateButtonFilter(old_cities, old_users)
});
$("#users").change(function(){
  activateButtonFilter(old_cities, old_users)
});
$(".btn-toggle").click(function() {
  $(this).find(".btn").toggleClass("active");  
  
  if ($(this).find(".btn-primary").length>0) {
    $(this).find(".btn").toggleClass("btn-primary");
  }
  if ($(this).find(".btn-danger").length>0) {
    $(this).find(".btn").toggleClass("btn-danger");
  }
  if ($(this).find(".btn-success").length>0) {
    $(this).find(".btn").toggleClass("btn-success");
  }
  if ($(this).find(".btn-info").length>0) {
    $(this).find(".btn").toggleClass("btn-info");
  }
  
  $(this).find(".btn").toggleClass("btn-default");
     
});